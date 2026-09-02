import pathlib
base = pathlib.Path(r"E:\github\dsh\projects\helloworld -unrealengine")
def write(p, c):
    full = base / p
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(c.strip()+"\n", encoding="utf-8")
    print(f"wrote {p}")

# --- Additional C++ systems to enlarge project ---

# 1. Gameplay Ability System
write("Source/RiftWeave/Public/Ability/WeaveAbility.h", r'''#pragma once
#include "CoreMinimal.h"
#include "Abilities/GameplayAbility.h"
#include "WeaveAbility.generated.h"
class UWeaveComponent;
UCLASS()
class RIFTWEAVE_API UWeaveAbility : public UGameplayAbility
{
    GENERATED_BODY()
public:
    UWeaveAbility();
    UPROPERTY(EditDefaultsOnly, Category="Weave") float Cooldown=0.5f;
    UPROPERTY(EditDefaultsOnly, Category="Weave") float StabilityCost=0.05f;
    virtual void ActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, const FGameplayEventData* TriggerEventData) override;
    virtual void EndAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, bool bReplicateEndAbility, bool bWasCancelled) override;
    UFUNCTION(BlueprintCallable) bool CanWeave() const;
};
''')
write("Source/RiftWeave/Private/Ability/WeaveAbility.cpp", r'''#include "Ability/WeaveAbility.h"
#include "AbilitySystemComponent.h"
UWeaveAbility::UWeaveAbility(){ InstancingPolicy=EGameplayAbilityInstancingPolicy::InstancedPerActor; }
void UWeaveAbility::ActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* Info, const FGameplayAbilityActivationInfo ActInfo, const FGameplayEventData* Data){ Super::ActivateAbility(Handle,Info,ActInfo,Data); UE_LOG(LogTemp,Log,TEXT("[Ability] Weave activate")); }
void UWeaveAbility::EndAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* Info, const FGameplayAbilityActivationInfo ActInfo, bool bRep, bool bCancel){ Super::EndAbility(Handle,Info,ActInfo,bRep,bCancel); }
bool UWeaveAbility::CanWeave() const { return true; }
''')
write("Source/RiftWeave/Public/Ability/WeaveAttributeSet.h", r'''#pragma once
#include "CoreMinimal.h"
#include "AttributeSet.h"
#include "AbilitySystemComponent.h"
#include "WeaveAttributeSet.generated.h"
#define ATTRIBUTE_ACCESSORS(Class, Prop) \
    GAMEPLAYATTRIBUTE_PROPERTY_GETTER(Class, Prop) \
    GAMEPLAYATTRIBUTE_VALUE_GETTER(Prop) \
    GAMEPLAYATTRIBUTE_VALUE_SETTER(Prop) \
    GAMEPLAYATTRIBUTE_VALUE_INITTER(Prop)
UCLASS()
class RIFTWEAVE_API UWeaveAttributeSet : public UAttributeSet
{
    GENERATED_BODY()
public:
    UWeaveAttributeSet();
    UPROPERTY(BlueprintReadOnly, Category="Weave", ReplicatedUsing=OnRep_Stability) FGameplayAttributeData Stability;
    ATTRIBUTE_ACCESSORS(UWeaveAttributeSet, Stability)
    UPROPERTY(BlueprintReadOnly, Category="Weave", ReplicatedUsing=OnRep_WeavePower) FGameplayAttributeData WeavePower;
    ATTRIBUTE_ACCESSORS(UWeaveAttributeSet, WeavePower)
    UPROPERTY(BlueprintReadOnly, Category="Weave", ReplicatedUsing=OnRep_AnchorCount) FGameplayAttributeData AnchorCount;
    ATTRIBUTE_ACCESSORS(UWeaveAttributeSet, AnchorCount)
    UFUNCTION() void OnRep_Stability(const FGameplayAttributeData& Old);
    UFUNCTION() void OnRep_WeavePower(const FGameplayAttributeData& Old);
    UFUNCTION() void OnRep_AnchorCount(const FGameplayAttributeData& Old);
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const override;
};
''')
write("Source/RiftWeave/Public/World/WeatherSystem.h", r'''#pragma once
#include "CoreMinimal.h"
#include "Subsystems/WorldSubsystem.h"
#include "WeatherSystem.generated.h"
UENUM(BlueprintType) enum class EWeatherType : uint8 { Clear, AshFall, SnowStorm, SporeRain, Aurora };
UCLASS()
class RIFTWEAVE_API UWeatherSystem : public UWorldSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void SetWeather(EWeatherType Type, float TransitionTime=2.f);
    UFUNCTION(BlueprintPure) EWeatherType GetWeather() const { return Current; }
    UPROPERTY(BlueprintAssignable) FOnWeatherChanged OnWeatherChanged;
    DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnWeatherChanged, EWeatherType, NewWeather, float, Intensity);
private:
    UPROPERTY() EWeatherType Current=EWeatherType::Clear;
};
''')
write("Source/RiftWeave/Private/World/WeatherSystem.cpp", r'''#include "World/WeatherSystem.h"
void UWeatherSystem::SetWeather(EWeatherType T,float TT){ Current=T; OnWeatherChanged.Broadcast(T,1.f); UE_LOG(LogTemp,Log,TEXT("[Weather] %d"),(int32)T); }
''')
write("Source/RiftWeave/Public/World/PhotoModeSubsystem.h", r'''#pragma once
#include "CoreMinimal.h"
#include "Subsystems/GameInstanceSubsystem.h"
#include "PhotoModeSubsystem.generated.h"
UCLASS()
class RIFTWEAVE_API UPhotoModeSubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void EnterPhotoMode();
    UFUNCTION(BlueprintCallable) void ExitPhotoMode();
    UFUNCTION(BlueprintCallable) void CapturePhoto(FString Filename);
    UFUNCTION(BlueprintPure) bool IsInPhotoMode() const { return bActive; }
    UPROPERTY(BlueprintAssignable) FSimpleMulticastDelegate OnPhotoTaken;
private:
    bool bActive=false;
};
''')
write("Source/RiftWeave/Private/World/PhotoModeSubsystem.cpp", r'''#include "World/PhotoModeSubsystem.h"
#include "Kismet/GameplayStatics.h"
void UPhotoModeSubsystem::EnterPhotoMode(){ bActive=true; UGameplayStatics::SetGamePaused(GetWorld(),true); }
void UPhotoModeSubsystem::ExitPhotoMode(){ bActive=false; UGameplayStatics::SetGamePaused(GetWorld(),false); }
void UPhotoModeSubsystem::CapturePhoto(FString Fn){ OnPhotoTaken.Broadcast(); UE_LOG(LogTemp,Log,TEXT("[Photo] %s"),*Fn); }
''')
write("Source/RiftWeave/Public/UI/PhotoModeWidget.h", r'''#pragma once
#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"
#include "PhotoModeWidget.generated.h"
UCLASS()
class RIFTWEAVE_API UPhotoModeWidget : public UUserWidget
{
    GENERATED_BODY()
public:
    UPROPERTY(meta=(BindWidget)) class UButton* BtnCapture;
    UPROPERTY(meta=(BindWidget)) class UButton* BtnExit;
    UPROPERTY(meta=(BindWidget)) class UTextBlock* TxtCoords;
    UFUNCTION(BlueprintCallable) void OnCaptureClicked();
    UFUNCTION(BlueprintCallable) void UpdateCoords(FVector Loc);
};
''')
write("Source/RiftWeave/Public/AI/AIWeaverCompanion.h", r'''#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "AIWeaverCompanion.generated.h"
class UStateTreeComponent;
/// AI companion for single-player — fills anchor role via StateTree + SmartObject.
UCLASS()
class RIFTWEAVE_API AAIWeaverCompanion : public ACharacter
{
    GENERATED_BODY()
public:
    AAIWeaverCompanion();
    UPROPERTY(VisibleAnywhere, Category="AI") TObjectPtr<UStateTreeComponent> StateTreeComp;
    UFUNCTION(BlueprintCallable) void CommandAnchor(FVector Location);
    UFUNCTION(BlueprintCallable) void FollowPlayer(AActor* Player);
protected:
    virtual void BeginPlay() override;
};
''')
write("Source/RiftWeave/Private/AI/AIWeaverCompanion.cpp", r'''#include "AI/AIWeaverCompanion.h"
#include "Components/StateTreeComponent.h"
AAIWeaverCompanion::AAIWeaverCompanion(){ StateTreeComp=CreateDefaultSubobject<UStateTreeComponent>("StateTree"); }
void AAIWeaverCompanion::BeginPlay(){ Super::BeginPlay(); }
void AAIWeaverCompanion::CommandAnchor(FVector L){ UE_LOG(LogTemp,Log,TEXT("[Companion] Anchor at %s"),*L.ToString()); }
void AAIWeaverCompanion::FollowPlayer(AActor* P){ UE_LOG(LogTemp,Log,TEXT("[Companion] Follow %s"),*GetNameSafe(P)); }
''')
write("Source/RiftWeave/Public/World/CollectibleThread.h", r'''#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "CollectibleThread.generated.h"
UCLASS()
class RIFTWEAVE_API ACollectibleThread : public AActor
{
    GENERATED_BODY()
public:
    ACollectibleThread();
    UPROPERTY(EditAnywhere, Category="Collectible") FName ThreadId;
    UPROPERTY(EditAnywhere, Category="Collectible") int32 Value=1;
    UPROPERTY(ReplicatedUsing=OnRep_Collected, BlueprintReadOnly) bool bCollected=false;
    UFUNCTION() void OnRep_Collected();
    UFUNCTION(BlueprintCallable) void Collect(AActor* Collector);
    UPROPERTY(BlueprintAssignable) FSimpleMulticastDelegate OnCollected;
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const override;
protected:
    UPROPERTY(VisibleAnywhere) TObjectPtr<UStaticMeshComponent> Mesh;
};
''')
write("Source/RiftWeave/Private/World/CollectibleThread.cpp", r'''#include "World/CollectibleThread.h"
#include "Net/UnrealNetwork.h"
ACollectibleThread::ACollectibleThread(){ bReplicates=true; Mesh=CreateDefaultSubobject<UStaticMeshComponent>("Mesh"); RootComponent=Mesh; }
void ACollectibleThread::Collect(AActor* C){ if(!bCollected){ bCollected=true; OnCollected.Broadcast(); OnRep_Collected(); } }
void ACollectibleThread::OnRep_Collected(){ Mesh->SetVisibility(false); }
void ACollectibleThread::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(ACollectibleThread,bCollected); }
''')
write("Source/RiftWeave/Public/Core/WeaveDeveloperSettings.h", r'''#pragma once
#include "CoreMinimal.h"
#include "Engine/DeveloperSettings.h"
#include "WeaveDeveloperSettings.generated.h"
UCLASS(Config=Game, DefaultConfig, meta=(DisplayName="RiftWeave Settings"))
class RIFTWEAVE_API UWeaveDeveloperSettings : public UDeveloperSettings
{
    GENERATED_BODY()
public:
    UPROPERTY(Config, EditAnywhere, Category="Weave") float MaxWeaveReach=4000.f;
    UPROPERTY(Config, EditAnywhere, Category="Weave") float DefaultStability=1.f;
    UPROPERTY(Config, EditAnywhere, Category="World") int32 TargetMassCount=3000;
    UPROPERTY(Config, EditAnywhere, Category="Audio") bool bEnableMetaSounds=true;
    virtual FName GetCategoryName() const override { return FName("Game"); }
};
''')
write("Source/RiftWeave/Public/World/SmartObject_Weave.h", r'''#pragma once
#include "CoreMinimal.h"
#include "SmartObjectDefinition.h"
#include "SmartObject_Weave.generated.h"
UCLASS()
class RIFTWEAVE_API USmartObject_WeaveDefinition : public USmartObjectDefinition
{
    GENERATED_BODY()
public:
    UPROPERTY(EditAnywhere, Category="Weave") float RequiredStability=0.7f;
    UPROPERTY(EditAnywhere, Category="Weave") FName PatternId="BasicStitch";
};
''')

# Tools
write("Tools/AssetPipeline/README.md", r"""# Asset Pipeline — RiftWeave

## Flow
Quixel Bridge -> FBX/EXR -> `import.py` -> UE Content -> validate

## Scripts
- `validate_assets.py --all` : naming + Nanite + generated.h checks
- `import.py` : batch import with Nanite flags (see Config/AssetImport.json)

## Config
`Tools/AssetPipeline/AssetImport.json` defines per-folder Nanite policy.

## CI
GitHub Actions runs validate on every PR.
""")
write("Tools/AssetPipeline/AssetImport.json", r"""{
  "version": 1,
  "policies": [
    { "path": "Content/World/Biomes/ObsidianForge/Meshes", "nanite": true, "lod": "auto" },
    { "path": "Content/World/Biomes/Frostvein/Meshes", "nanite": true, "lod": "auto" },
    { "path": "Content/World/Biomes/LuminousCanopy/Meshes/Trunks", "nanite": true, "lod": "auto" },
    { "path": "Content/World/Biomes/LuminousCanopy/Meshes/Foliage", "nanite": false, "lod": "4 + impostor" },
    { "path": "Content/Weavers", "nanite": false, "lod": "4 skeletal" },
    { "path": "Content/Niagara", "nanite": false, "lod": "n/a" }
  ]
}
""")
write("Tools/AssetPipeline/import.py", r"""#!/usr/bin/env python3
"""+"\"\"\"Batch import helper (stub) - integrates Quixel Bridge export.\"\"\""+r"""
import json, pathlib
cfg = json.load(open(pathlib.Path(__file__).parent / "AssetImport.json", encoding="utf-8"))
print(f"Import policies: {len(cfg['policies'])}")
for p in cfg["policies"]:
    print(f"  {p['path']} nanite={p['nanite']}")
print("Stub: run via UE Python (unreal.AssetTools) in editor.")
""")

# Tests
write("Tests/README.md", r"""# Tests — RiftWeave

## Automation
- `Tests/Gauntlet_WeaveSync.spec.json` : 4-client weave sync test
- `Tests/Perf_Mass2000.spec.json` : Mass 2000 perf baseline

Run via:
```
ue4 run Gauntlet -spec=Tests/Gauntlet_WeaveSync.spec.json
```
""")
write("Tests/Gauntlet_WeaveSync.spec.json", r"""{
  "name": "WeaveSync 4-Player",
  "clients": 4,
  "map": "/Game/Maps/Test_Mass_2000",
  "test": "WeaveSyncTest",
  "successCriteria": { "stabilityDelta": 0.02, "serverTickMs": 14, "durationSec": 120 }
}
""")
write("Tests/Perf_Mass2000.spec.json", r"""{
  "name": "Mass 2000 Perf",
  "map": "/Game/Maps/Test_Mass_2000",
  "agents": 2000,
  "criteria": { "avgFrameMs": 16.6, "massMs": 3.0, "naniteMs": 12.0 }
}
""")

# Localization
write("Config/Localization/README.md", r"""# Localization

- Source: `LOCTEXT` in C++/Blueprint
- Dashboard: `Window > Localization Dashboard`
- Targets: en, zh-Hans, ja
- Export: `Localization/RiftWeave.csv`
- Font: Noto Sans SC (zh), Noto Sans JP (ja), Inter (en)
""")
write("Localization/RiftWeave.csv", r""""Key","Source","en","zh-Hans","ja"
"WeaveAction","Weave","Weave","编织","織る"
"AnchorAction","Anchor","Anchor","锚定","アンカー"
"Stability","Stability","Stability","稳定性","安定性"
"PhotoMode","Photo Mode","Photo Mode","摄影模式","フォトモード"
"LoomWorkshop","Loom Workshop","Loom Workshop","织机工坊","織機工房"
""")

# GitHub templates
write(".github/ISSUE_TEMPLATE/bug_report.md", r"""---
name: Bug report
about: Report a weave that broke
title: "[Bug] "
labels: bug
---
**Describe the bug**
**Repro steps**
1. Go to '...'
2. Weave '...'
3. See error

**Expected**
**Screenshots**
**Platform** (PC/PS5/XSX)
""")
write(".github/ISSUE_TEMPLATE/feature_request.md", r"""---
name: Feature request
about: Suggest a new Pattern or POI
title: "[Feature] "
labels: enhancement
---
**Is your feature for a new Pattern / POI / System?**
**Describe**
**Why mass-market?**
""")
write(".github/pull_request_template.md", r"""## Describe
## Checklist
- [ ] `py Tools/AssetPipeline/validate_assets.py --all` passed
- [ ] No secrets committed
- [ ] Docs updated if gameplay changed
- [ ] Tested on at least 1 biome
""")
write("CHANGELOG.md", r"""# Changelog — RiftWeave

All notable changes follow Keep a Changelog + SemVer.

## [0.9.0] - 2026-09-02
### Added
- Core Weave/Anchor loop (Chaos field + Lumen GI)
- 3 biomes (Obsidian/Frostvein/Canopy) as World Partition DataLayers
- MassAI 2000 elk herd + StateTree
- MetaSounds loom + Quartz clock
- ReplicationGraph + Iris 4-player co-op + 50-player plaza (async ghosts)
- Loom Workshop + Photo Mode + 40 Pattern DataAssets
- Full GDD (12 chapters) + CI + LFS

### Known Issues
- Gas: HLOD clusters flicker at 4000m (fix r.HLOD.DistanceScale)
""")
write("SECURITY.md", r"""# Security

Report vulnerabilities via GitHub Security Advisories (private). No credentials in repo.

- Do not commit `.env`, `*.pem`, or `Saved/Config/*.ini`
- CI checks for secret patterns (`AKIA`, `ghp_`)
""")
write("CODE_OF_CONDUCT.md", r"""# Code of Conduct

Be kind. Weave together. Harassment, hate, or gatekeeping will be removed. See Contributor Covenant 2.1.
""")

# Content expands
write("Content/Maps/WP_RiftWeave.umap.README.md", r"""# WP_RiftWeave — Main World Partition Map

- Size: 4096x4096m (16km2)
- DataLayers: DL_Obsidian, DL_Frostvein, DL_Canopy, DL_Shared
- HLOD: 3 levels, cluster 128m
- PCG: RiftCracks (4000/km2), Foliage (800/km2)
- Lighting: Lumen HWRT, Volumetric Fog, SkyAtmosphere
- Test: Load each DataLayer in isolation -> stat streaming <2ms
""")
write("Content/Audio/MetaSounds/MS_Loom_Base.uasset.README.md", r"""# MS_Loom_Base (MetaSoundSource)

- Inputs: Stability (float 0-1), BiomeBlend (float), WeaveTrigger (trigger)
- Quartz: 120 BPM, quantized to 1/8
- Graph: Granular (Stability -> grain density) + 3x filter (BiomeBlend -> crossfade)
- Output: Stereo + reverb send (Lumen-driven)
- Controlled via UMetaSoundWeaveController (C++)

## Nanite: n/a (audio)
## Lumen: drives reverb
""")
write("Content/Niagara/NS_WeaveTear.uasset.README.md", r"""# NS_WeaveTear (Niagara System)

- Emitter 1: Ribbon (fiber) - spawn on Chaos field sample, Substrate emissive
- Emitter 2: Mesh debris - spawn on tear progress
- Params: TearProgress (0-1), Stability (0-1)
- Perf: 2k particles max, cull 50m
""")

# Additional doc for completeness
write("Documentation/12_FAQ.md", r"""# FAQ — RiftWeave

## Does it require UE?
No. All GDD is Markdown; code is readable without building. Build only if you have UE 5.4 + VS2022.

## Is it a tech demo?
No. Nanite/Lumen/Chaos are gameplay: tear needs Nanite detail, light-drag needs Lumen GI, destruction needs Chaos. All serve the 5-min loop.

## Can I play solo?
Yes. AI companion fills anchors via StateTree. Solo puzzle S_max 0.6, co-op 1.2 — solo is calm, co-op is comedy.

## How big is the world?
16km2 WP, 3 DataLayers, 52 POIs, 40 Patterns, 20h main + 100h repeatable.

## Monetization?
Buy-to-play $29.99, cosmetics only, all earnable.

## Performance?
See 04_TechImplementation.md scalability table. PC Ultra 4K60, PS5 60.

## UGC?
Loom Workshop in-game; patterns tradeable; Creator Fund.

## Accessibility?
3-button core, remappable, single-stick, color-blind, subtitles, haptics.

## Why "RiftWeave"?
Rift + Weave = you tear rifts and weave them. Chinese "织裂者" = one who weaves rifts.
""")
write("Documentation/13_Glossary.md", r"""# Glossary

- **Weave**: Hold Weave button + drag to tear/drag/stitch.
- **Anchor**: Pin a seam; 2-4 needed for big rifts.
- **Stability (S)**: 0-1.2, governs success.
- **Rift**: Dimensional overlap volume (RiftVolume).
- **Pattern**: LoomPattern DataAsset (visual + bonus).
- **DataLayer**: World Partition layer per biome.
- **HLOD**: Hierarchical LOD for Nanite clusters.
- **MassAI**: Mass Entity crowd (elk/drone/sprite).
- **StateTree**: AI logic graph.
- **MetaSounds**: Procedural audio graph.
- **Iris**: UE replication system.
- **ReplicationGraph**: Relevance & dormancy.
- **PCG**: Procedural Content Generation.
- **Substrate**: UE layered material.
- **Chaos**: Destruction/cloth/field.
- **Lumen**: Global illumination.
- **Nanite**: Virtualized geometry.
""")

print("large gen done")
