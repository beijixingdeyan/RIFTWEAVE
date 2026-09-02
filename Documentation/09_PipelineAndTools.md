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

## 命名规范

- `SM_` StaticMesh, `GC_` GeometryCollection, `NS_` Niagara, `MS_` MetaSound, `WBP_` Widget, `BP_` Blueprint, `ST_` StateTree, `PCG_` PCG Graph, `M_` Material, `MI_` Instance, `DL_` DataLayer.

## 提交检查清单 (Checklist)

- [ ] `validate_assets.py` 通过
- [ ] Nanite/ Lumen 可视化无红
- [ ] 无 secrets (`git secrets --scan`)
- [ ] 文档更新 (若改玩法)

## CI 扩展 (未来)

- 自动 Gauntlet：每夜跑 `Test_Mass_2000` + 4 人编织，生成性能报告 (CSV→Grafana)。
