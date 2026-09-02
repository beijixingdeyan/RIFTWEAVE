import pathlib
base = pathlib.Path(r"E:\github\dsh\projects\helloworld -unrealengine")
files={}
files[r"Source/RiftWeave/Private/Weaving/WeaveComponent.cpp"] = r'''#include "Weaving/WeaveComponent.h"
#include "Net/UnrealNetwork.h"
#include "Physics/ChaosWeaveField.h"
UWeaveComponent::UWeaveComponent(){ PrimaryComponentTick.bCanEverTick=true; SetIsReplicatedByDefault(true); }
void UWeaveComponent::Server_BeginTear_Implementation(const FVector& Start,const FVector& Normal){ bIsWeaving=true; Stability=1.f; OnWeaveStateChanged.Broadcast("Tear",Stability); }
void UWeaveComponent::Server_UpdateDrag_Implementation(const FVector& TargetPos){ Stability=FMath::Clamp(Stability-0.001f,0.f,1.f); }
void UWeaveComponent::Server_EndWeave_Implementation(const FVector& End){ bIsWeaving=false; OnWeaveCompleted.Broadcast("Rift_01"); }
void UWeaveComponent::OnRep_Stability(){}
void UWeaveComponent::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(UWeaveComponent,bIsWeaving); DOREPLIFETIME(UWeaveComponent,Stability); }
void UWeaveComponent::TickComponent(float DT,ELevelTick T,FActorComponentTickFunction* F){ Super::TickComponent(DT,T,F); }
'''
files[r"Source/RiftWeave/Private/Weaving/WeaveFieldSystem.cpp"] = r'''#include "Weaving/WeaveFieldSystem.h"
AWeaveFieldSystem::AWeaveFieldSystem(){}
void AWeaveFieldSystem::ApplyTearField(const FVector& Origin,float Radius,float Magnitude){ UE_LOG(LogTemp,Log,TEXT("[Field] Tear at %s r=%.0f"),*Origin.ToString(),Radius); }
void AWeaveFieldSystem::ApplyStitchField(const FVector& A,const FVector& B,float Blend){ UE_LOG(LogTemp,Log,TEXT("[Field] Stitch blend %.2f"),Blend); }
'''
files[r"Source/RiftWeave/Private/Dimension/DimensionManager.cpp"] = r'''#include "Dimension/DimensionManager.h"
void UDimensionManager::SetDimensionWeight(EDimensionId Dim,float W){ Weights.Add(Dim,FMath::Clamp(W,0.f,1.f)); OnBlendChanged.Broadcast(Dim,W); }
float UDimensionManager::GetDimensionWeight(EDimensionId Dim) const { const float* p=Weights.Find(Dim); return p?*p:0.f; }
void UDimensionManager::BlendTo(EDimensionId Target,float Duration){ SetDimensionWeight(Target,1.f); }
'''
files[r"Source/RiftWeave/Private/Dimension/RiftVolume.cpp"] = r'''#include "Dimension/RiftVolume.h"
ARiftVolume::ARiftVolume(){}
float ARiftVolume::GetBlendAtLocation(FVector Loc) const { if(!BlendCurve) return 0.5f; float d=FVector::Dist(Loc,GetActorLocation())/2000.f; return BlendCurve->GetFloatValue(FMath::Clamp(d,0.f,1.f)); }
'''
files[r"Source/RiftWeave/Private/Core/RiftWeaveCharacter.cpp"] = r'''#include "Core/RiftWeaveCharacter.h"
#include "Weaving/WeaveComponent.h"
#include "Weaving/DimensionAnchorComponent.h"
#include "MotionWarpingComponent.h"
#include "GameFramework/CharacterMovementComponent.h"
ARiftWeaveCharacter::ARiftWeaveCharacter(const FObjectInitializer& OI):Super(OI){
    WeaveComp=CreateDefaultSubobject<UWeaveComponent>("WeaveComp");
    AnchorComp=CreateDefaultSubobject<UDimensionAnchorComponent>("AnchorComp");
    WarpingComp=CreateDefaultSubobject<UMotionWarpingComponent>("WarpingComp");
    GetCharacterMovement()->MaxWalkSpeed=520.f; GetCharacterMovement()->JumpZVelocity=650.f;
}
void ARiftWeaveCharacter::SetupPlayerInputComponent(UInputComponent* PIC){ Super::SetupPlayerInputComponent(PIC); }
void ARiftWeaveCharacter::RequestWeave(const FVector& S,const FVector& E){ if(WeaveComp) WeaveComp->Server_BeginTear(S,(E-S).GetSafeNormal()); }
void ARiftWeaveCharacter::PlaceAnchor(const FVector& Loc){ if(AnchorComp) AnchorComp->Server_PlaceAnchor(Loc); }
'''
files[r"Source/RiftWeave/Private/Core/RiftWeaveGameState.cpp"] = r'''#include "Core/RiftWeaveGameState.h"
#include "Net/UnrealNetwork.h"
void ARiftWeaveGameState::OnRep_BiomeBlend(){ UE_LOG(LogTemp,Log,TEXT("[GS] Biome blend updated")); }
void ARiftWeaveGameState::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(ARiftWeaveGameState,BiomeBlendRatios); DOREPLIFETIME(ARiftWeaveGameState,ActiveRiftIds); DOREPLIFETIME(ARiftWeaveGameState,GlobalWeaveStability); }
'''
files[r"Source/RiftWeave/Private/Core/RiftWeavePlayerState.cpp"] = r'''#include "Core/RiftWeavePlayerState.h"
#include "Net/UnrealNetwork.h"
void GetLifetimeReplicatedProps_PlayerState(TArray<FLifetimeProperty>& Out){}
'''
files[r"Source/RiftWeave/Private/World/WorldPartitionHelper.cpp"] = r'''#include "World/WorldPartitionHelper.h"
void UWorldPartitionHelper::StreamInBiome(FName L){ UE_LOG(LogTemp,Log,TEXT("[WP] StreamIn %s"),*L.ToString()); }
void UWorldPartitionHelper::StreamOutBiome(FName L){ UE_LOG(LogTemp,Log,TEXT("[WP] StreamOut %s"),*L.ToString()); }
bool UWorldPartitionHelper::IsDataLayerLoaded(FName L){ return false; }
'''
files[r"Source/RiftWeave/Private/Core/RiftWeaveCheatManager.cpp"] = r'''#include "Core/RiftWeaveCheatManager.h"
void URiftWeaveCheatManager::RiftWeave_GodWeave(){ UE_LOG(LogTemp,Log,TEXT("[Cheat] GodWeave")); }
void URiftWeaveCheatManager::RiftWeave_TeleportBiome(FString B){ UE_LOG(LogTemp,Log,TEXT("[Cheat] Teleport %s"),*B); }
void URiftWeaveCheatManager::RiftWeave_SpawnRift(FString R){ UE_LOG(LogTemp,Log,TEXT("[Cheat] Spawn %s"),*R); }
void URiftWeaveCheatManager::RiftWeave_SetStability(float S){ UE_LOG(LogTemp,Log,TEXT("[Cheat] Stability %.2f"),S); }
'''
files[r"Source/RiftWeave/Public/Weaving/WeaveSaveGame.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "GameFramework/SaveGame.h"
#include "WeaveSaveGame.generated.h"
UCLASS()
class RIFTWEAVE_API UWeaveSaveGame : public USaveGame
{
    GENERATED_BODY()
public:
    UPROPERTY(BlueprintReadWrite, Category="Save") TArray<FName> UnlockedPatterns;
    UPROPERTY(BlueprintReadWrite, Category="Save") TMap<FName,float> BestStability;
    UPROPERTY(BlueprintReadWrite, Category="Save") int32 TotalWeaves=0;
    UFUNCTION(BlueprintCallable) void AddPattern(FName Id);
};
'''
files[r"Source/RiftWeave/Public/UI/LoomWorkshopWidget.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"
#include "LoomWorkshopWidget.generated.h"
class ULoomPattern;
UCLASS()
class RIFTWEAVE_API ULoomWorkshopWidget : public UUserWidget
{
    GENERATED_BODY()
public:
    UPROPERTY(BlueprintReadOnly, meta=(BindWidget)) class UUniformGridPanel* PatternGrid;
    UPROPERTY(BlueprintReadOnly, meta=(BindWidget)) class UTextBlock* PreviewText;
    UFUNCTION(BlueprintCallable) void RefreshPatterns(const TArray<ULoomPattern*>& Patterns);
    UFUNCTION(BlueprintCallable) void OnPatternSelected(ULoomPattern* Pattern);
    UPROPERTY(BlueprintAssignable) FOnPatternSelected OnPatternChosen;
    DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnPatternSelected, ULoomPattern*, Pattern);
};
'''
files[r"Source/RiftWeave/Public/World/POIManager.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Subsystems/WorldSubsystem.h"
#include "POIManager.generated.h"
USTRUCT(BlueprintType) struct FPointOfInterest { GENERATED_BODY() FName Id; FVector Location; FText Title; int32 Difficulty=1; bool bDiscovered=false; };
UCLASS()
class RIFTWEAVE_API UPOIManager : public UWorldSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void RegisterPOI(const FPointOfInterest& POI);
    UFUNCTION(BlueprintCallable) void DiscoverPOI(FName Id);
    UFUNCTION(BlueprintPure) TArray<FPointOfInterest> GetUndiscoveredInRadius(FVector Center,float Radius) const;
private:
    TArray<FPointOfInterest> POIs;
};
'''
files[r"Plugins/RiftWeaveWeavingSystem/RiftWeaveWeavingSystem.uplugin"] = r'''{
    "FileVersion": 3,
    "Version": 1,
    "VersionName": "0.9.0",
    "FriendlyName": "RiftWeave Weaving System",
    "Description": "Core weaving logic: tear/drag/stitch, Chaos fields, pattern evaluation. Runtime + Editor tools.",
    "Category": "Gameplay",
    "CreatedBy": "WeaveWorks Studio",
    "CanContainContent": true,
    "IsBetaVersion": true,
    "Installed": false,
    "Modules": [{ "Name": "RiftWeaveWeavingSystem", "Type": "Runtime", "LoadingPhase": "Default" }]
}
'''
files[r"Plugins/RiftWeaveWeavingSystem/Source/RiftWeaveWeavingSystem/RiftWeaveWeavingSystem.Build.cs"] = r'''using UnrealBuildTool;
public class RiftWeaveWeavingSystem : ModuleRules {
    public RiftWeaveWeavingSystem(ReadOnlyTargetRules T):base(T){
        PCHUsage=PCHUsageMode.UseExplicitOrSharedPCHs;
        PublicDependencyModuleNames.AddRange(new[]{"Core","CoreUObject","Engine","Niagara","Chaos","GeometryCollectionEngine","FieldSystemEngine"});
    }
}
'''
files[r"Plugins/RiftWeaveWeavingSystem/Source/RiftWeaveWeavingSystem/Public/WeavingPatternEvaluator.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "WeavingPatternEvaluator.generated.h"
UCLASS()
class RIFTWEAVEWEAVINGSYSTEM_API UWeavingPatternEvaluator : public UObject
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable, Category="Weaving") static float EvaluateStability(float DragSpeed,float AngleError,int32 NumAnchors);
    UFUNCTION(BlueprintCallable, Category="Weaving") static FName SuggestPattern(const TArray<FName>& BiomeTags);
};
'''
files[r"Plugins/RiftWeaveWeavingSystem/Source/RiftWeaveWeavingSystem/Private/WeavingPatternEvaluator.cpp"] = r'''#include "WeavingPatternEvaluator.h"
float UWeavingPatternEvaluator::EvaluateStability(float Speed,float Angle,int32 Anchors){ float s=1.f - FMath::Clamp(Speed/2000.f,0.f,0.4f) - FMath::Clamp(Angle/90.f,0.f,0.3f); s+=Anchors*0.08f; return FMath::Clamp(s,0.f,1.f); }
FName UWeavingPatternEvaluator::SuggestPattern(const TArray<FName>& Tags){ if(Tags.Contains("Obsidian")&&Tags.Contains("Frostvein")) return "HotSpring"; return "BasicStitch"; }
'''
files[r"Plugins/DimensionStreaming/DimensionStreaming.uplugin"] = r'''{
    "FileVersion": 3,
    "Version": 1,
    "VersionName": "0.9.0",
    "FriendlyName": "Dimension Streaming",
    "Description": "World Partition data-layer driver for dimension blending. Handles Lumen cross-GI weights and Nanite LOD bias per dimension.",
    "Category": "World",
    "CreatedBy": "WeaveWorks Studio",
    "CanContainContent": false,
    "IsBetaVersion": true,
    "Modules": [{ "Name": "DimensionStreaming", "Type": "Runtime", "LoadingPhase": "PostEngineInit" }]
}
'''
files[r"Plugins/DimensionStreaming/Source/DimensionStreaming/DimensionStreaming.Build.cs"] = r'''using UnrealBuildTool;
public class DimensionStreaming : ModuleRules {
    public DimensionStreaming(ReadOnlyTargetRules T):base(T){
        PCHUsage=PCHUsageMode.UseExplicitOrSharedPCHs;
        PublicDependencyModuleNames.AddRange(new[]{"Core","CoreUObject","Engine","RenderCore"});
    }
}
'''
files[r"Plugins/DimensionStreaming/Source/DimensionStreaming/Public/DimensionStreamingSubsystem.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Subsystems/WorldSubsystem.h"
#include "DimensionStreamingSubsystem.generated.h"
UCLASS()
class RIFTWEAVE_API UDimensionStreamingSubsystem : public UWorldSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void SetDimensionAlpha(FName Dim, float Alpha);
    UFUNCTION(BlueprintPure) float GetDimensionAlpha(FName Dim) const;
private:
    TMap<FName,float> Alphas;
};
'''
for p,c in files.items():
    full = base / p
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(c.strip()+"\n", encoding="utf-8")
    print(f"wrote {p}")
print("more done")
