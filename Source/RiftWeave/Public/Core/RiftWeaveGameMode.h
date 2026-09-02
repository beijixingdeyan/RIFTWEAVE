#pragma once
#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "RiftWeaveGameMode.generated.h"

class ARiftWeaveGameState;
class ARiftWeavePlayerState;

/// Authoritative game mode — 4-player co-op, Iris/ReplicationGraph aware.
UCLASS()
class RIFTWEAVE_API ARiftWeaveGameMode : public AGameModeBase
{
    GENERATED_BODY()
public:
    ARiftWeaveGameMode();

    UPROPERTY(EditDefaultsOnly, Category="RiftWeave|Session")
    int32 MaxCoopPlayers = 4;

    UPROPERTY(EditDefaultsOnly, Category="RiftWeave|Session")
    int32 MaxPlazaPlayers = 50;

    UPROPERTY(EditDefaultsOnly, Category="RiftWeave|World")
    FName StartingWorldPartitionLevel = "WP_RiftWeave";

    virtual void PostLogin(APlayerController* NewPlayer) override;
    virtual void HandleStartingNewPlayer_Implementation(APlayerController* NewPlayer) override;
    UFUNCTION(BlueprintCallable) void HostRiftSession(FName RiftId);
};
