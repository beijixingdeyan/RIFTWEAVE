import pathlib
base = pathlib.Path(r"E:\github\dsh\projects\helloworld -unrealengine")
files = {}

files[r"Source/RiftWeave/Public/Core/RiftWeavePlayerController.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"
#include "RiftWeavePlayerController.generated.h"
class UEnhancedInputAction;
class UInputMappingContext;
UCLASS()
class RIFTWEAVE_API ARiftWeavePlayerController : public APlayerController
{
    GENERATED_BODY()
public:
    ARiftWeavePlayerController();
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UInputMappingContext> WeaverMappingContext;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Move;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Look;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Weave;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Anchor;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Interact;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Photo;
    UFUNCTION(BlueprintCallable) void TogglePhotoMode();
    UFUNCTION(BlueprintCallable) void RequestRemap(FName ActionName);
protected:
    virtual void BeginPlay() override;
    virtual void SetupInputComponent() override;
    void OnWeaveStarted(const struct FInputActionValue& Value);
    void OnWeaveCompleted(const struct FInputActionValue& Value);
    void OnAnchor(const struct FInputActionValue& Value);
};
'''

files[r"Source/RiftWeave/Private/Core/RiftWeavePlayerController.cpp"] = r'''#include "Core/RiftWeavePlayerController.h"
#include "EnhancedInputComponent.h"
#include "EnhancedInputSubsystems.h"
ARiftWeavePlayerController::ARiftWeavePlayerController(){ bShowMouseCursor=false; }
void ARiftWeavePlayerController::BeginPlay(){
    Super::BeginPlay();
    if(auto* Sub=ULocalPlayer::GetSubsystem<UEnhancedInputLocalPlayerSubsystem>(GetLocalPlayer())){
        if(WeaverMappingContext) Sub->AddMappingContext(WeaverMappingContext,0);
    }
}
void ARiftWeavePlayerController::SetupInputComponent(){
    Super::SetupInputComponent();
    if(auto* EIC=Cast<UEnhancedInputComponent>(InputComponent)){
        if(IA_Weave){ EIC->BindAction(IA_Weave,ETriggerEvent::Started,this,&ARiftWeavePlayerController::OnWeaveStarted); EIC->BindAction(IA_Weave,ETriggerEvent::Completed,this,&ARiftWeavePlayerController::OnWeaveCompleted); }
        if(IA_Anchor) EIC->BindAction(IA_Anchor,ETriggerEvent::Triggered,this,&ARiftWeavePlayerController::OnAnchor);
    }
}
void ARiftWeavePlayerController::OnWeaveStarted(const FInputActionValue& V){ UE_LOG(LogTemp,Verbose,TEXT("[PC] Weave start")); }
void ARiftWeavePlayerController::OnWeaveCompleted(const FInputActionValue& V){ UE_LOG(LogTemp,Verbose,TEXT("[PC] Weave end")); }
void ARiftWeavePlayerController::OnAnchor(const FInputActionValue& V){}
void ARiftWeavePlayerController::TogglePhotoMode(){}
void ARiftWeavePlayerController::RequestRemap(FName A){}
'''

files[r"Source/RiftWeave/Public/Core/RiftWeaveGameInstance.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Engine/GameInstance.h"
#include "RiftWeaveGameInstance.generated.h"
UCLASS()
class RIFTWEAVE_API URiftWeaveGameInstance : public UGameInstance
{
    GENERATED_BODY()
public:
    virtual void Init() override;
    virtual void Shutdown() override;
    UFUNCTION(BlueprintCallable) void CreateCoopSession(int32 MaxPlayers=4);
    UFUNCTION(BlueprintCallable) void JoinSession(const FString& JoinCode);
    UPROPERTY(BlueprintReadOnly, Category="Session") FString LastJoinCode;
};
'''

files[r"Source/RiftWeave/Private/Core/RiftWeaveGameInstance.cpp"] = r'''#include "Core/RiftWeaveGameInstance.h"
void URiftWeaveGameInstance::Init(){ Super::Init(); UE_LOG(LogTemp,Log,TEXT("[GI] RiftWeave init")); }
void URiftWeaveGameInstance::Shutdown(){ Super::Shutdown(); }
void URiftWeaveGameInstance::CreateCoopSession(int32 MaxPlayers){ UE_LOG(LogTemp,Log,TEXT("[GI] Create session %d"),MaxPlayers); }
void URiftWeaveGameInstance::JoinSession(const FString& Code){ LastJoinCode=Code; UE_LOG(LogTemp,Log,TEXT("[GI] Join %s"),*Code); }
'''

files[r"Source/RiftWeave/Public/Weaving/DimensionAnchorComponent.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Components/SceneComponent.h"
#include "DimensionAnchorComponent.generated.h"
UCLASS(ClassGroup=(Weaving), meta=(BlueprintSpawnableComponent))
class RIFTWEAVE_API UDimensionAnchorComponent : public USceneComponent
{
    GENERATED_BODY()
public:
    UDimensionAnchorComponent();
    UPROPERTY(EditDefaultsOnly, Category="Anchor") float MaxAnchorDistance=4000.f;
    UPROPERTY(EditDefaultsOnly, Category="Anchor") float ChargeTime=0.8f;
    UPROPERTY(Replicated, BlueprintReadOnly, Category="Anchor") bool bAnchored=false;
    UPROPERTY(Replicated, BlueprintReadOnly, Category="Anchor") FVector AnchorLocation;
    UFUNCTION(Server,Reliable,BlueprintCallable) void Server_PlaceAnchor(FVector Location);
    UFUNCTION(Server,Reliable,BlueprintCallable) void Server_ReleaseAnchor();
    UFUNCTION(BlueprintPure) bool IsCharged() const { return ChargeRatio>=1.f; }
protected:
    UPROPERTY(Replicated) float ChargeRatio=0.f;
    virtual void TickComponent(float DT,ELevelTick T,FActorComponentTickFunction* F) override;
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const override;
};
'''

files[r"Source/RiftWeave/Private/Weaving/DimensionAnchorComponent.cpp"] = r'''#include "Weaving/DimensionAnchorComponent.h"
#include "Net/UnrealNetwork.h"
UDimensionAnchorComponent::UDimensionAnchorComponent(){ PrimaryComponentTick.bCanEverTick=true; SetIsReplicatedByDefault(true); }
void UDimensionAnchorComponent::Server_PlaceAnchor_Implementation(FVector Loc){ AnchorLocation=Loc; bAnchored=true; ChargeRatio=1.f; }
void UDimensionAnchorComponent::Server_ReleaseAnchor_Implementation(){ bAnchored=false; ChargeRatio=0.f; }
void UDimensionAnchorComponent::TickComponent(float DT,ELevelTick T,FActorComponentTickFunction* F){ Super::TickComponent(DT,T,F); }
void UDimensionAnchorComponent::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(UDimensionAnchorComponent,bAnchored); DOREPLIFETIME(UDimensionAnchorComponent,AnchorLocation); DOREPLIFETIME(UDimensionAnchorComponent,ChargeRatio); }
'''

files[r"Source/RiftWeave/Public/Weaving/LoomPattern.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "LoomPattern.generated.h"
UCLASS(BlueprintType)
class RIFTWEAVE_API ULoomPattern : public UPrimaryDataAsset
{
    GENERATED_BODY()
public:
    UPROPERTY(EditAnywhere,BlueprintReadOnly,Category="Pattern") FName PatternId;
    UPROPERTY(EditAnywhere,BlueprintReadOnly,Category="Pattern") FText DisplayName;
    UPROPERTY(EditAnywhere,BlueprintReadOnly,Category="Pattern") TObjectPtr<UMaterialInterface> SeamMaterial;
    UPROPERTY(EditAnywhere,BlueprintReadOnly,Category="Pattern") TObjectPtr<UNiagaraSystem> WeaveVFX;
    UPROPERTY(EditAnywhere,BlueprintReadOnly,Category="Pattern") float StabilityBonus=0.1f;
    UPROPERTY(EditAnywhere,BlueprintReadOnly,Category="Pattern") TArray<FName> RequiredBiomes;
    virtual FPrimaryAssetId GetPrimaryAssetId() const override { return FPrimaryAssetId("LoomPattern",PatternId); }
};
'''

files[r"Source/RiftWeave/Public/World/BiomeManager.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Subsystems/WorldSubsystem.h"
#include "BiomeManager.generated.h"
UENUM(BlueprintType) enum class EBiomeId : uint8 { ObsidianForge, Frostvein, LuminousCanopy, Shared };
UCLASS()
class RIFTWEAVE_API UBiomeManager : public UWorldSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void LoadBiome(EBiomeId Biome);
    UFUNCTION(BlueprintCallable) void UnloadBiome(EBiomeId Biome);
    UFUNCTION(BlueprintPure) bool IsBiomeLoaded(EBiomeId Biome) const;
    UFUNCTION(BlueprintCallable) void SetBiomeBlend(EBiomeId A, EBiomeId B, float Alpha);
    DECLARE_DYNAMIC_MULTICAST_DELEGATE_ThreeParams(FOnBiomeBlend, EBiomeId, A, EBiomeId, B, float, Alpha);
    UPROPERTY(BlueprintAssignable) FOnBiomeBlend OnBiomeBlend;
private:
    TSet<EBiomeId> LoadedBiomes;
};
'''

files[r"Source/RiftWeave/Private/World/BiomeManager.cpp"] = r'''#include "World/BiomeManager.h"
void UBiomeManager::LoadBiome(EBiomeId B){ LoadedBiomes.Add(B); UE_LOG(LogTemp,Log,TEXT("[Biome] Load %d"),(int32)B); }
void UBiomeManager::UnloadBiome(EBiomeId B){ LoadedBiomes.Remove(B); }
bool UBiomeManager::IsBiomeLoaded(EBiomeId B) const { return LoadedBiomes.Contains(B); }
void UBiomeManager::SetBiomeBlend(EBiomeId A, EBiomeId B, float Alpha){ OnBiomeBlend.Broadcast(A,B,Alpha); }
'''

files[r"Source/RiftWeave/Public/World/RiftPuzzleActor.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "RiftPuzzleActor.generated.h"
class UBoxComponent;
UCLASS()
class RIFTWEAVE_API ARiftPuzzleActor : public AActor
{
    GENERATED_BODY()
public:
    ARiftPuzzleActor();
    UPROPERTY(EditAnywhere,Category="Puzzle") FName PuzzleId;
    UPROPERTY(EditAnywhere,Category="Puzzle") int32 RequiredAnchors=2;
    UPROPERTY(EditAnywhere,Category="Puzzle") TArray<FName> RequiredPatterns;
    UPROPERTY(ReplicatedUsing=OnRep_Solved,BlueprintReadOnly,Category="Puzzle") bool bSolved=false;
    UFUNCTION(BlueprintCallable) void TrySolve(const TArray<FVector>& AnchorPositions);
    UFUNCTION() void OnRep_Solved();
    UPROPERTY(BlueprintAssignable) FSimpleMulticastDelegate OnSolved;
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const override;
protected:
    UPROPERTY(VisibleAnywhere) TObjectPtr<UBoxComponent> TriggerBox;
};
'''

files[r"Source/RiftWeave/Private/World/RiftPuzzleActor.cpp"] = r'''#include "World/RiftPuzzleActor.h"
#include "Components/BoxComponent.h"
#include "Net/UnrealNetwork.h"
ARiftPuzzleActor::ARiftPuzzleActor(){ bReplicates=true; TriggerBox=CreateDefaultSubobject<UBoxComponent>("Trigger"); RootComponent=TriggerBox; }
void ARiftPuzzleActor::TrySolve(const TArray<FVector>& Anchors){ if((int32)Anchors.Num()>=RequiredAnchors && !bSolved){ bSolved=true; OnSolved.Broadcast(); OnRep_Solved(); } }
void ARiftPuzzleActor::OnRep_Solved(){ UE_LOG(LogTemp,Log,TEXT("[Puzzle] %s solved"),*PuzzleId.ToString()); }
void ARiftPuzzleActor::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(ARiftPuzzleActor,bSolved); }
'''

files[r"Source/RiftWeave/Public/AI/MassWeaverAI.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "MassEntityTypes.h"
#include "MassWeaverAI.generated.h"
USTRUCT() struct FFragment_FrostElk : public FMassFragment { GENERATED_BODY() FVector Velocity; float Panic=0.f; };
USTRUCT() struct FFragment_ForgeDrone : public FMassFragment { GENERATED_BODY() FVector Target; bool bCarryingHeat=false; };
USTRUCT() struct FFragment_CanopySprite : public FMassFragment { GENERATED_BODY() float GlowPhase=0.f; };
USTRUCT() struct FTag_InRift : public FMassTag { GENERATED_BODY() };
'''

files[r"Source/RiftWeave/Public/AI/WeaverCrowdProcessor.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "MassProcessor.h"
#include "WeaverCrowdProcessor.generated.h"
UCLASS()
class RIFTWEAVE_API UWeaverCrowdProcessor : public UMassProcessor
{
    GENERATED_BODY()
public:
    UWeaverCrowdProcessor();
    virtual void ConfigureQueries(const TSharedRef<FMassEntityManager>& EM) override;
    virtual void Execute(FMassEntityManager& EM, FMassExecutionContext& Ctx) override;
protected:
    FMassEntityQuery HerdQuery;
};
'''

files[r"Source/RiftWeave/Private/AI/WeaverCrowdProcessor.cpp"] = r'''#include "AI/WeaverCrowdProcessor.h"
#include "AI/MassWeaverAI.h"
UWeaverCrowdProcessor::UWeaverCrowdProcessor(){ ExecutionFlags = (int32)EProcessorExecutionFlags::All; }
void UWeaverCrowdProcessor::ConfigureQueries(const TSharedRef<FMassEntityManager>& EM){ HerdQuery.AddRequirement<FFragment_FrostElk>(EMassFragmentAccess::ReadWrite); HerdQuery.AddTagRequirement<FTag_InRift>(EMassFragmentPresence::None); }
void UWeaverCrowdProcessor::Execute(FMassEntityManager& EM, FMassExecutionContext& Ctx){ HerdQuery.ForEachEntityChunk(EM,Ctx,[](FMassExecutionContext& C){ auto& Elks=C.GetMutableFragment<FFragment_FrostElk>(); }); }
'''

files[r"Source/RiftWeave/Public/Physics/ChaosWeaveField.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Field/FieldSystemTypes.h"
#include "ChaosWeaveField.generated.h"
UCLASS()
class RIFTWEAVE_API UChaosWeaveField : public UObject
{
    GENERATED_BODY()
public:
    static FFieldSystemCommand MakeTearField(FVector Origin,float Radius,float Magnitude);
    static FFieldSystemCommand MakeStitchField(FVector A,FVector B,float BlendAlpha);
    static FFieldSystemCommand MakeAnchorStrainField(FVector AnchorPos,float Stiffness);
};
'''

files[r"Source/RiftWeave/Private/Physics/ChaosWeaveField.cpp"] = r'''#include "Physics/ChaosWeaveField.h"
FFieldSystemCommand UChaosWeaveField::MakeTearField(FVector O,float R,float M){ return FFieldSystemCommand("Tear",nullptr); }
FFieldSystemCommand UChaosWeaveField::MakeStitchField(FVector A,FVector B,float Alpha){ return FFieldSystemCommand("Stitch",nullptr); }
FFieldSystemCommand UChaosWeaveField::MakeAnchorStrainField(FVector P,float S){ return FFieldSystemCommand("AnchorStrain",nullptr); }
'''

files[r"Source/RiftWeave/Public/Audio/MetaSoundWeaveController.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "MetaSoundWeaveController.generated.h"
class UMetaSoundSource;
UCLASS(ClassGroup=(Audio), meta=(BlueprintSpawnableComponent))
class RIFTWEAVE_API UMetaSoundWeaveController : public UActorComponent
{
    GENERATED_BODY()
public:
    UMetaSoundWeaveController();
    UPROPERTY(EditAnywhere,Category="Audio") TObjectPtr<UMetaSoundSource> LoomSource;
    UFUNCTION(BlueprintCallable) void SetStability(float S);
    UFUNCTION(BlueprintCallable) void SetBiomeBlend(FName A,FName B,float Alpha);
    UFUNCTION(BlueprintCallable) void TriggerWeaveEvent(FName EventId);
protected:
    virtual void BeginPlay() override;
    UPROPERTY() TObjectPtr<UAudioComponent> AudioComp;
};
'''

files[r"Source/RiftWeave/Private/Audio/MetaSoundWeaveController.cpp"] = r'''#include "Audio/MetaSoundWeaveController.h"
#include "Components/AudioComponent.h"
UMetaSoundWeaveController::UMetaSoundWeaveController(){ PrimaryComponentTick.bCanEverTick=false; }
void UMetaSoundWeaveController::BeginPlay(){ Super::BeginPlay(); AudioComp=NewObject<UAudioComponent>(this); if(AudioComp) AudioComp->RegisterComponent(); }
void UMetaSoundWeaveController::SetStability(float S){ if(AudioComp) AudioComp->SetFloatParameter("Stability",S); }
void UMetaSoundWeaveController::SetBiomeBlend(FName A,FName B,float Alpha){ if(AudioComp){ AudioComp->SetFloatParameter("BiomeBlend",Alpha); } }
void UMetaSoundWeaveController::TriggerWeaveEvent(FName E){ if(AudioComp) AudioComp->SetTriggerParameter(E); }
'''

files[r"Source/RiftWeave/Public/Multiplayer/RiftReplicationGraph.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "ReplicationGraph.h"
#include "RiftReplicationGraph.generated.h"
UCLASS()
class RIFTWEAVE_API URiftReplicationGraph : public UReplicationGraph
{
    GENERATED_BODY()
public:
    virtual void InitGlobalGraphNodes() override;
    virtual void InitConnectionGraphNodes(UNetReplicationGraphConnection* Conn) override;
};
'''

files[r"Source/RiftWeave/Private/Multiplayer/RiftReplicationGraph.cpp"] = r'''#include "Multiplayer/RiftReplicationGraph.h"
void URiftReplicationGraph::InitGlobalGraphNodes(){ Super::InitGlobalGraphNodes(); }
void URiftReplicationGraph::InitConnectionGraphNodes(UNetReplicationGraphConnection* C){ Super::InitConnectionGraphNodes(C); }
'''

files[r"Source/RiftWeave/Public/UI/WeaveHUD.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "GameFramework/HUD.h"
#include "WeaveHUD.generated.h"
UCLASS()
class RIFTWEAVE_API AWeaveHUD : public AHUD
{
    GENERATED_BODY()
public:
    UPROPERTY(EditDefaultsOnly,Category="UI") TSubclassOf<UUserWidget> StabilityWidgetClass;
    UPROPERTY(EditDefaultsOnly,Category="UI") TSubclassOf<UUserWidget> AnchorWidgetClass;
    virtual void BeginPlay() override;
    UFUNCTION(BlueprintCallable) void ShowWeaveHint(FText Hint);
};
'''

files[r"Source/RiftWeave/Private/UI/WeaveHUD.cpp"] = r'''#include "UI/WeaveHUD.h"
#include "Blueprint/UserWidget.h"
void AWeaveHUD::BeginPlay(){ Super::BeginPlay(); if(StabilityWidgetClass){ auto* W=CreateWidget<UUserWidget>(GetWorld(),StabilityWidgetClass); if(W) W->AddToViewport(); } }
void AWeaveHUD::ShowWeaveHint(FText H){ UE_LOG(LogTemp,Log,TEXT("[HUD] Hint: %s"),*H.ToString()); }
'''

files[r"Source/RiftWeave/Public/Animation/WeaverAnimInstance.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "Animation/AnimInstance.h"
#include "WeaverAnimInstance.generated.h"
UCLASS()
class RIFTWEAVE_API UWeaverAnimInstance : public UAnimInstance
{
    GENERATED_BODY()
public:
    UPROPERTY(BlueprintReadOnly,Category="Weave") bool bIsWeaving=false;
    UPROPERTY(BlueprintReadOnly,Category="Weave") float WeaveCharge=0.f;
    UPROPERTY(BlueprintReadOnly,Category="Movement") float Speed=0.f;
    UPROPERTY(BlueprintReadOnly,Category="Movement") bool bIsInAir=false;
    UFUNCTION(BlueprintCallable) void SetWeaveState(bool bWeaving,float Charge);
};
'''

files[r"Source/RiftWeave/Private/Animation/WeaverAnimInstance.cpp"] = r'''#include "Animation/WeaverAnimInstance.h"
void UWeaverAnimInstance::SetWeaveState(bool bW,float C){ bIsWeaving=bW; WeaveCharge=C; }
'''

files[r"Source/RiftWeave/Public/World/WorldPartitionHelper.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "World/WorldPartitionHelper.generated.h"
UCLASS()
class RIFTWEAVE_API UWorldPartitionHelper : public UObject
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable, Category="World") static void StreamInBiome(FName BiomeDataLayer);
    UFUNCTION(BlueprintCallable, Category="World") static void StreamOutBiome(FName BiomeDataLayer);
    UFUNCTION(BlueprintPure, Category="World") static bool IsDataLayerLoaded(FName Layer);
};
'''

files[r"Source/RiftWeave/Public/Core/RiftWeaveCheatManager.h"] = r'''#pragma once
#include "CoreMinimal.h"
#include "GameFramework/CheatManager.h"
#include "RiftWeaveCheatManager.generated.h"
UCLASS()
class RIFTWEAVE_API URiftWeaveCheatManager : public UCheatManager
{
    GENERATED_BODY()
public:
    UFUNCTION(Exec) void RiftWeave_GodWeave();
    UFUNCTION(Exec) void RiftWeave_TeleportBiome(FString Biome);
    UFUNCTION(Exec) void RiftWeave_SpawnRift(FString RiftId);
    UFUNCTION(Exec) void RiftWeave_SetStability(float S);
};
'''

for p,c in files.items():
    full = base / p
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(c.strip()+"\n", encoding="utf-8")
    print(f"wrote {p}")
print("all done")

