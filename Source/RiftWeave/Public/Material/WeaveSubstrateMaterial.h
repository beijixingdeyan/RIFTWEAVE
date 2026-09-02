#pragma once
#include "CoreMinimal.h"
#include "Material/SubstrateMaterial.h"
#include "WeaveSubstrateMaterial.generated.h"
/// Substrate master for weaves: 3 slabs (base rock/ice/bark, seam emissive, cover snow/ash/moss)
/// Params: SeamProgress 0-1, PatternId, BiomeBlend. Uses RVT for large coverage.
UCLASS()
class RIFTWEAVE_API UWeaveSubstrateMaterial : public UMaterial
{
    GENERATED_BODY()
public:
    UPROPERTY(EditAnywhere, Category="Substrate") float SeamEmissive=2.0f;
    UPROPERTY(EditAnywhere, Category="Substrate") float RVTBlendDistance=5000.f;
    UFUNCTION(BlueprintCallable) void SetSeamProgress(float P);
};
