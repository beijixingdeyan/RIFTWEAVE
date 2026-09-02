#pragma once
#include "CoreMinimal.h"
#include "ControlRig.h"
#include "WeaverControlRig.generated.h"
/// ControlRig for Weaver: full-body IK + look-at + hand warp for weave reach.
/// Drives 52 MetaHuman face BS + body IK. Used by WeaverAnimInstance.
/// Rig units: LimbIK (arms/legs), LookAt (eyes), Fabrik (spine), Spring (cloak).
UCLASS()
class RIFTWEAVE_API UWeaverControlRig : public UControlRig
{
    GENERATED_BODY()
public:
    UWeaverControlRig();
    UPROPERTY(EditAnywhere, Category="Weave") float HandReachScale=1.2f;
    UFUNCTION(BlueprintCallable) void SetWeaveTarget(FVector Target);
    UFUNCTION(BlueprintCallable) void SetLookAtTarget(FVector EyeTarget);
protected:
    UPROPERTY() FVector WeaveTargetCache;
};
