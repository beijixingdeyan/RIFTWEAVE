#include "World/CollectibleThread.h"
#include "Net/UnrealNetwork.h"
ACollectibleThread::ACollectibleThread(){ bReplicates=true; Mesh=CreateDefaultSubobject<UStaticMeshComponent>("Mesh"); RootComponent=Mesh; }
void ACollectibleThread::Collect(AActor* C){ if(!bCollected){ bCollected=true; OnCollected.Broadcast(); OnRep_Collected(); } }
void ACollectibleThread::OnRep_Collected(){ Mesh->SetVisibility(false); }
void ACollectibleThread::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(ACollectibleThread,bCollected); }
