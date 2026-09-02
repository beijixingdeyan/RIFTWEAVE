#pragma once
#include "CoreMinimal.h"
#include "GameFramework/CheatManager.h"
#include "RiftWeaveCheatManager.generated.h"
UCLASS()
class RIFTWEAVE_API URiftWeaveCheatManager : public UCheatManager
{
    GENERATED_BODY()
public:
    UFUNCTION(Exec) void RiftWeave_GodWeave();
    UFUNCTION(Exec) void RiftWeave_TeleportBiome(FString Biome);
    UFUNCTION(Exec) void RiftWeave_SpawnRift(FString RiftId);
    UFUNCTION(Exec) void RiftWeave_SetStability(float S);
};
