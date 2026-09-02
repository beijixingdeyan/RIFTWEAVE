import pathlib
base = pathlib.Path(r"E:\github\dsh\projects\helloworld -unrealengine\Documentation")

# Append expansions to make docs large and excellent

expansions = {
"03_GameplaySystems.md": r"""

## 数值细化

### 稳定性公式 (Stability)
```
S = clamp( 1.0 - (dragSpeed/2500)*0.4 - (angleError/90)*0.3 + anchors*0.12 + patternBonus, 0, 1.2 )
```
- dragSpeed: 每帧拖动距离，2500 = 最大惩罚
- angleError: 拖动向量与裂缝法线夹角，90°=最大惩罚
- anchors: 0-4，每锚点 +0.12
- patternBonus: 0.05-0.15 (LoomPattern.StabilityBonus)

反馈：
- S<0.4: 裂缝闪红、MetaSounds 低沉嗡鸣、Chaos 碎屑大量掉落
- S 0.4-0.7: 黄光、提示“需要锚点”
- S>0.85: 绿光 + 缝线发光 + 完成时彩带

### 经济
- 线币 (Thread): 仅外观。可通过编织 (S>0.8)、摄影赛、异步点亮获得。不可购买。
- Pattern 解锁：S>0.9 的编织有 30% 掉落新 Pattern 碎片 (3 碎片合成)。

## 涌现示例库 (Emergence Catalog, 设计时用)

| 组合 | 结果 | MassAI 影响 | 摄影价值 |
|------|------|-------------|----------|
| 熔岩 + 雪 | 温泉 (蒸汽雾 + 热水材质) | Elk 聚集取暖 | 高 (暖雾人像) |
| 熔岩 + 藤 | 焦藤 (黑化藤，可燃) | Sprite 避开 | 中 (对比) |
| 极光 + 冰 | 棱镜光路 | 无 | 极高 (光绘) |
| 荧光 + 雪 | 发光雪 (夜光) | Drone 趋光 | 高 |
| 四重混合 | 星空温泉 | 全部聚集 | 爆款 |

### 碎片化叙事触发
- 每个涌现首次出现时，线灵会低语一句环境叙事 (如首次造温泉：“暖意让记忆解冻”)，强化学习。

## 可访问性进阶

- **色盲模拟**：Editor 工具 `ColorBlindPreview` (CommonUI) 预览 3 种色盲下的裂缝可读性。
- **输入重映射**：所有 5 动作可重绑，支持单手 (左摇杆 = 移动+视角合并，长按 Weave 切换)。
""",
"05_ArtAudio.md": r"""

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
""",
"06_WorldLevelDesign.md": r"""

## POI 列表 (精选 12)

| POI | 生态 | 人数 | 核心玩法 | 叙事 |
|-----|------|------|----------|------|
| Crucible | Obsidian | 4 | 搬运熔岩河 | 锻父的炉 |
| Harp | Frostvein | 1 | 冰棱镜调音 | 孩子的摇篮曲 |
| Bloom | Canopy | 4 | 藤蔓开花 | 森林的第一次遗忘 |
| Towers | Obsidian | 1 | 摄影 VISTA | 眺望三生态 |
| Trail | Frostvein | 2 | Elk 迁徙护送 | 等待的脚印 |
| Hollow | Canopy | 2 | 低语迷宫 | 记忆过载 |

## World Partition 调试

- `wp.Runtime.ToggleDrawRuntimeHash` 看 Cell。
- `r.HLOD 0/1` 切换 HLOD。
- 目标：`stat unit` <16ms (PS5), `stat streaming` <2ms。

## 引导动线

- 主线：神殿 → Obsidian (北) → Frostvein (东) → Canopy (南) 顺时针，避免往返。
- 支线：POI 间有 PCG 小裂缝串联，像露珠链，鼓励偏航 50-100m。
""",
"07_UIUX.md": r"""

## 详细线框 (Wireframe Notes)

- **HUD 稳定性环**：SVG 环，180°，内径 48px，外径 64px，织纹贴图滚动速度 = Stability*2。
- **锚点 pips**：4 圆点，空心描边 2px，锚定后填充 + 脉冲 (1.2s)。
- **LoomWorkshop**：左侧 PatternGrid (4×10), 右侧 3D 预览 (Substrate 球), 底部参数滑条 (Niagara 强度, 缝宽)。

## 动效

- 缝合完成：HUD 环 0→100% 快充 + 屏幕边缘织线收束 (0.6s, easeOut)。
- 失败：环抖动 (Chaos 噪声) + 织线回弹。

## 本地化 UI

- 中文/英文切换：字长 1.6× 预留，按钮最小 120px 宽。
- 图标化：Weave/Anchor 用针/钉图标，非文字，跨语言。
""",
"08_MultiplayerSocial.md": r"""

## 详细带宽预算

| 通道 | 频率 | 大小 | 备注 |
|------|------|------|------|
| Weave RPC | 20Hz 聚合 | 24 bytes | 位置+法线 |
| Stability | 10Hz | 4 bytes | float |
| Mass (首领) | 10Hz | 16 bytes | pos+vel |
| 幽灵 | 0.03Hz (30s) | 1KB 批 | Top20 |

- 总计 4 人 <40KB/s 上行，符合 Iris 自适应。

## 社交礼仪

- 默认静音，轮盘 8 表情 + 4 快捷 (“来锚点”“看光”“拍照”“谢谢”)。
- 恶意：投票踢 (需 3/4 同意)，幽灵举报 3 次自动隐藏。

## 测试计划

- Gauntlet 4-client 编织同步测试：同一裂缝 4 人同时拖，校验 S 一致 (<0.02 误差)。
- 50 人 Plaza 压力：Mass 800 + 玩家 50，目标 server tick <14ms。
""",
"09_PipelineAndTools.md": r"""

## 命名规范

- `SM_` StaticMesh, `GC_` GeometryCollection, `NS_` Niagara, `MS_` MetaSound, `WBP_` Widget, `BP_` Blueprint, `ST_` StateTree, `PCG_` PCG Graph, `M_` Material, `MI_` Instance, `DL_` DataLayer.

## 提交检查清单 (Checklist)

- [ ] `validate_assets.py` 通过
- [ ] Nanite/ Lumen 可视化无红
- [ ] 无 secrets (`git secrets --scan`)
- [ ] 文档更新 (若改玩法)

## CI 扩展 (未来)

- 自动 Gauntlet：每夜跑 `Test_Mass_2000` + 4 人编织，生成性能报告 (CSV→Grafana)。
""",
"10_ProductionPlan.md": r"""

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
""",
"11_BusinessAndLiveOps.md": r"""

## 数据看板 (Dashboard)

- DAU/WAU, 编织次数, 平均 S, 最热混搭 Top10, 幽灵点亮率, 摄影投稿数, 市集交易。
- 预警：S<0.5 编织 >40% → 难度过高，需加强引导。

## 社区激励细则

- Creator Fund：每赛季流水 20% 注入，按 订阅×点亮 加权分成，Top100 均有奖，Top10 额外实体织机微缩模型。
- 主播：提供 OBS 插件 (Photo Mode 绿幕 + 稳定性覆盖)，方便切片。

## 风险：内容消耗

- 缓解：PCG + UGC 保证每周新裂缝；赛季重置 Daily Rift 种子；老玩家 mentor 新人双倍线币。
"""
}

for fname, add in expansions.items():
    p = base / fname
    if p.exists():
        orig = p.read_text(encoding="utf-8")
        # Append before last line if marker exists, else just append
        new = orig.rstrip() + "\n\n" + add.strip() + "\n"
        p.write_text(new, encoding="utf-8")
        print(f"expanded {fname} -> {len(new.splitlines())} lines")
    else:
        print(f"missing {fname}")

print("expand done")
