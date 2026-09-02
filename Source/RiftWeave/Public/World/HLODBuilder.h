#pragma once
#include "CoreMinimal.h"
#include "World/HLODBuilder.h"
#include "HLODBuilder.generated.h"
/// HLOD builder for Nanite clusters: 128m cells -> 3 levels, merges 256 instances.
/// Driven by WorldPartition HLODUtilities, validates via stat HLOD.
UCLASS()
class RIFTWEAVE_API UHLODBuilder_RiftWeave : public UHLODBuilder
{
    GENERATED_BODY()
public:
    UPROPERTY(EditAnywhere, Category="HLOD") float CellSize=12800.f;
    UPROPERTY(EditAnywhere, Category="HLOD") int32 Levels=3;
    UFUNCTION(BlueprintCallable) void BuildHLODForBiome(FName BiomeLayer);
};
