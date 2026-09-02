# 性能与优化 (Performance) — 60 FPS 承诺

## 预算 (16ms @60FPS)
| 系统 | PC Ultra | PS5 Perf | 备注 |
|------|----------|----------|------|
| Nanite | 12ms | 10ms | 1px→2px, 10B tris |
| Lumen | 3ms | 4ms (SWRT) | HWRT→SWRT回退 |
| Mass (3000→1500) | 3ms | 2.5ms | 30Hz, dormancy 120m |
| Chaos | 2ms | 2ms | 异步, 合并>50碎块 |
| Niagara | 1ms | 1ms | 2k粒, cull 50m |
| 总 | <16ms | <16ms | `stat unit` |

## Nanite 策略
- 岩石/悬崖/冰壁/树干：Nanite on，12M→HLOD 256实例/簇
- 植被/角色：Nanite off，传统LOD 4级
- 验证：`stat nanite`，`r.Nanite.MaxPixelsPerEdge 1→2`

## Lumen
- `r.Lumen.HardwareRayTracing 1→0` (PS5 SWRT)
- `r.Lumen.ScreenProbeGather.DownsampleFactor 16`
- 光色驱动谜题，`r.Lumen.Visualize` 调试光路

## MassAI
- `r.Mass.TickInterval 0.033` (30Hz), 分4桶
- `ReplicationGraph` dormancy >120m, `Iris` 自适应 10-30Hz
- `stat mass` <3ms

## Chaos
- `SolverThreadPoolSize 4`, `MaxSubsteps 6`
- 场半径<5m不产新GC，>50碎块合并HLOD
- `p.Chaos.Solver.DebugDraw 0`

## World Partition
- `CellSize 32000`, `LoadingRange 64000`, `HLOD 128m/3级`
- `wp.Runtime.ToggleDrawRuntimeHash` 看Cell，`r.HLOD 0/1` 切换
- 目标 `stat streaming` <2ms

## 自动化
- **CI**：每提交 `validate_assets.py` + Gauntlet `Perf_Mass2000` (16.6ms阈值)
- **Gauntlet**：4-client WeaveSync (stability delta <0.02, server tick <14ms)
- **Profile**：`Unreal Insights` 周期采样

## 设备
| 平台 | 分辨率 | 帧率 | 降质 |
|------|--------|------|------|
| PC Ultra | 4K | 60 | Nanite1px HWRT Mass3000 |
| PS5 Perf | Dynamic4K | 60 | Nanite2px SWRT Mass1500 |
| XSS | 1440p | 30 | Mass800, foliage0.8 |
