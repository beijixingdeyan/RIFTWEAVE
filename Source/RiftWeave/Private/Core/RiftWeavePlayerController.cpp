#include "Core/RiftWeavePlayerController.h"
#include "EnhancedInputComponent.h"
#include "EnhancedInputSubsystems.h"
ARiftWeavePlayerController::ARiftWeavePlayerController(){ bShowMouseCursor=false; }
void ARiftWeavePlayerController::BeginPlay(){
    Super::BeginPlay();
    if(auto* Sub=ULocalPlayer::GetSubsystem<UEnhancedInputLocalPlayerSubsystem>(GetLocalPlayer())){
        if(WeaverMappingContext) Sub->AddMappingContext(WeaverMappingContext,0);
    }
}
void ARiftWeavePlayerController::SetupInputComponent(){
    Super::SetupInputComponent();
    if(auto* EIC=Cast<UEnhancedInputComponent>(InputComponent)){
        if(IA_Weave){ EIC->BindAction(IA_Weave,ETriggerEvent::Started,this,&ARiftWeavePlayerController::OnWeaveStarted); EIC->BindAction(IA_Weave,ETriggerEvent::Completed,this,&ARiftWeavePlayerController::OnWeaveCompleted); }
        if(IA_Anchor) EIC->BindAction(IA_Anchor,ETriggerEvent::Triggered,this,&ARiftWeavePlayerController::OnAnchor);
    }
}
void ARiftWeavePlayerController::OnWeaveStarted(const FInputActionValue& V){ UE_LOG(LogTemp,Verbose,TEXT("[PC] Weave start")); }
void ARiftWeavePlayerController::OnWeaveCompleted(const FInputActionValue& V){ UE_LOG(LogTemp,Verbose,TEXT("[PC] Weave end")); }
void ARiftWeavePlayerController::OnAnchor(const FInputActionValue& V){}
void ARiftWeavePlayerController::TogglePhotoMode(){}
void ARiftWeavePlayerController::RequestRemap(FName A){}
