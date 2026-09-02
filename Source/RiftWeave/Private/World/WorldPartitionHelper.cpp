#include "World/WorldPartitionHelper.h"
void UWorldPartitionHelper::StreamInBiome(FName L){ UE_LOG(LogTemp,Log,TEXT("[WP] StreamIn %s"),*L.ToString()); }
void UWorldPartitionHelper::StreamOutBiome(FName L){ UE_LOG(LogTemp,Log,TEXT("[WP] StreamOut %s"),*L.ToString()); }
bool UWorldPartitionHelper::IsDataLayerLoaded(FName L){ return false; }
