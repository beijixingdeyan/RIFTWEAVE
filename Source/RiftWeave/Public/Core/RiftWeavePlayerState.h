#pragma once
#include "CoreMinimal.h"
#include "GameFramework/PlayerState.h"
#include "RiftWeavePlayerState.generated.h"

UCLASS()
class RIFTWEAVE_API ARiftWeavePlayerState : public APlayerState
{
    GENERATED_BODY()
public:
    UPROPERTY(Replicated, BlueprintReadOnly, Category="Weaver")
    int32 WeavesCompleted = 0;

    UPROPERTY(Replicated, BlueprintReadOnly, Category="Weaver")
    float MasteryLevel = 0.f;

    UPROPERTY(Replicated, BlueprintReadOnly, Category="Weaver")
    TArray<FName> UnlockedPatterns;
};
