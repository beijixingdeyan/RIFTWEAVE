#pragma once
#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"
#include "LoomWorkshopWidget.generated.h"
class ULoomPattern;
UCLASS()
class RIFTWEAVE_API ULoomWorkshopWidget : public UUserWidget
{
    GENERATED_BODY()
public:
    UPROPERTY(BlueprintReadOnly, meta=(BindWidget)) class UUniformGridPanel* PatternGrid;
    UPROPERTY(BlueprintReadOnly, meta=(BindWidget)) class UTextBlock* PreviewText;
    UFUNCTION(BlueprintCallable) void RefreshPatterns(const TArray<ULoomPattern*>& Patterns);
    UFUNCTION(BlueprintCallable) void OnPatternSelected(ULoomPattern* Pattern);
    UPROPERTY(BlueprintAssignable) FOnPatternSelected OnPatternChosen;
    DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnPatternSelected, ULoomPattern*, Pattern);
};
