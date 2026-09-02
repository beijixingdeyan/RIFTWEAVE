#pragma once
#include "CoreMinimal.h"
#include "Subsystems/GameInstanceSubsystem.h"
#include "AccessibilitySubsystem.generated.h"
UENUM(BlueprintType) enum class EColorBlindMode : uint8 { None, Deuteranopia, Protanopia, Tritanopia };
/// Accessibility: remap, single-stick, color-blind, high-contrast, subtitles, haptics, FOV, hold-to-toggle.
UCLASS()
class RIFTWEAVE_API UAccessibilitySubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void SetColorBlindMode(EColorBlindMode Mode);
    UFUNCTION(BlueprintCallable) void SetSingleStick(bool bEnabled);
    UFUNCTION(BlueprintCallable) void SetHighContrast(bool bEnabled);
    UFUNCTION(BlueprintCallable) void SetHoldToWeave(bool bHold);
    UFUNCTION(BlueprintCallable) void SetSubtitleScale(float Scale);
    UPROPERTY(BlueprintReadOnly, Category="A11y") EColorBlindMode CurrentMode=EColorBlindMode::None;
    UPROPERTY(BlueprintAssignable) FOnColorBlindChanged OnColorBlindChanged;
    DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnColorBlindChanged, EColorBlindMode, Mode);
};
