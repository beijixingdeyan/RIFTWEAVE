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

## 人员配比 (30-50 人峰值)

- 工程 10 (Gameplay 3, Tech 3, 网络 2, 工具 2)
- 美术 15 (环境 6, 角色 3, VFX 2, 动画 2, UI 2)
- 设计 8 (关卡 4, 系统 2, 叙事 2)
- 音频 3
- 制作/QA/社区 8

## 里程碑可玩标准 (Playable Criteria)

- M1 (6月): 1 墙可撕，1 拖 1 缝，S 计算正确。
- M2 (12月): Obsidian 可通关，2 人，3 Pattern。
- M3 (18月): 3 生态缝合演出完整，Photo + Workshop。
- Beta (24月): 全主线 + 50 POI + 性能达标。

## 外包

- Quixel 扫描 (岩石/植被) 外包 30%，内部 Nanite 处理。
- MetaHuman 定制 (锻父/孩子) 外包面部扫描，内部 ControlRig。
