#pragma once
#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"
#include "RiftWeavePlayerController.generated.h"
class UEnhancedInputAction;
class UInputMappingContext;
UCLASS()
class RIFTWEAVE_API ARiftWeavePlayerController : public APlayerController
{
    GENERATED_BODY()
public:
    ARiftWeavePlayerController();
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UInputMappingContext> WeaverMappingContext;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Move;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Look;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Weave;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Anchor;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Interact;
    UPROPERTY(EditDefaultsOnly, Category="Input") TObjectPtr<UEnhancedInputAction> IA_Photo;
    UFUNCTION(BlueprintCallable) void TogglePhotoMode();
    UFUNCTION(BlueprintCallable) void RequestRemap(FName ActionName);
protected:
    virtual void BeginPlay() override;
    virtual void SetupInputComponent() override;
    void OnWeaveStarted(const struct FInputActionValue& Value);
    void OnWeaveCompleted(const struct FInputActionValue& Value);
    void OnAnchor(const struct FInputActionValue& Value);
};
