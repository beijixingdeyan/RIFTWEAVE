#include "World/PhotoModeSubsystem.h"
#include "Kismet/GameplayStatics.h"
void UPhotoModeSubsystem::EnterPhotoMode(){ bActive=true; UGameplayStatics::SetGamePaused(GetWorld(),true); }
void UPhotoModeSubsystem::ExitPhotoMode(){ bActive=false; UGameplayStatics::SetGamePaused(GetWorld(),false); }
void UPhotoModeSubsystem::CapturePhoto(FString Fn){ OnPhotoTaken.Broadcast(); UE_LOG(LogTemp,Log,TEXT("[Photo] %s"),*Fn); }
