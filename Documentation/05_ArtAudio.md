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

## 材质体系 (Substrate)

Master Material `M_WeaveMaster` (Substrate):
- 层 0: 基岩/冰/树皮 (Nanite 位移)
- 层 1: 缝线 (emissive, 缝合时 0→1 lerp)
- 层 2: 覆盖 (雪/灰/苔, RVT 混合)
- 参数：`SeamProgress`, `WeavePatternID`, `BiomeBlend`

- **优化**：Substrate slab 3 层以内，`r.Substrate=1`。

## 概念艺术板 (Art Boards)

- **Obsidian**: 关键词 锋利/炽热/未完成。Ref: 《风之谷》腐海工厂 + 冰岛火山。
- **Frostvein**: 关键词 空旷/等待/星光。Ref: 《死亡搁浅》雪原 + 挪威极光。
- **Canopy**: 关键词 繁茂/记忆/呼吸。Ref: 吉卜力 + 《湮灭》闪光。

## 音频实现细节

- **Quartz**：`QuartzSubsystem` 120 BPM，Weave 操作量化到 1/8 拍，保证音乐与操作同频。
- **Dynamic Mix**：Weaving 时 duck 底噪 -3dB，突出缝合叮。
- **Voice**：MetaHuman + `Audio2Face` (可选) 驱动唇形，StateTree 控制对话触发 (靠近 POI 3m)。
