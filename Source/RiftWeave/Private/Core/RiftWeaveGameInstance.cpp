#include "Core/RiftWeaveGameInstance.h"
void URiftWeaveGameInstance::Init(){ Super::Init(); UE_LOG(LogTemp,Log,TEXT("[GI] RiftWeave init")); }
void URiftWeaveGameInstance::Shutdown(){ Super::Shutdown(); }
void URiftWeaveGameInstance::CreateCoopSession(int32 MaxPlayers){ UE_LOG(LogTemp,Log,TEXT("[GI] Create session %d"),MaxPlayers); }
void URiftWeaveGameInstance::JoinSession(const FString& Code){ LastJoinCode=Code; UE_LOG(LogTemp,Log,TEXT("[GI] Join %s"),*Code); }
