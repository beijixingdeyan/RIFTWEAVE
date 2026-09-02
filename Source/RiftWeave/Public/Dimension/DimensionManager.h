#pragma once
#include "CoreMinimal.h"
#include "Subsystems/WorldSubsystem.h"
#include "DimensionManager.generated.h"

UENUM(BlueprintType)
enum class EDimensionId : uint8 { Obsidian, Frostvein, Luminous, Liminal };

/// Manages per-dimension Data Layers + Lumen blend + Nanite streaming weights.
UCLASS()
class RIFTWEAVE_API UDimensionManager : public UWorldSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void SetDimensionWeight(EDimensionId Dim, float Weight);
    UFUNCTION(BlueprintPure) float GetDimensionWeight(EDimensionId Dim) const;
    UFUNCTION(BlueprintCallable) void BlendTo(EDimensionId Target, float Duration);

    UPROPERTY(BlueprintAssignable) FOnDimensionBlendChanged OnBlendChanged;

    DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnDimensionBlendChanged, EDimensionId, Dim, float, Weight);
private:
    TMap<EDimensionId, float> Weights;
};
