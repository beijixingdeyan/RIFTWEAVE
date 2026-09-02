#pragma once
#include "CoreMinimal.h"
#include "Engine/GameInstance.h"
#include "RiftWeaveGameInstance.generated.h"
UCLASS()
class RIFTWEAVE_API URiftWeaveGameInstance : public UGameInstance
{
    GENERATED_BODY()
public:
    virtual void Init() override;
    virtual void Shutdown() override;
    UFUNCTION(BlueprintCallable) void CreateCoopSession(int32 MaxPlayers=4);
    UFUNCTION(BlueprintCallable) void JoinSession(const FString& JoinCode);
    UPROPERTY(BlueprintReadOnly, Category="Session") FString LastJoinCode;
};
