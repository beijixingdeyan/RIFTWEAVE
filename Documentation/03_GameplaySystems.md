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
