#pragma once
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
