import pathlib
base = pathlib.Path(r"E:\github\dsh\projects\helloworld -unrealengine\Documentation")
base.mkdir(parents=True, exist_ok=True)

def w(name, content):
    (base / name).write_text(content.strip()+"\n", encoding="utf-8")
    print(f"wrote {name} {len(content)} chars")

# 00 Phase0
w("00_Phase0_ExperienceValidation.md", r"""
# Phase 0 — 大众体验验证 (Mass-Market Experience Validation)

> 回答 5 个第一性原理问题。每个 >250 字，有具体场景、操作、情绪曲线。

---

## Q1: 首因效应 — 前 5 分钟 (First 5 Minutes)

### 设计目标
第 30 秒在操作，第 3 分钟理解乐趣，第 5 分钟想截图分享。拒绝播片陷阱。

### 分镜脚本 (精确到秒)

**0:00-0:15 启动即操作**
无 Logo 堆砌。黑屏中传来织机“咔嗒”声（MetaSounds），一束线光从屏幕中心拉开——玩家已在操作：鼠标/右摇杆轻拉，线光跟随。字幕只有一句：“拉开它。”（无术语、无教学文字）。Lumen 的第一缕光从裂缝漏出，照亮织者手套的纤维（Nanite 微观细节：针脚清晰到 0.2mm）。

**0:15-0:45 第一次撕裂 (Tear)**
教学不是文字，是**地形**：前方堵住去路的是一面“破布墙”——明显比周围旧、颜色不同。玩家本能地对它按住 **Weave (LMB/RT)** 并拖动。Chaos Field 生效：墙像布一样被撕开，碎屑按布料物理飞散，Niagara 火星沿撕裂边燃烧。音效：布帛撕裂 + 低沉嗡鸣（MetaSounds 参数 `TearTension` 随拖动速度变尖锐）。情绪：**权力感**——“我弄坏了世界，但世界没有惩罚我，反而通了路。”

**0:45-1:30 第一次拖拽 (Drag)**
墙后是一个小庭院：一侧是岩浆池（Obsidian Forge 的橙红 Light），一侧是薄雪（Frostvein 白）。引导：雪地上有干枯的幼苗，提示“需要 тепло”。玩家把岩浆池边缘的一块“熔岩方块”（发光、可拖）撕下来，拖过裂缝，放在雪地上。Lumen 实时 GI：橙光在雪上晕开，幼苗 3 秒内冒芽、开出半透明小花（Substrate 材质混合）。旁观者（父母/女友）此刻会说：“哇它活了！”——**非玩家入口**。

**1:30-3:00 第一次协作幽灵 (Async hint)**
进入织机神殿大厅，中央悬浮着“心织机”——3 个空槽（对应 3 生态）。墙上投影出**异步幽灵**：另一个玩家（录像）曾在这里把雨林的发光藤蔓拖来缠住柱子。玩家模仿：撕开侧墙（通往 Luminous Canopy 的临时裂缝），拖一束藤蔓回来，藤蔓自动缠柱、点亮通路。系统提示：“+1 编织”并触发 **自动 Photo Mode**：镜头拉远，角色站在三种光混合的门前，UI 只有“按 Share 分享”。前 3 分钟闭环：**撕 → 拖 → 缝 = 创造**，已被身体记住。

**3:00-5:00 第一个合作谜题 (2 人镜像)**
若单人：AI 伙伴“线灵”(MassAI + StateTree)会举起对侧锚点，示意“一起拉”。
若双人：两人各站一侧，每人按 **Anchor (RMB/LT)** 钉住裂缝两端，裂缝才稳定；一人松手，裂缝像橡皮筋回弹（Chaos 回弹）。必须语音/手势协调：“我数 3 一起拉”。成功后，整面墙倒下露出远景——16km² 的 World Partition 世界无缝展开，3 个生态在远处同时可见（Nanite 远景无 pop + Lumen 天光统一）。BGM 在 Quartz 时钟上切入主旋律（MetaSounds `BiomeBlend=0.33` 三分和声）。情绪曲线：**好奇 → 权力 → 惊喜 → 欢笑 → 敬畏**。第 5 分钟，玩家已分享第一张截图——社交货币完成。

### 为什么不劝退
- 零死亡：掉入岩浆被线拉回（参考双人成行复活），失败只回 3 秒前。
- 零文字教学：所有引导是光、颜色、声音、地形 affordance。
- 极低操作：全程只用 Weave/Anchor/Interact，冲刺/跳跃被缝合进 Weave 手势（长按 Weave = 冲刺撕）。

---

## Q2: 社交的化学反应 — 1+1>2 还是各玩各的？

### 选择：强制协作 + 轻异步 (Force-Coop + Async Share)

**核心机制：锚点耦合物理 (Coupled Anchor Physics)**
- 每个 rift 需要 `N` 个锚点（2-4），每个锚点由不同玩家持有。
- 裂缝稳定性 `S = f(锚点数, 角度误差, 拖动速度)`。单人 `S_max=0.6`（只能做小缝），双人 `S=0.9`（可拖整块地形），四人 `S=1.2`（可搬运瀑布、整段城墙）。
- 物理是耦合的：`A 拉左边，B 拉右边，河水才流动`。若只有一人，河水只在原地打旋。

**场景 1：温泉胡闹 (Obsidian + Frostvein)**
- 4 人：A/B 钉住火山口裂缝，C 用藤蔓引水，D 把雪块拖来做池壁。岩浆遇雪 → Chaos 蒸汽 + Niagara 沸腾 + Lumen 暖雾。四人同时被蒸汽遮挡视野，笑成一片，但池子真的留在了世界里（World Partition 持久化），其他玩家路过可泡（回血）。
- 单人：只能做“迷你温泉”，无蒸汽奇观。
- **化学反应**：混乱是乐趣，不是惩罚。像“胡闹厨房”——越乱越好笑，但乱中有成就。

**场景 2：空中花园 (Luminous + Obsidian)**
- 需要 3 人：1 人在地面锚定，1 人在浮岛锚定，1 人在中间编织藤蔓桥。桥的张力实时计算（Chaos Cloth），人走上去会晃，队友必须“绷紧”——按住 Anchor 不放，手会抖（手柄 haptics + 屏幕边缘织线绷紧特效）。
- 旁观者视角：看朋友在晃桥上尖叫，比自己玩还好笑——**直播友好**。

**异步社交 (死亡搁浅式)**
- 你造的温泉、桥、花园会以 **DataLayer 幽灵** 出现在好友/陌生人的世界（Iris 稀疏同步，低带宽）。
- 你可以给别人的造物“点亮”（Interact），对方会收到 MetaHuman 感谢信（异步邮件 + 小奖励）。
- 市集 (Plaza, 50 人)：展示全服最赞的 10 个玩家编织（投票），逛市集本身是社交——像动森看别人家。

**为什么 1+1>2**
- 单人是解谜（静），多人是物理喜剧（动）。
- 失败也好笑：锚点没对齐导致整条河倒灌进村庄（但无惩罚，村民 MassAI 会撑伞吐槽）。
- 记忆点：玩家事后回忆的不是“我解了谜”，而是“我们把火山倒进了雪地，结果把队友煮了”。

---

## Q3: 创造的欲望 — 社交货币生成器

### 不是“我们有建造模式”，而是“你不得不分享”

**生成器 1：不可能的混搭 (Impossible Mix)**
- 规则：任意两个生态的材质/光/物理可混合。系统不预设“温泉”——温泉是玩家发现的涌现（岩浆 + 雪 + 池壁 = 蒸汽 + 热水材质）。类似化学实验，组合数 = 3 生态 × 12 材质 × 8 光 = 288 种“新物质”，每种有独特 Substrate 外观 + Niagara + 音效。
- **分享点**：玩家会发“你们见过紫色极光下的岩浆瀑布吗？我把极光拖进了火山口”。
- 截图自动构图：Lumen 保证无论怎么混，光都好看；Nanite 保证裂缝边缘细节经得起 4K 放大。

**生成器 2：织机工坊 (Loom Workshop)**
- 解锁 40+ 织纹 (Pattern DataAsset)：不是数值，是视觉——“龙鳞缝”“冰裂纹”“藤蔓编”。玩家在工坊中用 3D 预览调参（Substrate 图层 + Niagara 强度），一键应用到世界某条裂缝。
- 工坊作品可命名、上架市集、被他人订阅。创作者获“线币”（cosmetics 货币，非付费）。
- 病毒案例：幻兽帕鲁的“道德模糊”梗 → 我们的梗是“把队友缝进墙里当装饰”（物理允许，但队友可一键挣脱，纯搞笑）。

**生成器 3：照片即任务**
- 每次重大编织后 2 秒触发 Photo Mode，快门声 + 轻微慢动作。照片带坐标水印与 Pattern 标签，分享到 Discord/微博/B站一键带话题 `#RiftWeave`。
- 每周摄影赛：主题如“最离谱的温泉”，获胜作品变成游戏内海报（World Partition 广告牌）。

**为什么天然适合发朋友圈**
- 视觉奇观：Lumen 跨维度光混合是其他引擎难做的——橙+青+荧光绿的 GI 在一张图里，现实中不存在，故新鲜。
- 故事性：每张图背后有个胡闹故事（“我们本想修桥，结果造了瀑布”），比单纯风景照更有谈资。
- 低门槛：不需要技术，胡闹即创造。

---

## Q4: 持续新鲜感 — 1 / 10 / 50 / 100 小时在追求什么？

### 涌现系统：简单规则 → 无限组合

**3 条底层规则**
1. **物质守恒**：拖走的物质在源头消失，在目标出现（World Partition 持久化）。
2. **属性继承**：熔岩保持“热”标签，冰保持“冷”，藤保持“生长”，光保持“颜色”。热+冷=蒸汽，热+生长=焦藤，冷+光=折射。
3. **稳定性经济**：每条裂缝有稳定性预算，锚点数与 Pattern 质量决定能否维持大工程。

**时间曲线**

**第 1 小时：惊奇 (Wonder)**
- 目标：学会撕拖缝，完成 3 个生态的入门谜题（各 10 分钟）。
- 追求：看遍 3 种光、摸遍 3 种材质。收集 5 个基础 Pattern。
- 情绪：每 5 分钟一次“哇”。

**第 10 小时：掌握 (Mastery)**
- 目标：心织机的第一颗心（Obsidian 心）修复，需要 6 个谜题 + 1 个 4 人大型编织（搬运熔岩河）。
- 追求：解锁进阶 Pattern（需跨生态组合），尝试把不同生态的动植物混养（MassAI 会迁移：把 Frostvein 的 elk 赶进 Canopy 会发光）。
- 新鲜感来源：谜题开始要求角度/速度（Weave 技巧），失败会产生意外但有趣的副作用（把村庄冻住 → 村民改穿棉袄，彩蛋）。

**第 50 小时：表达 (Expression)**
- 目标：第二颗心 + 工坊大师。开始为市集造景，为拍照赛投稿。
- 追求：收集全 40 Pattern，挑战日替裂缝（Daily Rift：随机地形 + 随机目标，如“用风把花粉送进火山”）。
- 涌现：玩家社区发现“岩浆+冰+藤+极光”四重混合会产生“星空温泉”（Substrate 星点 + Lumen 四色 GI），官方未设计，靠规则自然出现——成为新 meta。

**第 100 小时：传承 (Legacy)**
- 目标：第三颗心 + 全成就 + 工坊人气作品。
- 追求：带新人（ mentor 系统：老玩家当锚点，新人主编织，双方得奖励）、UGC 赛季（官方提供新 Pattern 工具，赛季主题“机械织”）、速通（Speedweave 排行榜：最快缝合某裂缝）。
- 反重复设计：World Partition + PCG 每周刷新的野生裂缝 + 异步幽灵的无限供给，保证地图永不耗尽。

**防重复 3 招**
- 不做重复任务：所有“收集”都是为编织服务的，不是单独 fetch。
- 每 10 小时刷新规则：新 Pattern 改变物理（如“弹性缝”让桥会弹）。
- 玩家即内容：市集与幽灵保证你永远能看到别人没见过的混搭。

---

## Q5: 非玩家的入口 — 旁观者乐趣 + 极低门槛

### 旁观者乐趣 (Spectator Joy)

**视觉即剧情**
- 即使不懂操作，看 Lumen 光在裂缝间流动就值回票价——像看染色实验。主播把岩浆倒进雪地时，弹幕会刷“煮雪”“温泉诞生”。
- MassAI 提供的“活着感”：2k elk 迁徙、500 无人机巡逻、村民对编织的实时反应（鼓掌/撑伞/拍照），让直播画面永远不静止。

**戏剧性时刻 (Streamable Moments)**
- **物理喜剧**：四人拉桥，桥突然断裂，四人一起掉进自己造的温泉——必被剪成切片。
- **美学奇观**：夜晚把 Canopy 的荧光拖进 Frostvein 冰洞，冰洞瞬间变成水晶宫——适合做封面图。
- **温情彩蛋**：修复 Frostvein 的“等待的孩子”记忆时，全洞冰融花开，MetaHuman 孩子会抱住玩家——即使旁观者也会感动（像看皮克斯短片）。

**极低门槛入口**

**操作**：3 键 + 移动视角。Weave 是长按拖，Anchor 是点按，Interact 是 E/A。没有连招、没有 QTE、没有精确平台跳跃（MotionWarping 自动吸附）。手残也能通关主线——难题有“安全网”：超时后线灵会示意正确角度，或允许降低难度（稳定性要求 -30%）。

**认知**：叙事主线是“回家/修复”（孩子等春天、老人守火炉），无需游戏术语。深层叙事藏在环境：墙上的织纹、村民日记、MassAI 的迁徙路线——不看也不影响通关。

**社交入口**：
- **沙发共玩**：支持分屏/同屏协作（PS5 同机 2 人 + 线上 2 人），父母按一个键就能当“锚点工具人”，孩子主编织，双方都有贡献。
- **云观战**：市集广场支持 50 人围观大型编织，围观者可扔“荧光粉”（Niagara）助威，无操作压力但有参与感。
- **一键分享**：Photo Mode 到分享只需 2 步，比游戏内截图更快。

**一句话让非玩家想试**
> “这不是打怪，是和朋友一起把世界当橡皮泥玩——把火山倒进雪地，把极光缝进雨林，每次胡闹都会留下发光的疤痕，别人路过会为你鼓掌。”

---
*Phase 0 完成 — 进入提案。*
""")

w("01_GameProposal.md", r"""
# Phase 1 — 项目提案 (Game Proposal)

## 游戏名称
**RIFTWEAVE / 织裂者**  
- 英文：RIFTWEAVE — Weavers of the Torn World
- 中文：织裂者 — 缝合纪元
- 记忆点：Rift (裂缝) + Weave (编织)，动词感强，易传播；中文“织裂”制造矛盾张力。

## 核心定位 (一句话让非玩家也想试)
> 和朋友一起把世界当布料撕开——把火山倒进雪地泡温泉，把极光缝进雨林点亮夜空，每次胡闹都会留下发光的疤痕。

## 类型标签
**开放世界 × 合作解谜 × 创造模拟 × 轻叙事冒险**  
- 非战斗核心（无传统血条），物理与光是武器。
- 4 人合作解谜为主，单人可玩（AI 线灵补位），50 人广场异步社交。

## 核心机制 (≤100 字，每 5 分钟在做什么)
**撕(Weave) → 拖(Drag) → 钉(Anchor) → 缝(Stitch)**。按住 Weave 撕开维度裂缝，拖动物质/光/生物跨维度，队友钉锚点稳定裂缝，释放完成编织。物质保留属性，跨生态产生涌现（蒸汽/生长/折射）。

## 反直觉设计 (违反品类常识但有效)
**破坏即创造，且越多人越不稳定反而越有趣。**  
传统合作游戏追求“配合完美”，RIFTWEAVE 故意让 4 人物理耦合——桥会晃、河会溢、蒸汽会遮挡。完美配合能造奇观，配合失误会造喜剧，但两者都留下持久、可分享、被他人点赞的世界痕迹。失误不是惩罚，是新的社交货币。

## UE5 技术杠杆 (其他引擎做不到的体验)
- **Nanite + Chaos 耦合撕裂**：Nanite 让裂缝边缘保持像素级纤维细节（其他引擎 LOD 会糊），Chaos Field 让撕裂是真实物理破坏——可撕到 0.2mm 纤维，再缝合无痕。玩法上，玩家可把整座山按纤维方向撕成条，再编成桥。
- **Lumen 跨维度 GI 作为谜题**：Lumen 的实时多重 GI 让“拖光”成为资源——把 Obsidian 的橙光拖进 Frostvein 冰洞，冰的折射会改变光路，照亮 Canopy 种子使其生长。光路是物理可玩的，非贴图。
- **MassAI 2000+ 异构群体的涌现迁徙**：3k elk/drone/sprite 同屏，每群有不同 StateTree（迁徙/恐慌/趋光），玩家编织会改变地形与光，直接重路由群体——观看 Mass 迁徙改道本身是玩法（摄影任务）。

## 社交设计
- **主要**：4 人强制合作（锚点机制）+ 2 人沙发同屏 + 50 人广场。
- **异步**：死亡搁浅式 DataLayer 幽灵——你的温泉/桥以低精度幽灵出现在他人世界，可点亮致谢。
- **为什么 1+1>2**：单人是静谜（S=0.6），4 人是动态物理喜剧（S=1.2）+ 持久世界改变 + 直播切片。人越多，涌现越离谱，分享欲越强。

## 首 5 分钟体验 (逐分钟)
见 Phase0 Q1 分镜。0:00 拉线光 → 0:30 撕布墙 → 1:30 拖岩浆救幼苗 → 3:00 模仿幽灵缠藤 → 5:00 四人锚点倒墙见全景 + 自动 Photo。

## 100 小时内容规划
| 阶段 | 小时 | 追求 | 内容量 |
|------|------|------|--------|
| 惊奇 | 1 | 学会撕拖缝，看遍 3 生态光 | 3 入门谜题 + 5 Pattern |
| 掌握 | 10 | 修复第一颗心 (Obsidian)，掌握角度/速度 | 6 谜题 + 1 大型 4 人编织 |
| 表达 | 50 | 工坊大师，市集造景，日替裂缝 | 40 Pattern + Daily Rift + 摄影赛 |
| 传承 | 100 | 带新人、赛季 UGC、速通榜 | 赛季主题 + Creator Fund |

主线 20h (3 心)，可重复 100h+ (Daily/工坊/摄影/速通/幽灵)。

## 与 3 个现有 UE 项目的差异化
| 项目 | 同 | 异 |
|------|----|----|
| **双人成行** | 强制合作、每关新玩法 | 我们无战斗、合作是物理耦合而非关卡脚本；世界是开放连续而非线性关卡 |
| **黑神话：悟空** | UE5 电影级美术、文化独特性 | 我们面向大众零死亡惩罚、非硬核战斗；美术是混搭奇观而非写实神话 |
| **堡垒之夜** | 建造+社交、实时活动 | 我们建造是跨维度物质守恒 + Lumen 光学，非方块；社交是小队物理喜剧 + 异步幽灵，非大逃杀 |

## 目标平台
**PC (Steam/Epic, 首发) + PS5 + Xbox Series X|S**。  
- PC 最高画质：Nanite 1px/边，Lumen HWRT，Chaos 4 线程。
- PS5/XSX：动态 4K/60，Nanite 2px，Lumen SWRT 回退，Mass 1500。DualSense 自适应扳机模拟撕裂张力。
- Switch (云版评估)：若做原生，需 Nanite 关、Chaos 简化、Mass 300，暂不首发。

## 商业模式
**买断制 + 仅外观 (Cosmetics Only)** — 29.99 USD。
- 无数值付费，无 Pay-to-Win。付费仅织纹样式、表情、家园装饰。
- 所有付费外观可通过编织精通解锁（线币），可交易。
- 赛季通行证 (9.99) 解锁当季 Pattern 抢先体验，非独占，赛季后可肝。
- Creator Fund：市集人气工坊按订阅分成，激励 UGC。
""")

w("02_WorldAndNarrative.md", r"""
# 世界观与叙事架构

## 世界观设定 (≤300 字，独特)

世界是一块被“织机”织就的布。远古织者为防虚无，用三根主线织出大陆：**燃线 (Obsidian)**、**寒线 (Frostvein)**、**生线 (Canopy)**。织机崩塌后，三线断裂，世界裂成三块浮岛，裂缝中漏出虚无（无光无色的“白”）。玩家是当代织者，针能撕开线隙、拖动线的物质与光、再缝合。缝合不是“修复原样”，而是**混织**——把燃线缝进寒线，寒线缝进生线，让世界以新的、更绚丽的方式完整。虚无不是怪物，是“未被编织的空白”，会被玩家的编织自然驱散。

## 主线故事大纲 (12 关键节点)

1. **醒于织机**：玩家在崩塌织机神殿醒来，线灵 (Loom Spirit, MetaHuman 少女) 唤醒你。
2. **第一课·撕**：撕开布墙，学会 Weave。
3. **第一课·拖**：拖岩浆救幼苗，见证“热+冷=生”。
4. **幽灵低语**：见异步幽灵的藤蔓，学会跨维度。
5. **Obsidian 心·entrant**：进入燃线浮岛，火山熄灭、锻父失语。
6. **锻父的固执**：环境叙事——锻父为保火种拒绝让寒线进入，导致全岛过热崩裂。谜题：把雪拖入锻炉，锻父回忆起妻儿在雪中等待。
7. **Frostvein 心·entrant**：寒线浮岛永冬，孩子等待春天。
8. **孩子的等待**：孩子为等父母归来拒绝让燃线进入，导致永冻。谜题：把 Canopy 的荧光拖入冰洞，冰中开花，孩子明白“等待不是静止”。
9. **Canopy 心·entrant**：生线浮岛过度生长，记忆过载。
10. **森林的记忆**：森林为记住所有人而拒绝让虚无（空白）进入，导致窒息。谜题：撕开记忆茧，让白进入——空白让森林学会遗忘，鸟群回归。
11. **心织机·缝合**：三心归位，玩家在神殿用三线混织整片大陆（4 人大型编织，16km² 全可见，Lumen 三色融合）。
12. **新布**：世界不是恢复原样，而是成为三色混织的新布。玩家成为新织机守护者，开放 Live 赛季。

## 环境叙事设计 (如何通过场景讲故事)

- **织纹语言**：每道裂缝的织纹密度 = 该地记忆强度。高密度织纹 = 有人反复缝补（执念），稀疏 = 被遗忘。
- **MassAI 痕迹**：Elk 迁徙路线绕开“执念”区，形成自然路径；Drone 残骸指向锻父最后的尝试。
- **光的情绪**：Lumen 强度与 NPC 情绪绑定——锻父区光硬且刺眼（愤怒），孩子区光冷且散（孤独），森林区光斑驳且重影（记忆过载）。玩家拖光即在调节情绪。
- **可读物**：村民日记本（Substrate 纸张，Nanite 字迹清晰）、织机边的半成品（Chaos Cloth 未完成编织垂落）。

## NPC 设计 (MetaHuman 应用，记忆/情感)

| NPC | MetaHuman 特征 | 记忆系统 | 情感反应 |
|-----|----------------|----------|----------|
| 线灵 (伴侣) | 少女，ControlRig 面部 52 blendshape，织线发光瞳孔 | 记住玩家每个编织的稳定性，夸奖/吐槽 | 随 GlobalWeaveStability 改变语调（MetaSounds 变调） |
| 锻父 | 老者，皱纹 Nanite 位移，声音嘶哑 | 固执阶段拒绝寒线对话；被“雪入炉”后记忆解锁新台词 | 眼神从硬盯→柔和（ControlRig 视线目标从火→雪） |
| 孩子 | 7 岁，MetaHuman 孩童比例，大眼睛 | 等待时反复说“妈妈说春天会来”；花开后说“原来春天是我种的” | 拥抱动画用 MotionWarping 适配玩家身高 |
| 森林 | 非人，Niagara 拟人光团 + 村民集体低语 | 记住全服玩家的编织次数，过载时低语加速 | 玩家带入“白”后，低语变鸟鸣（MetaSounds crossfade） |

- **技术**：StateTree 驱动 NPC 日常（锻父打铁、孩子堆雪人），SmartObject 让 NPC 对新编织的温泉/桥产生“使用”行为（泡澡/过桥），增强世界活感。
""")

w("03_GameplaySystems.md", r"""
# 核心玩法系统

## 核心循环图 (Input → Process → Feedback → Growth)

```
[Input] Weave/Anchor/Interact (3键)
   ↓
[Process] Chaos Field 撕裂 → Lumen 光/物质属性计算 → 稳定性 S 评估
   ↓
[Feedback] 视觉: Substrate 缝/ Niagara 火花 / Lumen GI 变化
           听觉: MetaSounds 张力音高 + Quartz 节拍
           触觉: DualSense 扳机阻力 + 屏幕织线绷紧
           世界: 地形/水/植被持久改变 + MassAI 改道
   ↓
[Growth] 解锁 Pattern → 工坊创作 → 市集分享 → 线币 → 新能力 (更远/更稳/新纹)
   ↓ loop (每 5 分钟)
```

## 主要系统交互图

```
Weaving (撕拖缝) ─┬─> World (World Partition 持久化 + HLOD 更新)
                  ├─> Physics (Chaos 破坏/布料) ─> Niagara
                  ├─> Dimension (Lumen GI 权重, Nanite LOD bias)
                  └─> Audio (MetaSounds Stability/BiomeBlend)

MassAI ─────────┬─> World (迁徙受地形/光影响)
                └─> Narrative (NPC 对编织的反应)

Loom Workshop ──> Weaving (Pattern 改变缝的外观/稳定性加成)
      ↑                ↓
  Economy (线币/市集) ←─┘
```

## 涌现式设计 (简单规则 → 复杂结果)

**规则 1：物质守恒 + 属性继承**
- 热 (Obsidian) + 冷 (Frostvein) = 蒸汽 (新雾 Niagara + 温暖区)
- 热 + 生 (Canopy) = 焦藤 (可燃藤，Mass sprite 避开)
- 冷 + 光 = 折射 (冰棱镜改变 Lumen 方向)
- 生 + 光 = 繁茂 (种子在光下生长速度 ×3)

**涌现案例**
- 玩家把岩浆瀑布拖进 Canopy 瀑布 → 蒸汽 + 焦藤 + 新光路，三者又影响 Elk 迁徙（Elk 怕热但喜光，路径呈 S 形）。官方未设计此 S 形迁徙，是规则自然产生。
- 4 人把 Frostvein 极光 + Obsidian 火光 + Canopy 荧光同时缝进一洞 → 产生“星空” Substrate（四色 GI 叠加 + 噪点），成为社区新摄影 meta。

**稳定性经济**
- 每条裂缝有预算 `B = base + 锚点*0.3 + PatternBonus`。拖大块地形耗 B，B 不足则裂缝回弹。逼玩家权衡：是一次搬大山，还是分多次搬小石。

## 难度与进度曲线

| 阶段 | 失败率 | 安全网 | 挑战 |
|------|--------|--------|------|
| 0-2h | <5% | 线灵示意角度、允许 3 次回退 | 无 |
| 2-10h | 15% | 超时降低 S 要求 30% | 角度/速度评分 (影响 Pattern 解锁) |
| 10-20h | 25% | 可呼叫 AI 线灵补位锚点 | 限时 Daily Rift |
| 20h+ | 40% (可选) | 无，但可重试无惩罚 | 速通榜、摄影赛、无锚点挑战 |

- **死亡**：无血条。跌落/岩浆 → 线拉回 (1.5s)，仅损失 2% 稳定性。
- **成长**：MasteryLevel 0-100，每 10 级解锁新 Pattern 槽 + 更远 WeaveReach (2.5km → 4km)。
""")

w("04_TechImplementation.md", r"""
# UE5 技术实现方案 (Technical Deep Dive)

## Nanite 策略

| 资产 | Nanite? | 原因 | LOD/HLOD |
|------|---------|------|----------|
| 岩石/悬崖/冰壁/树干 | 是 | 撕裂需像素级纤维，Nanite 保持 10B 三角无 pop | Nanite 自动 + HLOD cluster 256 instances → 1 mesh |
| 树叶/草/藤叶 | 否 | 需 WPO 风动，Nanite 不支持 WPO | 传统 LOD 4 级 + Impostor |
| 角色 (Weaver) | 否 | 蒙皮网格，Chaos Cloth | 4 LOD, 2k→40k tris |
| 裂缝碎屑 (GC) | 是 (Nanite GC) | 破坏后碎块仍需高细节 | Chaos GC + Nanite |
| 建筑废墟 | 是 | 可破坏 | HLOD 3 级 |

- **设置**：`r.Nanite.MaxPixelsPerEdge=1` (PC), `=2` (Console)。`r.Nanite.AllowTessellation=1` 用于纤维位移。
- **验证**：`stat nanite` 目标 <12ms (PC), <16ms (Console)。

## Lumen 光照设计 (氛围 + 玩法)

- **全局**：`r.DynamicGlobalIlluminationMethod=1` (Lumen), `r.ReflectionMethod=1`, `r.Lumen.HardwareRayTracing=1` (PC), SWRT 回退 (Console)。
- **玩法杠杆**：
  - 每生态主光是可拖的：Obsidian (Emissive 20000 lux 橙), Frostvein (Aurora 5000 lux 青), Canopy (Biolum 8000 lux 绿)。
  - `UDimensionManager` 权重驱动 `PostProcessVolume` 的 `LumenSceneLighting` 与 `VolumetricFog`：权重 0→1 时，GI 在 0.5s 内插值，玩家可见光色在裂缝间“流动”。
  - 谜题：Frostvein 冰棱镜关卡——拖 Obsidian 光进洞，Lumen 反射经棱镜聚焦到种子，种子生长。光路用 `Lumen.Visualize` 调试。
- **性能**：`r.Lumen.ScreenProbeGather.DownsampleFactor=16`, `r.Lumen.TranslucencyVolume=1` (雾)。

## Chaos 物理应用

| 模块 | 用途 | 玩法层 |
|------|------|--------|
| **Chaos Destruction (GeometryCollection)** | 撕裂墙/地/冰 | 核心：撕开即破坏，碎块可再拖 |
| **Chaos Cloth** | 织者斗篷、裂缝纤维条、藤蔓 | 视觉 + 轻玩法：风影响藤摆，拖动改变布张力 |
| **Chaos Flesh** | 锻父记忆回闪的软体 (可选) | 叙事：回忆中面团柔软 vs 现实僵硬 |
| **Field System** | Tear/Stitch/Anchor 三场 | 驱动破坏的力场，`AWeaveFieldSystem` 生成 |

- **解算**：`ChaosSolver` 异步，`SolverThreadPoolSize=4`，`MaxSubsteps=6`。
- **优化**：GC 集群 >50 碎块时合并为 HLOD 碎块，场半径 <5m 时不产生新 GC。

## Control Rig + Motion Warping

- **ControlRig**：`CR_Weaver_Face` (52 BS), `CR_Weaver_Body` (IK 手脚)。面部用 MetaHuman Rig，身体用 FullBodyIK。
- **MotionWarping**：
  - `Warp_WeaveReach`：Weave 目标点远时，自动 warp 手臂伸展 + 脚步前踏，保持不滑步。
  - `Warp_AnchorBrace`：锚定时，warp 到最近可支撑点（墙/地面），播放“撑住” pose。
- **验证**：`showdebug motionwarping`。

## MassAI + StateTree

- **规模**：3k 实体 (Elk 2000, Drone 500, Sprite 500)。`MassEntity` + `StateTree` + `SmartObject`.
- **Elk**：StateTree `ST_ElkHerd` — `Graze → Migrate → Panic (broadcast) → Flee`。Panic 用 `MassSignal` 传播，范围 30m，衰减 0.9。
- **Drone**：`ST_DronePatrol` — 巡逻 → 检测编织 → 围观 (SmartObject `SO_WatchWeave`)。
- **性能**：`r.Mass.TickInterval=0.033` (30Hz), `MassProcessor` 分 4 桶，`stat mass` <3ms。远处 >120m 进入 dormancy (ReplicationGraph 控制)。
- **Emergence**：Elk 避热/趋光，Drone 趋新奇——玩家编织会自然重路由群体，无需脚本。

## MetaSounds

- **Graph**：`MS_Loom_Base` — Quartz Clock 120 BPM 输入，`Stability` 控制粒状密度，`BiomeBlend` 控制三层滤波，`WeaveTrigger` 触发 whoosh。
- **实现**：`UMetaSoundWeaveController` 持有 `UAudioComponent` (MetaSoundSource)，`SetFloatParameter` 驱动。
- **Reverb**：Lumen 光强度驱动 `AudioVolume` reverb send——亮处混响短，洞内长。

## World Partition 大世界

- **大小**：16 km² (4×4 km)，3 DataLayers (DL_Obsidian/Frostvein/Canopy) + 1 Shared (神殿)。
- **分区**：`WorldPartitionRuntimeSpatialHash`, `CellSize=32000`, `LoadingRange=64000` (64m)。`HLOD` 3 级，`WP_HLOD_Builder` 每 128m 簇。
- **填充密度**：PCG 每 km² 4000 裂缝实例 + 800 植被簇 + 12 POI。`POIManager` 按兴趣度排序流送。
- **持久化**：编织改变写入 `WorldPartition` 的 `DataLayerInstance` 存档 (SaveGame + `WorldPartition` `RuntimeHash` 增量)。异步幽灵 via `Iris` 稀疏同步 (每 30s 批处理)。

## 网络架构 (ReplicationGraph + Iris, 4 Coop + 50 Plaza)

- **模式**：Dedicated Server (Shipping) + Listen Server (Dev)。`Iris` 作为 `GameNetDriver`。
- **ReplicationGraph**：
  - `AlwaysRelevant`：锚定玩家、RiftVolume、RiftPuzzleActor。
  - `Spatial`：MassAI (120m dormancy), Niagara (80m cull), 编织碎块 (50m)。
  - `Dormancy`：远处 Elk 进入 `Dormant`，重进入时插值。
- **Iris**：`bUseAdaptiveNetUpdateFrequency=true`，Weave 操作 `Server RPC` 聚合 (每 0.05s 合并 `Server_UpdateDrag`)。
- **Voice**：EOS Voice (队伍) + 文本轮盘 (无 mic 友好)。
- **Anti-cheat**：服务器校验 `EvaluateStability` (WeavingPatternEvaluator) + 最大拖动距离 (4km) + 速率限制 (10 RPC/s)。无竞技，无需强反作弊。

## 跨平台 + 优化

| 目标 | 分辨率 | 帧率 | 关键降质 |
|------|--------|------|----------|
| PC Ultra | 4K | 60 | Nanite 1px, Lumen HWRT, Mass 3000 |
| PC High | 1440p | 60 | Nanite 1px, HWRT |
| PS5 Perf | Dynamic 4K | 60 | Nanite 2px, SWRT, Mass 1500 |
| XSX | 同 PS5 | 60 | 同 PS5 |
| XSS | 1440p | 30 | Nanite 2px, SWRT, Mass 800 |

- **Input**：EnhancedInput + CommonUI，DualSense 自适应扳机 (撕裂张力 0-100% 阻力)。
- **内存**：Streaming Pool 4000 MB, VT Pool 2×。
""")

w("05_ArtAudio.md", r"""
# 美术与视听方向

## 整体美术风格

**关键词：织物现实主义 (Woven Realism) + 光学奇幻**
- **Reference**：吉卜力《幽灵公主》森林 + 《死亡搁浅》地貌 + 《纪念碑谷》几何 + 现实织物微距摄影。
- **原则**：近看是布料纤维（Nanite 微观），远看是壮丽地貌（Lumen 大气）。材质像布：岩石有织纹，冰有经纬，藤是编绳。
- **比例**：角色 1:7.5 头身，亲切非超写实（面向大众），但 MetaHuman 面部保持真实情感。

## 色彩设计

| 场景 | 主色 | 情绪色 | UI 色 |
|------|------|--------|-------|
| Obsidian Forge | 墨黑 #0A0A0F + 熔岩橙 #FF4D00 | 愤怒/固执 — 高对比硬光 | 橙 #FF6B2E |
| Frostvein | 霜白 #F0F8FF + 极光青 #00E5FF | 孤独/等待 — 冷扩散光 | 青 #7DF9FF |
| Canopy | 夜绿 #0B1A12 + 荧光绿 #1BFF8A | 记忆过载 — 斑驳重影 | 绿 #1BFF8A |
| 缝合区 | 三色混合 + Substrate 星点 | 希望 — 三色 GI 融合 | 织金 #E8D9B8 (缝线) |

- **UI**：低饱和织物底 + 高饱和缝线强调 (Substrate 缝发光 2.0 emissive)。

## 角色设计原则 (面向大众)

- **Weaver**：中性，可自定义 (MetaHuman 4 预设：少年/少女/中年/长者)，斗篷 Chaos Cloth 随编织飘动，手套有发光针。
- **NPC**：锻父 (壮实老者，手烫伤疤 Nanite 位移)，孩子 (圆脸大眼)，线灵 (半透明发光，Niagara 发丝)。
- **可读性**：剪影清晰，远处 MassAI 也能分辨（Elk 角发光，Drone 红眼）。

## 音频设计 (MetaSounds 动态)

| 层 | 内容 | 驱动 |
|----|------|------|
| **Bed** | 三生态底噪 (炉火/风雪/虫鸣) | BiomeBlend 权重 crossfade |
| **Weave** | 撕裂布帛 + 嗡鸣 + 缝合叮 | DragSpeed + AngleError + Stability |
| **Music** | 三主题 (锻锤/冰铃/藤笛) 在 Quartz 上对位 | 玩家位置与编织进度 (Stability → 和声丰满度) |
| **Feedback** | 锚定“咔嗒” + 完成“织机咔哒合拍” | 事件触发 (OnWeaveCompleted) |

- **无静态 BGM**：所有音乐是 MetaSounds 实时作曲，玩家静止时稀疏，玩家编织时丰满。
- **无障碍**：全对白字幕 + 方向性字幕 (震动提示编织方向)。

## Niagara 特效

- **WeaveTear**：布纤维撕开 + 纤维光丝 (Substrate emissive)。
- **StitchWeld**：焊点星火，Stability 越高星火越密。
- **BiomeBlendFog**：三色雾随权重流动，像染色。
- **PhotoConfetti**：快门时 2s 织线彩带。

## 灯光

- Lumen 为主，无烘焙。`PostProcess` 体积每生态一个，权重由 `DimensionManager` 驱动。
- 关键帧：日夜循环 45 分钟，黄昏时三生态光同时出现，缝合区最美——鼓励黄昏摄影。
""")

w("06_WorldLevelDesign.md", r"""
# 关卡/世界设计

## 3 个核心生态/区域设计

### 1. Obsidian Forge (燃线) — 垂直·热·破坏
- **视觉**：阶梯火山，黑曜石锋利，熔岩河像织线流动。WPO 熔岩波。
- **玩法**：Chaos 破坏——用锤破壳、用裂缝引流。热是资源：把热拖到 Frostvein 可化雪，拖到 Canopy 会焦藤需控制。
- **叙事**：锻父守炉，环境是未完成的锻件（半熔的剑、冷却的模）。POI：Crucible (大型 4 人搬运熔岩)、Towers (摄影 VISTA)、Echoes (锻父独白，随编织解锁)。

### 2. Frostvein Tundra (寒线) — 水平·冷·光学
- **视觉**：白茫茫地平线 + 青色冰洞星空。风雪 Niagara + 远处 Elk 群 Mass。
- **玩法**：Lumen 光学——冰棱镜折射、手电聚焦。冷是资源：把寒带进 Forge 可淬火，带进 Canopy 可保鲜种子。
- **叙事**：孩子堆雪人等春。POI：Harp (冰晶琴，MetaSounds 演奏)、Shrine (孩子记忆)、Trail (Elk 迁徙摄影)。

### 3. Luminous Canopy (生线) — 密林·生·生长
- **视觉**：巨树如柱，荧光孢子如雪，藤蔓可生长 (Niagara + Chaos Cloth)。
- **玩法**：生长——用光和水让藤蔓实时长成桥。需管理过度生长（藤会堵路）。
- **叙事**：森林记得太多，低语过载。POI：Memory Hollow (低语迷宫)、Bloom (巨花，4 人编织开花)、Nets (藤网平台谜题)。

## 开放世界填充策略 (如何避免“大而空”)

- **密度**：每 200m 一个微谜题 (30s)，每 500m 一个 POI (5 min)，每 1km 一个大型编织 (15 min)。PCG 保证野外不空：裂缝、植被、Mass 群始终在视野内。
- **兴趣驱动**：`POIManager` 按“好奇心”排序——未见过的混搭 (如未试过 热+生) 会高亮为金色裂缝，引导尝试。
- **异步幽灵**：即使单人，也能看到他人编织的幽灵痕迹——世界永远有“人味”。

## 兴趣点 (POI) 设计原则

1. **可见性**：3 个生态的最高点彼此可见 (Nanite 远景)，POI 有独特天际线 (锻炉烟/冰洞光柱/巨花荧光)。
2. **可达性**：无“跑图惩罚”——Weave 可作位移 (撕开捷径)，锚点可作抓钩 (MotionWarping 吸附)。
3. **回报**：每个 POI 给 Pattern 碎片 + 摄影构图奖励 + 一段环境叙事 (日记/回声)。
4. **社交**：大型 POI 需 2-4 人，入口有“等待锚点”提示，路过玩家自然协作。

## 导航设计

- **不迷路**：主线织机光柱在天空可见 (Volumetric Fog 光柱)，小地图是织物纹理 (经纬线 = 等高线)。
- **奖励探索**：偏离主线 100m 即有 PCG 微裂缝，内有 Pattern；金色裂缝 (未尝试混搭) 有额外线币。
- **无小地图依赖**：Lumen 光色本身指路——橙光方向是 Forge，青光是 Frostvein，绿光是 Canopy。
""")

w("07_UIUX.md", r"""
# UI/UX 设计

## HUD 设计 (极简 vs 信息丰富)

- **原则**：极简常驻，丰富按需。
- **常驻** (左下)：
  - 稳定性环 (180°，0-100%，织线纹理，Stability 驱动)
  - 锚点 pips (1-4 点，空心→实心→发光)
- **按需**：
  - 拖动时：张力条 (DualSense 同步)
  - 解谜时：Pattern 提示 (3s 后淡出)
- **无**：血条、小地图数字、任务列表常驻——按 Tab 展开。

## 菜单/背包/地图

- **织纹背包**：不是格子，是织机梭子陈列 (3D 预览 Substrate 缝)，可旋转查看。
- **地图**：织物地图 (World Partition 缩略)，已编织的裂缝发光，幽灵痕迹半透明。可筛“我的编织/好友/全服”。
- **设置**：EnhancedInput 重映射可视化 (按住 Weave 时显示当前绑定)。

## 新手引导 (无文字教学)

- **环境引导**：布墙、发光幼苗、藤蔓柱——颜色与形状暗示交互。
- **幽灵示范**：第一个复杂谜题前必有幽灵录像。
- **线灵轻推**：超时 20s，线灵做一次慢动作示范 (不文字)。
- **触觉引导**：手柄震动方向 = 正确拖动方向。

## 无障碍设计

| 需求 | 方案 |
|------|------|
| 色盲 | 三生态除颜色外有形状区分 (Forge 尖锐、Tundra 圆润、Canopy 有机)；织线高对比模式 (黄/紫) |
| 单手操作 | 单摇杆模式：Weave 与视角合并，长按切换；锚点自动吸附 |
| 认知负荷 | 每屏最多 3 个信息元素；教程可回放 (神殿织机) |
| 听觉 | 全对白字幕 + 视觉化音源 (声波圈) |
| 晕动 | FOV 90 固定，Weave 拖动时 FOV 不变 (防晕)，可选黑边缩窄 |

## Photo Mode

- 一键 (P/Share) 进入，时间慢 0.3×，UI 隐藏，Rule-of-thirds 网格 + 织纹水印。
- 自动构图：Lumen 曝光自动适配缝合区三色，防止过曝。
- 分享：F12 直接带话题 #RiftWeave 到剪贴板。
""")

w("08_MultiplayerSocial.md", r"""
# 多人/社交系统

## 网络同步策略

- **Authority**：Dedicated Server 权威 (Weave 稳定性、谜题解算、World Partition 持久化)。
- **RPC 聚合**：`Server_UpdateDrag` 每 0.05s 聚合一次，减少 80% 包。
- **Iris**：自适应频率——Weaving 时 30Hz，闲置 10Hz。`UWeaveComponent` 的 `Stability` 用 `ReplicatedUsing` 插值。
- **MassAI**：仅同步首领 Elk，其余客户端预测 (StateTree 相同种子)。

## 合作机制设计

| 机制 | 人数 | 规则 |
|------|------|------|
| 锚点 | 1-4 | 每多一锚点 +0.3 B，角度误差 <15° 才满分 |
| 耦合物理 | 2-4 | 桥/河/藤的物理张力由所有锚点平均拉力决定 |
| 复活 | - | 跌落 → 队友 2s 内 Interact 拉回 (参考双人成行)，无惩罚 |
| 语音 | - | EOS Voice 队伍 + 轮盘表情 (无 mic 也可) |

## 异步社交 (死亡搁浅式共享世界)

- **幽灵层**：你的编织以 DataLayer 幽灵 (低 HLOD) 存于 `Iris` 的 `SparseReplication`，他人世界每 30s 拉取前 20 个高赞幽灵。
- **点亮**：他人可 Interact 点亮你的幽灵，你收线币 + 通知 (MetaHuman 感谢信)。
- **市集**：Plaza (50 人) 展示全服 Top10 编织 (投票)，可进入其原始坐标参观 (传送)。
- **反悲伤**：幽灵不可破坏他人谜题，仅装饰层；举报 → 隐藏。

## 反作弊 (如竞技元素)

- 无 PvP 竞技，仅合作 + 速通榜。
- 速通榜：服务器重放校验 (Weave 路径 + 时间)，异常 (WeaveReach >4km) 标记人工审核。
- 经济：线币仅外观，不可交易为现实货币，无 Pay-to-Win 诱因。
""")

w("09_PipelineAndTools.md", r"""
# 内容生产管线

## 关卡设计工具 (UE5 内置 + 自定义)

| 工具 | 用途 |
|------|------|
| **World Partition + DataLayers** | 3 生态分区，DataLayer 驱动维度权重 |
| **PCG (RiftCracks, Foliage)** | 程序化裂缝/植被，美术可刷参数 |
| **自定义 Editor Plugin: RiftWeaveWeavingSystem** | 可视化 WeaveField 预览 (editor 中拖动看 Chaos 场) |
| **MassAI Debugger** | `MassDebugger` + `StateTree` 可视化迁徙 |
| **Lumen Visualize** | 光路调试 |

## 资产生产流程

```
Quixel Megascans → Bridge → UE (Nanite on/off 按表) → Master Material (Substrate)
MetaHuman → MH Assembly → ControlRig → IK Retargeter → BP_Weaver
Houdini (裂缝) → FBX → Chaos GC → Nanite GC
Niagara (VFX) ← Substance (织纹) ← Pattern DataAsset
```

- **Nanite 策略**：导入时 `Build Nanite = true` (岩石)，`false` (植被/角色)。
- **验证**：`Tools/AssetPipeline/validate_assets.py --all` 检查 Nanite/LOD/材质/命名。

## 自动化测试

| 测试 | 频率 | 工具 |
|------|------|------|
| 性能 (stat unit, nanite, mass) | 每提交 (CI) | `Scripts/PerfTest.ps1` + Gauntlet |
| 兼容 (PS5/XSX) | 每日 | Unreal Automation + Test_Mass_2000 |
| 资产校验 | 每提交 | `validate_assets.py` |
| 网络 (4 人编织) | 每周 | Gauntlet 4-client 同步测试 |

## 本地化策略

- **文本**：`LOCTEXT` + `Localization Dashboard` (中英日)。
- **文化**：锻父/孩子故事本地化配音 (MetaHuman Lipsync)，织纹命名保留“织”意象 (英 Weave 保留)。
- **字体**：Noto Sans SC + 自定义织纹图标字体。
""")

w("10_ProductionPlan.md", r"""
# 开发规划 (2-3 年, 30-50 人)

## Pre-production (6 个月) — 原型验证

| 月 | 目标 | 交付 |
|----|------|------|
| 1-2 | 技术验证：Nanite 撕裂 + Chaos 场 + Lumen 拖光在 WP 小块可行 | 可玩灰盒：1 墙 1 熔岩 1 雪 |
| 3-4 | 垂直切片：Obsidian 一个谜题，2 人锚点，1 个 Pattern | 15 分钟切片 (含 Photo) |
| 5-6 | 美术垂直 + Mass 500 + MetaSounds 原型 | 目标画质截图 + 性能基线 |

- **团队**：12 人 (3 程序 3 美术 2 设计 2 音频 1 制作 1 QA)。

## Production Year 1 (12 个月) — 核心系统 + 前 30% 内容

- **Q1**：WeaveComponent + DimensionManager + Chaos Field 定版；BiomeManager + DataLayers；EnhancedInput
- **Q2**：Obsidian Forge 完整 (8 POI + Crucible 大型编织)；Frostvein 灰盒
- **Q3**：Frostvein 完整；MassAI 2000；StateTree 迁徙；ReplicationGraph + Iris 4 人
- **Q4**：Loom Workshop + 市集幽灵 + Photo Mode；第一次封闭试玩 (单人生态内)

## Production Year 2 (12 个月) — 剩余内容 + Polish + 优化

- **Q1**：Luminous Canopy 完整；全 3 生态缝合演出 (4 人 16km²)；HLOD 定版
- **Q2**：主线 12 节点定版；MetaHuman 演出；Niagara/MetaSounds 终版
- **Q3**：PS5/XSX 移植 + 优化 (Nanite 2px, SWRT)；DualSense 适配；无障碍
- **Q4**：Beta (500 人) → Polish (性能、Bug、本地化) → Cert (Sony/MS) → Gold

## Launch + Live Ops (Year 3+)

| 周期 | 内容 | 运营 |
|------|------|------|
| S0 Launch | 29.99 买断，3 心主线 | 首周摄影赛 + 主播活动 |
| S1 (3 月) | 新 Pattern 包“机械织” + Daily Rift 扩展 | Creator Fund 1st payout |
| S2 (6 月) | 新 POI 2 个/生态 + 新 Mass 物种 | 市集 Top 作品实体周边 |
| S3+ | 赛季主题 (如“雨织”)，UGC 工具开放 (PCG 图编辑器) | Discord/Reddit/微博/B站 社区赛 |

- **团队 Live**：15 人 (5 内容 4 工程 3 社区 3 QA)。

## 风险与缓解

| 风险 | 缓解 |
|------|------|
| Chaos 性能爆 | GC 合并 + 场半径限制 + LOD |
| Lumen 跨维度穿帮 | DataLayer 权重平滑 + 雾过渡 |
| 4 人物理不同步 | Iris 聚合 + 服务器权威 + 插值 |
| 内容量大 (20h+100h) | PCG + 异步 UGC 填补 |
""")

w("11_BusinessAndLiveOps.md", r"""
# 商业化与运营

## 定价策略

- **Buy-to-Play**：29.99 USD / 98 CNY (Steam/Epic/PS5/XSX)。首月 20% off。
- **Edition**：Standard (本体) + Weaver's Loom Edition (+ 3 独占 Pattern + 数字画集, 39.99)。
- **无 F2P 陷阱**：无体力、无抽卡、无数值。

## 赛季/DLC 内容规划

| 赛季 | 主题 | 免费 | 付费 (9.99 Pass) |
|------|------|------|------------------|
| S1 | 机械织 | 2 Pattern + 1 POI | 抢先 3 Pattern + 机械斗篷 |
| S2 | 雨织 | 雨物理 + 新 Niagara | 雨织伞 + 家园雨棚 |
| S3 | 星织 | 星空 Substrate | 星纹 + 摄影滤镜 |

- **DLC**：大型生态扩展 (如“深渊织”) 单独售卖 14.99，含 5h 主线。

## 社区运营

| 平台 | 定位 | 活动 |
|------|------|------|
| Discord | 核心玩家 + UGC | 每周编织挑战 + 工坊投票 |
| Reddit r/RiftWeave | 海外 | Meme 切片 + 速通榜 |
| 微博/B站 | 国内 | 摄影赛 + 主播共创 (提供 Photo Mode 绿幕) |
| X/TikTok | 病毒 | #RiftWeave 话题，官方转发最离谱温泉 |

## UGC 生态 (官方工具)

- **Loom Workshop**：游戏内可视化 Pattern 编辑器 (Substrate 图层 + Niagara 强度 + 稳定性加成)，一键上架市集。
- **PCG 图**：高级玩家可导出 PCG RiftCracks 图，分享给官方收录。
- **激励**：Creator Fund — 每赛季按订阅/点亮分成 (50% 流水)，Top10 获实体奖。
- **审核**：自动 (NSFW/性能) + 人工 (举报)，幽灵层不影响主线。

## 直播友好设计

- **戏剧性**：4 人桥塌切片、星空温泉诞生、Mass 迁徙改道——每 10 分钟一个切片点。
- **视觉**：Lumen 三色融合在缩略图中极辨识，封面点击率高。
- **互动**：Twitch 扩展“帮主播选 Pattern” (观众投票影响下一 Pattern 推荐)。
- **无剧透**：主线记忆可设“主播模式” (隐藏关键台词，仅表现编织)。

## 数据与迭代

- **埋点**：编织稳定性分布、混搭组合热度、POI 停留、幽灵点亮率。
- **迭代**：热度低的混搭在赛季中加强 (如提升 稳定性加成)，冷门 POI 加摄影奖励。
""")

# Extra index
w("README.md", r"""
# Documentation Index — RIFTWEAVE

| # | 文档 | 内容 |
|---|------|------|
| 00 | Phase0_ExperienceValidation | 五问验证 (首因/社交/创造/新鲜感/非玩家) |
| 01 | GameProposal | 提案 (名称/定位/反直觉/UE5 杠杆) |
| 02 | WorldAndNarrative | 世界观 + 12 节点主线 + 环境叙事 + MetaHuman |
| 03 | GameplaySystems | 核心循环 + 涌现 + 难度曲线 |
| 04 | TechImplementation | Nanite/Lumen/Chaos/Mass/MetaSounds/WP/Iris |
| 05 | ArtAudio | 美术风格 + 色彩 + Niagara + 灯光 |
| 06 | WorldLevelDesign | 3 生态 + 填充 + POI + 导航 |
| 07 | UIUX | HUD + 地图 + 无文字引导 + 无障碍 |
| 08 | MultiplayerSocial | ReplicationGraph/Iris + 4 人 + 异步幽灵 |
| 09 | PipelineAndTools | 关卡工具 + 资产流 + 自动化测试 |
| 10 | ProductionPlan | 2-3 年排期 + 风险 |
| 11 | BusinessAndLiveOps | 定价 + 赛季 + 社区 + UGC |

> 引擎外可读：无需 UE，纯 Markdown 即可评审完整 GDD。
""")

print("docs done")
