#pragma once
#include "CoreMinimal.h"
#include "Abilities/GameplayAbility.h"
#include "WeaveAbility.generated.h"
class UWeaveComponent;
UCLASS()
class RIFTWEAVE_API UWeaveAbility : public UGameplayAbility
{
    GENERATED_BODY()
public:
    UWeaveAbility();
    UPROPERTY(EditDefaultsOnly, Category="Weave") float Cooldown=0.5f;
    UPROPERTY(EditDefaultsOnly, Category="Weave") float StabilityCost=0.05f;
    virtual void ActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, const FGameplayEventData* TriggerEventData) override;
    virtual void EndAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo, const FGameplayAbilityActivationInfo ActivationInfo, bool bReplicateEndAbility, bool bWasCancelled) override;
    UFUNCTION(BlueprintCallable) bool CanWeave() const;
};
