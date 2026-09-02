#pragma once
#include "CoreMinimal.h"
#include "Subsystems/GameInstanceSubsystem.h"
#include "PhotoModeSubsystem.generated.h"
UCLASS()
class RIFTWEAVE_API UPhotoModeSubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void EnterPhotoMode();
    UFUNCTION(BlueprintCallable) void ExitPhotoMode();
    UFUNCTION(BlueprintCallable) void CapturePhoto(FString Filename);
    UFUNCTION(BlueprintPure) bool IsInPhotoMode() const { return bActive; }
    UPROPERTY(BlueprintAssignable) FSimpleMulticastDelegate OnPhotoTaken;
private:
    bool bActive=false;
};
