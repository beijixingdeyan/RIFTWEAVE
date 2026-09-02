#pragma once
#include "CoreMinimal.h"
#include "GameFramework/HUD.h"
#include "WeaveHUD.generated.h"
UCLASS()
class RIFTWEAVE_API AWeaveHUD : public AHUD
{
    GENERATED_BODY()
public:
    UPROPERTY(EditDefaultsOnly,Category="UI") TSubclassOf<UUserWidget> StabilityWidgetClass;
    UPROPERTY(EditDefaultsOnly,Category="UI") TSubclassOf<UUserWidget> AnchorWidgetClass;
    virtual void BeginPlay() override;
    UFUNCTION(BlueprintCallable) void ShowWeaveHint(FText Hint);
};
