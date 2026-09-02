#include "World/BiomeManager.h"
void UBiomeManager::LoadBiome(EBiomeId B){ LoadedBiomes.Add(B); UE_LOG(LogTemp,Log,TEXT("[Biome] Load %d"),(int32)B); }
void UBiomeManager::UnloadBiome(EBiomeId B){ LoadedBiomes.Remove(B); }
bool UBiomeManager::IsBiomeLoaded(EBiomeId B) const { return LoadedBiomes.Contains(B); }
void UBiomeManager::SetBiomeBlend(EBiomeId A, EBiomeId B, float Alpha){ OnBiomeBlend.Broadcast(A,B,Alpha); }
