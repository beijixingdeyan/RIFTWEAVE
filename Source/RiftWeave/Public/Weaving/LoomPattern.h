#pragma once
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
