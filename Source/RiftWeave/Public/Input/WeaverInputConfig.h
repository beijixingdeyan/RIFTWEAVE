#pragma once
#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "WeaverInputConfig.generated.h"
class UInputMappingContext; class UInputAction;
/// DataAsset for EnhancedInput: IMC_Weaver + 5 InputActions (Move/Look/Weave/Anchor/Interact + Photo)
/// Mass-market: Move+Look+Weave+Anchor+Interact only. Sprint/Jump folded into Weave hold.
UCLASS(BlueprintType)
class RIFTWEAVE_API UWeaverInputConfig : public UPrimaryDataAsset
{
    GENERATED_BODY()
public:
    UPROPERTY(EditAnywhere, Category="Input") TObjectPtr<UInputMappingContext> IMC_Weaver;
    UPROPERTY(EditAnywhere, Category="Input") TObjectPtr<UInputAction> IA_Move;
    UPROPERTY(EditAnywhere, Category="Input") TObjectPtr<UInputAction> IA_Look;
    UPROPERTY(EditAnywhere, Category="Input") TObjectPtr<UInputAction> IA_Weave;
    UPROPERTY(EditAnywhere, Category="Input") TObjectPtr<UInputAction> IA_Anchor;
    UPROPERTY(EditAnywhere, Category="Input") TObjectPtr<UInputAction> IA_Interact;
    UPROPERTY(EditAnywhere, Category="Input") TObjectPtr<UInputAction> IA_Photo;
    UFUNCTION(BlueprintCallable) void ApplyToPlayer(APlayerController* PC);
};
