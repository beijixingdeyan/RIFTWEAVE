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
