#pragma once
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
