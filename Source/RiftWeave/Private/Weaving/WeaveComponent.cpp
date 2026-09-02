#include "Weaving/WeaveComponent.h"
#include "Net/UnrealNetwork.h"
#include "Physics/ChaosWeaveField.h"
UWeaveComponent::UWeaveComponent(){ PrimaryComponentTick.bCanEverTick=true; SetIsReplicatedByDefault(true); }
void UWeaveComponent::Server_BeginTear_Implementation(const FVector& Start,const FVector& Normal){ bIsWeaving=true; Stability=1.f; OnWeaveStateChanged.Broadcast("Tear",Stability); }
void UWeaveComponent::Server_UpdateDrag_Implementation(const FVector& TargetPos){ Stability=FMath::Clamp(Stability-0.001f,0.f,1.f); }
void UWeaveComponent::Server_EndWeave_Implementation(const FVector& End){ bIsWeaving=false; OnWeaveCompleted.Broadcast("Rift_01"); }
void UWeaveComponent::OnRep_Stability(){}
void UWeaveComponent::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(UWeaveComponent,bIsWeaving); DOREPLIFETIME(UWeaveComponent,Stability); }
void UWeaveComponent::TickComponent(float DT,ELevelTick T,FActorComponentTickFunction* F){ Super::TickComponent(DT,T,F); }
