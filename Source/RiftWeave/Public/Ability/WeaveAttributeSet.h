#pragma once
#include "CoreMinimal.h"
#include "AttributeSet.h"
#include "AbilitySystemComponent.h"
#include "WeaveAttributeSet.generated.h"
#define ATTRIBUTE_ACCESSORS(Class, Prop) \
    GAMEPLAYATTRIBUTE_PROPERTY_GETTER(Class, Prop) \
    GAMEPLAYATTRIBUTE_VALUE_GETTER(Prop) \
    GAMEPLAYATTRIBUTE_VALUE_SETTER(Prop) \
    GAMEPLAYATTRIBUTE_VALUE_INITTER(Prop)
UCLASS()
class RIFTWEAVE_API UWeaveAttributeSet : public UAttributeSet
{
    GENERATED_BODY()
public:
    UWeaveAttributeSet();
    UPROPERTY(BlueprintReadOnly, Category="Weave", ReplicatedUsing=OnRep_Stability) FGameplayAttributeData Stability;
    ATTRIBUTE_ACCESSORS(UWeaveAttributeSet, Stability)
    UPROPERTY(BlueprintReadOnly, Category="Weave", ReplicatedUsing=OnRep_WeavePower) FGameplayAttributeData WeavePower;
    ATTRIBUTE_ACCESSORS(UWeaveAttributeSet, WeavePower)
    UPROPERTY(BlueprintReadOnly, Category="Weave", ReplicatedUsing=OnRep_AnchorCount) FGameplayAttributeData AnchorCount;
    ATTRIBUTE_ACCESSORS(UWeaveAttributeSet, AnchorCount)
    UFUNCTION() void OnRep_Stability(const FGameplayAttributeData& Old);
    UFUNCTION() void OnRep_WeavePower(const FGameplayAttributeData& Old);
    UFUNCTION() void OnRep_AnchorCount(const FGameplayAttributeData& Old);
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const override;
};
