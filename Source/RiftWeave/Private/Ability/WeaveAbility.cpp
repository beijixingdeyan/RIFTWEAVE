#include "Ability/WeaveAbility.h"
#include "AbilitySystemComponent.h"
UWeaveAbility::UWeaveAbility(){ InstancingPolicy=EGameplayAbilityInstancingPolicy::InstancedPerActor; }
void UWeaveAbility::ActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* Info, const FGameplayAbilityActivationInfo ActInfo, const FGameplayEventData* Data){ Super::ActivateAbility(Handle,Info,ActInfo,Data); UE_LOG(LogTemp,Log,TEXT("[Ability] Weave activate")); }
void UWeaveAbility::EndAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* Info, const FGameplayAbilityActivationInfo ActInfo, bool bRep, bool bCancel){ Super::EndAbility(Handle,Info,ActInfo,bRep,bCancel); }
bool UWeaveAbility::CanWeave() const { return true; }
