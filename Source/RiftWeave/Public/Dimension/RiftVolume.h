#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Volume.h"
#include "RiftVolume.generated.h"

/// Volume where two dimensions overlap — defines blend curve, physics material swap, spawn rules.
UCLASS()
class RIFTWEAVE_API ARiftVolume : public AVolume
{
    GENERATED_BODY()
public:
    ARiftVolume();
    UPROPERTY(EditAnywhere, Category="Rift") FName RiftId;
    UPROPERTY(EditAnywhere, Category="Rift") EDimensionId SourceDim;
    UPROPERTY(EditAnywhere, Category="Rift") EDimensionId TargetDim;
    UPROPERTY(EditAnywhere, Category="Rift") UCurveFloat* BlendCurve;
    UPROPERTY(EditAnywhere, Category="Rift") float RequiredAnchors = 2;

    UFUNCTION(BlueprintCallable) float GetBlendAtLocation(FVector Loc) const;
};
