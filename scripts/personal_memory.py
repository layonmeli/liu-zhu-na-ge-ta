#!/usr/bin/env python3
"""Local, opt-in Yuyan memory. Store short summaries, never raw conversations.

The default store is ~/.yuyan/memory.json, outside this skill package. Entries
expire after their expires_at UTC date (that date itself is inclusive).
All output is UTF-8 JSON. No networking, backups, or persistent logs are used.
"""

import argparse
from contextlib import contextmanager, nullcontext
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time


SKILL_ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ("expression", "support", "values", "context", "pattern")
ENTRY_FIELDS = {
    "id", "category", "content", "status", "source", "scope",
    "updated_at", "expires_at",
}
REQUIRED_INPUT = ENTRY_FIELDS - {"updated_at", "expires_at"}
LOCK_TIMEOUT = 5.0


class MemoryError(ValueError):
    """A user-readable validation or storage error."""


def utc_today():
    return datetime.now(timezone.utc).date()


def parse_date(value, field):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise MemoryError(f"{field}: expected a YYYY-MM-DD date")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise MemoryError(f"{field}: invalid calendar date") from exc


def short_text(value, field, maximum):
    if (not isinstance(value, str) or not value.strip()
            or len(value) > maximum
            or any(ord(c) < 32 or 0xD800 <= ord(c) <= 0xDFFF for c in value)):
        raise MemoryError(f"{field}: expected non-empty single-line text, max {maximum} characters")
    return value.strip()


def validate_entry(value, field="entry", incoming=False, today=None):
    if not isinstance(value, dict):
        raise MemoryError(f"{field}: expected a JSON object")
    required = REQUIRED_INPUT if incoming else ENTRY_FIELDS
    missing, extra = required - value.keys(), value.keys() - ENTRY_FIELDS
    if missing or extra:
        raise MemoryError(f"{field}: missing fields {sorted(missing)}; unknown fields {sorted(extra)}")
    entry = dict(value)
    for key, maximum in (("id", 80), ("content", 1000), ("source", 160), ("scope", 160)):
        entry[key] = short_text(entry[key], f"{field}.{key}", maximum)
    if entry["category"] not in CATEGORIES:
        raise MemoryError(f"{field}.category: expected one of {', '.join(CATEGORIES)}")
    if entry["status"] not in ("confirmed", "tentative"):
        raise MemoryError(f"{field}.status: expected confirmed or tentative")
    if "updated_at" in entry:
        parse_date(entry["updated_at"], f"{field}.updated_at")
    if incoming:
        entry["updated_at"] = today.isoformat()
    entry.setdefault("expires_at", None)
    if entry["expires_at"] is None:
        if entry["status"] == "tentative":
            raise MemoryError(f"{field}.expires_at: required for tentative entries")
    else:
        expiry = parse_date(entry["expires_at"], f"{field}.expires_at")
        updated = parse_date(entry["updated_at"], f"{field}.updated_at")
        if expiry < updated:
            raise MemoryError(f"{field}.expires_at: must not precede updated_at")
    return entry


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise MemoryError(f"JSON: duplicate field {key!r}")
        result[key] = value
    return result


def read_json(path, label):
    try:
        source = nullcontext(sys.stdin) if str(path) == "-" else path.open("r", encoding="utf-8-sig")
        with source as handle:
            return json.load(handle, object_pairs_hook=reject_duplicate_keys)
    except json.JSONDecodeError as exc:
        raise MemoryError(f"{label}: invalid JSON at line {exc.lineno}, column {exc.colno}; not overwritten") from exc
    except UnicodeError as exc:
        raise MemoryError(f"{label}: expected UTF-8 JSON; not overwritten") from exc


def blank_store():
    return {"schema_version": 1, "enabled": False, "entries": []}


def load_store(path):
    if not path.exists():
        return blank_store()
    data = read_json(path, "store")
    if not isinstance(data, dict) or set(data) != {"schema_version", "enabled", "entries"}:
        raise MemoryError("store: expected only schema_version, enabled, entries; not overwritten")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise MemoryError("store.schema_version: only version 1 is supported; not overwritten")
    if type(data["enabled"]) is not bool or not isinstance(data["entries"], list):
        raise MemoryError("store: enabled must be boolean and entries must be a list; not overwritten")
    entries, ids = [], set()
    for index, value in enumerate(data["entries"]):
        entry = validate_entry(value, f"store.entries[{index}]")
        if entry["id"] in ids:
            raise MemoryError("store.entries: duplicate id; not overwritten")
        ids.add(entry["id"])
        entries.append(entry)
    data["entries"] = entries
    return data


def resolve_store(value):
    path = Path(value).expanduser().resolve()
    try:
        path.relative_to(SKILL_ROOT)
    except ValueError:
        pass
    else:
        raise MemoryError("--store: must be outside the skill package directory")
    if path.is_dir():
        raise MemoryError("--store: expected a file, not a directory")
    return path


@contextmanager
def store_lock(path):
    """Serialize the complete read/modify/replace operation; never steal a lock."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_name(path.name + ".lock")
    deadline = time.monotonic() + LOCK_TIMEOUT
    while True:
        try:
            descriptor = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            break
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise MemoryError("store is locked; retry later. A leftover lock requires manual inspection")
            time.sleep(0.05)
    try:
        yield
    finally:
        os.close(descriptor)
        lock_path.unlink()


def write_store(path, data):
    descriptor, temporary = tempfile.mkstemp(prefix="." + path.name + ".", suffix=".tmp", dir=path.parent)
    temporary = Path(temporary)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def active(entry, today):
    return entry["expires_at"] is None or parse_date(entry["expires_at"], "expires_at") >= today


def metadata(data, today, exists):
    count = sum(active(entry, today) for entry in data["entries"])
    return {"schema_version": 1, "exists": exists, "enabled": data["enabled"],
            "entry_count": len(data["entries"]), "active_count": count,
            "expired_count": len(data["entries"]) - count}


def execute(args, path):
    today = utc_today()
    data = load_store(path)
    if args.command == "status":
        return metadata(data, today, path.exists())
    if args.command == "read":
        limit = args.limit if args.limit is not None else (0 if args.inspect else 20)
        entries = data["entries"] if data["enabled"] or args.inspect else []
        if not args.inspect:
            entries = [entry for entry in entries if active(entry, today)]
        if args.category:
            entries = [entry for entry in entries if entry["category"] == args.category]
        if args.scope:
            entries = [entry for entry in entries if args.scope.casefold() in entry["scope"].casefold()]
        selected = entries[:limit] if limit else entries
        return {"schema_version": 1, "enabled": data["enabled"], "inspect": args.inspect,
                "total_matches": len(entries), "count": len(selected),
                "truncated": len(selected) < len(entries), "entries": selected}
    if args.command == "init" and path.exists():
        return dict(metadata(data, today, True), changed=False)

    result = {}
    if args.command in ("enable", "disable"):
        data["enabled"] = args.command == "enable"
    elif args.command == "upsert":
        if not data["enabled"]:
            raise MemoryError("memory is disabled; enable it explicitly before writing")
        entry = validate_entry(read_json(Path(args.input).expanduser(), "input"), "input", True, today)
        old_index = next((i for i, old in enumerate(data["entries"]) if old["id"] == entry["id"]), None)
        if old_index is None:
            data["entries"].append(entry)
        else:
            data["entries"][old_index] = entry
        result = {"operation": "inserted" if old_index is None else "updated", "updated_at": entry["updated_at"]}
    elif args.command == "forget":
        if args.all:
            result["removed_count"] = len(data["entries"])
            data = blank_store()
        else:
            before = len(data["entries"])
            data["entries"] = [entry for entry in data["entries"] if entry["id"] != args.id]
            if len(data["entries"]) == before:
                raise MemoryError("forget: id not found; no changes made")
            result["removed_count"] = 1
    before = len(data["entries"])
    data["entries"] = [entry for entry in data["entries"] if active(entry, today)]
    result["expired_removed_count"] = before - len(data["entries"])
    write_store(path, data)
    return dict(metadata(data, today, True), **result, changed=True)


def nonnegative_integer(value):
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected a nonnegative integer") from exc
    if number < 0:
        raise argparse.ArgumentTypeError("expected a nonnegative integer")
    return number


def parser():
    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument("--store", default=argparse.SUPPRESS, help="JSON file outside the skill package")
    root = argparse.ArgumentParser(description=__doc__, parents=[shared])
    commands = root.add_subparsers(dest="command", required=True)
    for command in ("init", "enable", "disable", "status"):
        commands.add_parser(command, parents=[shared])
    read = commands.add_parser("read", parents=[shared])
    read.add_argument("--inspect", action="store_true", help="explicit user inspection: include disabled and expired entries")
    read.add_argument("--category", choices=CATEGORIES)
    read.add_argument("--scope", help="case-insensitive substring of scope")
    read.add_argument("--limit", type=nonnegative_integer, help="0 means all; default 20, or all with --inspect")
    upsert = commands.add_parser("upsert", parents=[shared])
    upsert.add_argument("--input", required=True, help="one UTF-8 JSON entry file, or - for stdin; summaries only, no raw chat")
    forget = commands.add_parser("forget", parents=[shared])
    selection = forget.add_mutually_exclusive_group(required=True)
    selection.add_argument("--id")
    selection.add_argument("--all", action="store_true", help="empty all entries and disable memory")
    return root


def main(argv=None):
    if hasattr(sys.stdin, "reconfigure"):
        sys.stdin.reconfigure(encoding="utf-8-sig", errors="strict")
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = parser().parse_args(argv)
    try:
        path = resolve_store(getattr(args, "store", Path.home() / ".yuyan" / "memory.json"))
        # A first read/status does not create a memory directory.
        if args.command in ("read", "status") and not path.parent.exists():
            result = execute(args, path)
        else:
            with store_lock(path):
                result = execute(args, path)
        print(json.dumps(result, ensure_ascii=False, allow_nan=False))
        return 0
    except (MemoryError, OSError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
