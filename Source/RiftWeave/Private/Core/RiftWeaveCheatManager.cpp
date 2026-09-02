#include "Core/RiftWeaveCheatManager.h"
void URiftWeaveCheatManager::RiftWeave_GodWeave(){ UE_LOG(LogTemp,Log,TEXT("[Cheat] GodWeave")); }
void URiftWeaveCheatManager::RiftWeave_TeleportBiome(FString B){ UE_LOG(LogTemp,Log,TEXT("[Cheat] Teleport %s"),*B); }
void URiftWeaveCheatManager::RiftWeave_SpawnRift(FString R){ UE_LOG(LogTemp,Log,TEXT("[Cheat] Spawn %s"),*R); }
void URiftWeaveCheatManager::RiftWeave_SetStability(float S){ UE_LOG(LogTemp,Log,TEXT("[Cheat] Stability %.2f"),S); }
