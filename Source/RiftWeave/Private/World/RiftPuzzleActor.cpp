#include "World/RiftPuzzleActor.h"
#include "Components/BoxComponent.h"
#include "Net/UnrealNetwork.h"
ARiftPuzzleActor::ARiftPuzzleActor(){ bReplicates=true; TriggerBox=CreateDefaultSubobject<UBoxComponent>("Trigger"); RootComponent=TriggerBox; }
void ARiftPuzzleActor::TrySolve(const TArray<FVector>& Anchors){ if((int32)Anchors.Num()>=RequiredAnchors && !bSolved){ bSolved=true; OnSolved.Broadcast(); OnRep_Solved(); } }
void ARiftPuzzleActor::OnRep_Solved(){ UE_LOG(LogTemp,Log,TEXT("[Puzzle] %s solved"),*PuzzleId.ToString()); }
void ARiftPuzzleActor::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(ARiftPuzzleActor,bSolved); }
