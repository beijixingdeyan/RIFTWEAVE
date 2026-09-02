#include "Weaving/DimensionAnchorComponent.h"
#include "Net/UnrealNetwork.h"
UDimensionAnchorComponent::UDimensionAnchorComponent(){ PrimaryComponentTick.bCanEverTick=true; SetIsReplicatedByDefault(true); }
void UDimensionAnchorComponent::Server_PlaceAnchor_Implementation(FVector Loc){ AnchorLocation=Loc; bAnchored=true; ChargeRatio=1.f; }
void UDimensionAnchorComponent::Server_ReleaseAnchor_Implementation(){ bAnchored=false; ChargeRatio=0.f; }
void UDimensionAnchorComponent::TickComponent(float DT,ELevelTick T,FActorComponentTickFunction* F){ Super::TickComponent(DT,T,F); }
void UDimensionAnchorComponent::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(UDimensionAnchorComponent,bAnchored); DOREPLIFETIME(UDimensionAnchorComponent,AnchorLocation); DOREPLIFETIME(UDimensionAnchorComponent,ChargeRatio); }
