#include "Core/RiftWeaveGameState.h"
#include "Net/UnrealNetwork.h"
void ARiftWeaveGameState::OnRep_BiomeBlend(){ UE_LOG(LogTemp,Log,TEXT("[GS] Biome blend updated")); }
void ARiftWeaveGameState::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const { Super::GetLifetimeReplicatedProps(Out); DOREPLIFETIME(ARiftWeaveGameState,BiomeBlendRatios); DOREPLIFETIME(ARiftWeaveGameState,ActiveRiftIds); DOREPLIFETIME(ARiftWeaveGameState,GlobalWeaveStability); }
