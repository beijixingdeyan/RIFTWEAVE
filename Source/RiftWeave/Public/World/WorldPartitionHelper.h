#pragma once
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
