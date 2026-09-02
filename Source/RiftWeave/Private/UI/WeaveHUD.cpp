#include "UI/WeaveHUD.h"
#include "Blueprint/UserWidget.h"
void AWeaveHUD::BeginPlay(){ Super::BeginPlay(); if(StabilityWidgetClass){ auto* W=CreateWidget<UUserWidget>(GetWorld(),StabilityWidgetClass); if(W) W->AddToViewport(); } }
void AWeaveHUD::ShowWeaveHint(FText H){ UE_LOG(LogTemp,Log,TEXT("[HUD] Hint: %s"),*H.ToString()); }
