#pragma once
#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"
#include "PhotoModeWidget.generated.h"
UCLASS()
class RIFTWEAVE_API UPhotoModeWidget : public UUserWidget
{
    GENERATED_BODY()
public:
    UPROPERTY(meta=(BindWidget)) class UButton* BtnCapture;
    UPROPERTY(meta=(BindWidget)) class UButton* BtnExit;
    UPROPERTY(meta=(BindWidget)) class UTextBlock* TxtCoords;
    UFUNCTION(BlueprintCallable) void OnCaptureClicked();
    UFUNCTION(BlueprintCallable) void UpdateCoords(FVector Loc);
};
