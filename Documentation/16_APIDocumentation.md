# API 文档 — RiftWeave C++ / BP

## 核心循环
```cpp
// Weave: 撕拖缝，服务器权威
WeaveComp->Server_BeginTear(Start, Normal);
WeaveComp->Server_UpdateDrag(Target); // 0.05s聚合
WeaveComp->Server_EndWeave(End);
// 稳定性
float S = UWeavingPatternEvaluator::EvaluateStability(DragSpeed, AngleError, Anchors);
// 0-1.2，S>0.85发光缝
```

## 维度
```cpp
UDimensionManager* DM = GetWorld()->GetSubsystem<UDimensionManager>();
DM->SetDimensionWeight(EDimensionId::Obsidian, 0.7f);
DM->BlendTo(EDimensionId::Frostvein, 2.f); // 2s插值
```

## Biome
```cpp
UBiomeManager* BM = GetWorld()->GetSubsystem<UBiomeManager>();
BM->LoadBiome(EBiomeId::ObsidianForge);
BM->SetBiomeBlend(EBiomeId::ObsidianForge, EBiomeId::Frostvein, 0.5f);
```

## 音频
```cpp
UMetaSoundWeaveController* AC = ...;
AC->SetStability(0.9f);
AC->SetBiomeBlend("Obsidian", "Frostvein", 0.5f);
AC->TriggerWeaveEvent("Stitch");
```

## 难题
```cpp
ARiftPuzzleActor* P = ...;
P->TrySolve({Anchor1, Anchor2}); // RequiredAnchors=2
P->OnSolved.AddDynamic(this, &MyClass::OnSolved);
```

## Mass
```cpp
// Elk fragment
FFragment_FrostElk Elk; Elk.Panic = 0.8f;
// Processor: WeaverCrowdProcessor (30Hz)
```

## 网络
```cpp
// ReplicationGraph: AlwaysRelevant → RiftVolume, Dormancy 120m for Mass
// Iris: adaptive 10-30Hz, RPC聚合
```

## BP 节点
- `WeaveAbility` (GAS): Cooldown 0.5, Cost 0.05
- `WeaveAttributeSet`: Stability/WeavePower/AnchorCount (replicated)
- `AccessibilitySubsystem`: SetColorBlindMode, SetSingleStick
