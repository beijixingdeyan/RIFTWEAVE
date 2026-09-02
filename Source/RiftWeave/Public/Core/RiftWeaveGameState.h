#pragma once
#include "CoreMinimal.h"
#include "GameFramework/GameStateBase.h"
#include "RiftWeaveGameState.generated.h"

/// Replicated world state — biome blend ratios, active rifts, loom progress.
UCLASS()
class RIFTWEAVE_API ARiftWeaveGameState : public AGameStateBase
{
    GENERATED_BODY()
public:
    UPROPERTY(ReplicatedUsing=OnRep_BiomeBlend, BlueprintReadOnly, Category="Weave")
    TMap<FName, float> BiomeBlendRatios;

    UPROPERTY(Replicated, BlueprintReadOnly, Category="Weave")
    TArray<FName> ActiveRiftIds;

    UPROPERTY(Replicated, BlueprintReadOnly, Category="Weave")
    float GlobalWeaveStability = 1.f;

    UFUNCTION() void OnRep_BiomeBlend();
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
};
