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
