#include "Audio/MetaSoundWeaveController.h"
#include "Components/AudioComponent.h"
UMetaSoundWeaveController::UMetaSoundWeaveController(){ PrimaryComponentTick.bCanEverTick=false; }
void UMetaSoundWeaveController::BeginPlay(){ Super::BeginPlay(); AudioComp=NewObject<UAudioComponent>(this); if(AudioComp) AudioComp->RegisterComponent(); }
void UMetaSoundWeaveController::SetStability(float S){ if(AudioComp) AudioComp->SetFloatParameter("Stability",S); }
void UMetaSoundWeaveController::SetBiomeBlend(FName A,FName B,float Alpha){ if(AudioComp){ AudioComp->SetFloatParameter("BiomeBlend",Alpha); } }
void UMetaSoundWeaveController::TriggerWeaveEvent(FName E){ if(AudioComp) AudioComp->SetTriggerParameter(E); }
