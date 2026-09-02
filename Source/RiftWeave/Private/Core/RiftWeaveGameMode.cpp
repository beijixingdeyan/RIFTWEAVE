#include "Core/RiftWeaveGameMode.h"
#include "Core/RiftWeaveGameState.h"
#include "Core/RiftWeavePlayerState.h"
#include "GameFramework/PlayerController.h"

ARiftWeaveGameMode::ARiftWeaveGameMode()
{
    GameStateClass = ARiftWeaveGameState::StaticClass();
    PlayerStateClass = ARiftWeavePlayerState::StaticClass();
}

void ARiftWeaveGameMode::PostLogin(APlayerController* NewPlayer)
{
    Super::PostLogin(NewPlayer);
    UE_LOG(LogTemp, Log, TEXT("[GameMode] Player joined: %s"), *GetNameSafe(NewPlayer));
}

void ARiftWeaveGameMode::HandleStartingNewPlayer_Implementation(APlayerController* NewPlayer)
{
    Super::HandleStartingNewPlayer_Implementation(NewPlayer);
}

void ARiftWeaveGameMode::HostRiftSession(FName RiftId)
{
    UE_LOG(LogTemp, Log, TEXT("[GameMode] Hosting rift %s"), *RiftId.ToString());
}
