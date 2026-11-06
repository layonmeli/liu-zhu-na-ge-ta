# GitHub相近Skill对照与融合记录

核对日期：2026-11-05。检索范围为公开GitHub仓库中的沟通、NVC、情绪澄清和聊天记录分析类Skill。搜索发现后读取实际SKILL.md、按需参考文件，并通过GitHub API核对下列commit和许可证；不是仅依据搜索摘要选用。

累计采用8个项目中的部分工作方法：6个MIT、1个CC BY 4.0、1个Apache-2.0来源，重新组织为适合本技能的中文指引；未安装上游Skill、未运行仓库脚本、未接入其外部服务。相应署名、改编范围与许可声明保留在 [第三方声明](../THIRD_PARTY_NOTICES.md)。GitHub仓库本身不是心理学效果证据，原有研究依据仍见 [研究资料](sources.md)。

## 实际融合的八个来源

### G01 gusujushi：区分表达与事务目的

- 仓库：[gusujushi/gusujushi-nonviolent-communication](https://github.com/gusujushi/gusujushi-nonviolent-communication)
- 固定版本：[SKILL.md](https://github.com/gusujushi/gusujushi-nonviolent-communication/blob/c82bfc3bd58b3114cfaeff885b29f2f84b443abc/SKILL.md)
- 版本：`c82bfc3bd58b3114cfaeff885b29f2f84b443abc`；[MIT LICENSE](https://github.com/gusujushi/gusujushi-nonviolent-communication/blob/c82bfc3bd58b3114cfaeff885b29f2f84b443abc/LICENSE)。已读完整文件。
- 采用：将其情绪/事务分流改造成“希望被听懂，还是希望有一个具体行动”，仅在目标含糊时核对，落在主流程第3步及expression.md。
- 没有采用：把NVC框架当所有冲突的统一原因；强制每句话填齐四要素。原有感受、需要、请求区分已经具备，无需重复增加模板。

### G02 AYi：先让自己的版本说完整

- 仓库：[ayi-ai/ayi-nonviolent-communication](https://github.com/ayi-ai/ayi-nonviolent-communication)
- 固定版本：[SKILL.md](https://github.com/ayi-ai/ayi-nonviolent-communication/blob/edd2d077367978a462ec1a94ec440bc34014ae2b/SKILL.md)、[自我倾听参考](https://github.com/ayi-ai/ayi-nonviolent-communication/blob/edd2d077367978a462ec1a94ec440bc34014ae2b/references/empathy-and-self.md)
- 版本：`edd2d077367978a462ec1a94ec440bc34014ae2b`；[MIT LICENSE](https://github.com/ayi-ai/ayi-nonviolent-communication/blob/edd2d077367978a462ec1a94ec440bc34014ae2b/LICENSE)。已读上述内容及许可证。
- 采用：借鉴自我倾听的优先顺序，补充用户未说完时不催着换位思考、分批材料暂不下结论。落在主文件开场与ambiguous-language.md。
- 没有采用：用需要解释所有暴力，或者把“不”理解为并非拒绝。此技能仍尊重字面拒绝、明确边界和行为责任。

### G03 sincere-communication：本人语气与真诚检查

- 仓库：[LINKlin0123/sincere-communication-skill](https://github.com/LINKlin0123/sincere-communication-skill)
- 固定版本：[SKILL.md](https://github.com/LINKlin0123/sincere-communication-skill/blob/14ecbdc37508735371faa0816f3ffbfae607496d/SKILL.md)、[语气参考](https://github.com/LINKlin0123/sincere-communication-skill/blob/14ecbdc37508735371faa0816f3ffbfae607496d/references/de-ai-rules.md)
- 版本：`14ecbdc37508735371faa0816f3ffbfae607496d`；[MIT LICENSE](https://github.com/LINKlin0123/sincere-communication-skill/blob/14ecbdc37508735371faa0816f3ffbfae607496d/LICENSE)。本轮再次用API确认当前HEAD未变，并全文读Skill、四份references、两份examples、README、CHANGELOG和许可证。
- 采用：用用户已提供的日常聊天作措辞参照，核对称呼、长短和表达直接度，落在expression.md。不要求更多隐私样本，也不把一次气话当永久风格。
- 本轮增量：扩展不编造原则到内心历程、感情、态度与已完成的改变；将其“可移植测试”改为检查是否遗漏已有的真实细节，而非强制凑数。将具体责任与行动建议重组为真诚道歉、可承担的承诺，以及按实际回应继续对话，落在主文件与expression.md。参考：[de-ai-rules.md](https://github.com/LINKlin0123/sincere-communication-skill/blob/14ecbdc37508735371faa0816f3ffbfae607496d/references/de-ai-rules.md)、[apology.md](https://github.com/LINKlin0123/sincere-communication-skill/blob/14ecbdc37508735371faa0816f3ffbfae607496d/references/apology.md)。
- 设计转化：真诚允许隐私、复杂意愿和不确定；不强制先试探“还生气吗”，不为诚恳删除真实限制，也不把所有“但是”一律禁用。这些是本技能结合用户目标对上游做的重写与纠偏，不声称上游已经包含同样规则。
- 没有采用：固定情绪阈值、刻意制造真人语病、自我惩罚、统一到访建议、固定间隔催消息、默认两版及字数门槛，或把表面否认直接解释为仍然生气。[real-patterns.md](https://github.com/LINKlin0123/sincere-communication-skill/blob/14ecbdc37508735371faa0816f3ffbfae607496d/references/real-patterns.md) 声称源自平台案例却未提供可核出处，不作为实证依据。

### G04 Partner Text Coach：自己的草稿再试说

- 仓库：[curiositech/some_claude_skills](https://github.com/curiositech/some_claude_skills)
- 固定版本：[partner-text-coach/SKILL.md](https://github.com/curiositech/some_claude_skills/blob/d47e2e5ded912f448b36da6c391be724d3e50496/.claude/skills/partner-text-coach/SKILL.md)
- 版本：`d47e2e5ded912f448b36da6c391be724d3e50496`；[MIT LICENSE](https://github.com/curiositech/some_claude_skills/blob/d47e2e5ded912f448b36da6c391be724d3e50496/LICENSE)。已读Skill及完整许可证。
- 采用：将Talk-Back改成“核对本人意图—查看可能歧义—最小改一句”；文字沟通反复卡住时，可先表达核心一点，再由用户决定是否另谈。落在expression.md。
- 没有采用：将“fine/随便”固定翻译成受伤、由回复延迟推依恋、统一语气标尺，或一概要求当面处理关系。练习不会预测真实对方反应。

### G05 LoveLab：按事件看全上下文

- 仓库：[thc1006/lovelab-skills](https://github.com/thc1006/lovelab-skills)
- 固定版本：[lovelab-analyze](https://github.com/thc1006/lovelab-skills/blob/e76c0219137b9bb977aaa7273521ed2c96418158/skills/lovelab-analyze/SKILL.md)、[lovelab-nvc](https://github.com/thc1006/lovelab-skills/blob/e76c0219137b9bb977aaa7273521ed2c96418158/skills/lovelab-nvc/SKILL.md)、[lovelab-dynamics](https://github.com/thc1006/lovelab-skills/blob/e76c0219137b9bb977aaa7273521ed2c96418158/skills/lovelab-dynamics/SKILL.md)
- 版本：`e76c0219137b9bb977aaa7273521ed2c96418158`；[MIT LICENSE](https://github.com/thc1006/lovelab-skills/blob/e76c0219137b9bb977aaa7273521ed2c96418158/LICENSE)。已读三份Skill及许可证。
- 采用：将话题切分改成保留同一事件的起因、本人原句、紧接回应和后来补充；同时查找已说清的感谢、澄清、道歉或边界。落在ambiguous-language.md。
- 没有采用：依恋/NVC/权力分数、代词比率、关系预测、年龄文化自动归因；不把“只做朋友”改写为仍应争取特殊地位。发现修复表达不等于对方已接受。

### G06 Motivational Interviewing：容纳矛盾并找回本人选择

- 作者：heartpunk；项目：[motivational-interviewing-skill](https://github.com/heartpunk/motivational-interviewing-skill)。
- 固定版本：[SKILL.md](https://github.com/heartpunk/motivational-interviewing-skill/blob/ebc96be84935d4d79459fa2d3e3bba71f377c9ca/motivational-interviewing/skills/motivational-interviewing/SKILL.md)；commit `ebc96be84935d4d79459fa2d3e3bba71f377c9ca`。已读完整Skill、插件作者元数据和 [CC BY 4.0声明](https://github.com/heartpunk/motivational-interviewing-skill/blob/ebc96be84935d4d79459fa2d3e3bba71f377c9ca/LICENSE.txt)。
- 采用并改编：两种本人已说出的愿望可以并列映照；遇到含糊的“应该”时核对自己的意愿、认同的责任与外部期待；用户主动想找准备办法时，从本人确认有帮助的既往经历中找一小步。中文重写并限定到表达情境，落在主文件、ambiguous-language.md和uncertainty-and-encouragement.md。
- 没有采用：完整访谈协议、准备度打分、固定每轮提问后立即结束、拒绝成稿或鼓励的角色限制；不引导每个用户都把犹豫转为行动。只取上述流程启发，不声称正在提供治疗或已经获得上游背书。

### G07 Coach：可以映照一句，留出继续说的空间

- 作者：Taivo Pungas；项目：[taivop/marketplace](https://github.com/taivop/marketplace)。
- 固定版本：[Coach SKILL.md](https://github.com/taivop/marketplace/blob/c5280edfdca283c7cd698db4975cd9c77d96ab43/skills/coach/SKILL.md)；commit `c5280edfdca283c7cd698db4975cd9c77d96ab43`；[MIT LICENSE](https://github.com/taivop/marketplace/blob/c5280edfdca283c7cd698db4975cd9c77d96ab43/LICENSE)。已全文读Skill和许可证。
- 采用并改编：反映用户已经说出的关键词或两种愿望后，可以不追加问题；允许自然停顿，而不是每轮继续追问。落在主文件开场和ambiguous-language.md。
- 没有采用：即使标签不准确也以此推动探索、默认询问谈话预算、绝不替用户做事或给解决方案、默认引入身体聚焦或外部卡片练习。本技能仍可以按请求直接成稿。

### G08 SocialCoach：依据本人原话、当时信息与实际回应复盘

- 作者：SocialCoach contributors；项目：[GeminiLight/SocialCoach](https://github.com/GeminiLight/SocialCoach)。这是网页应用，本次只借鉴有关复盘的指引。
- 固定版本：commit `21af5281e80064c867bfbe0b4763e8e2f20c0fd4`；[README](https://github.com/GeminiLight/SocialCoach/blob/21af5281e80064c867bfbe0b4763e8e2f20c0fd4/README.md)、[prompts.ts](https://github.com/GeminiLight/SocialCoach/blob/21af5281e80064c867bfbe0b4763e8e2f20c0fd4/app/src/lib/prompts.ts)、[debrief-prompt.ts](https://github.com/GeminiLight/SocialCoach/blob/21af5281e80064c867bfbe0b4763e8e2f20c0fd4/app/src/lib/tasks/debrief-prompt.ts)、[Apache-2.0 LICENSE](https://github.com/GeminiLight/SocialCoach/blob/21af5281e80064c867bfbe0b4763e8e2f20c0fd4/LICENSE)。已读README、debrief全文，prompts的公共原则/评估段落与模式提取选段，以及LICENSE；没有审阅或运行整个应用。
- 采用并改编：先以本人实际原句为依据；修改当时措辞只用当时可知信息；区分提议、同意和落实；不把对方答应解释成已经原谅或没有受伤。重写为expression.md中的按需简短复盘，补强原先已有的“表达与结果分开”原则。
- 没有采用：评分、固定练习轮次、能力画像、应用服务、长期训练路径。用户只要一句文案或鼓励时不强制进行复盘。树路径检索未见根目录NOTICE，发现的视频NOTICE仅涉及视频/语音材料，本次没有使用这些材料。

## 读过但没有融入的方法

| 候选 | 核对范围与版本 | 本次取舍 |
| --- | --- | --- |
| [relationship-deep-analysis](https://github.com/LibertyZero10/relationship-deep-analysis/blob/84df890869a1cc0529e63393b93dc2d445a951bb/SKILL.md) | SKILL与完整MIT许可证；commit `84df890869a1cc0529e63393b93dc2d445a951bb` | 身份、时间核对已经具备；不采用从频率、延迟等推出人格、防御或关系走向的框架。 |
| [ai-heartpower-coach](https://github.com/zhaocathy1221-hash/ai-heartpower-coach/blob/c9570a08514c5baea8e14310d2603d21de579060/SKILL.md) | Skill与仓库根目录；commit `c9570a08514c5baea8e14310d2603d21de579060`；API未识别许可，根目录未见LICENSE | 倾听方向相近，但七题画像和创业者模式偏离当前任务；未复制其内容。 |
| [howtotalk / active-listening](https://github.com/wuraaang/claude-code-skills/tree/d90b100bcd398b823659fea902229047fe838cbe) | howtotalk入口、active-listening主要段落及根目录；commit `d90b100bcd398b823659fea902229047fe838cbe`；未确认许可 | 十余框架路由过重；不引入身体动作推断或同理心打分。现有倾听依据来自原先SAMHSA资料。 |
| [love-skill](https://github.com/pajama-studio/love-skill/blob/316bf52d90ff7c37f361007fa9ebdbfdbff51ce0/SKILL.md) | 入口与Skill中框架、权限、性别/依恋相关选段；commit `316bf52d90ff7c37f361007fa9ebdbfdbff51ce0`；未确认许可 | 侧重伴侣咨询、多理论和外部演化接口；未引入分类、联网接口或脚本。未声称精读其全部参考材料。 |
| [ReplyHer](https://github.com/replyher/replyher-skill/blob/4c256188fa6c275ea996d273a24e211a34288fca/SKILL.md) | 完整Skill与MIT许可证；commit `4c256188fa6c275ea996d273a24e211a34288fca` | 截图取材有重合，但解读潜台词、推拉策略、固定多选回复和推广引导不适合；未采用。 |
| [guided-journaling-skill](https://github.com/jasonge27/guided-journaling-skill/blob/57d79d58b70e8d6c7bde602ce0783b106b0f619a/skills/guided-journaling/SKILL.md) | 本轮读取主Skill及MIT许可证，前次另读README和reflective/relationship参考；commit `57d79d58b70e8d6c7bde602ce0783b106b0f619a` | 倾听、复盘与按用户需要回应已覆盖；没有为凑来源增加日记、逐字存档或默认读全部历史。 |
| [relationship-science-coach](https://github.com/tristanmanchester/agent-skills/blob/main/relationship-science-coach/SKILL.md) | 本轮快速复核当前主Skill及LICENSE，未深读整套参考 | 与事实/解释分开、本人自主和短请求直接帮助等现有原则高度重合；许可写明Internal-use-only，本次不纳入分发内容。 |

## 维护说明

以上固定版本用于追溯，不代表永久推荐其最新内容；星标数没有被用作有效性证明。融合没有改变技能的判断原则：用户能否认模型的解释，已确认的拒绝不会被改写，普通对话不会先变成问卷。新增内容也不要求安装上述项目或进行网络调用。
