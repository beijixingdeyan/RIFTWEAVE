#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "RiftPuzzleActor.generated.h"
class UBoxComponent;
UCLASS()
class RIFTWEAVE_API ARiftPuzzleActor : public AActor
{
    GENERATED_BODY()
public:
    ARiftPuzzleActor();
    UPROPERTY(EditAnywhere,Category="Puzzle") FName PuzzleId;
    UPROPERTY(EditAnywhere,Category="Puzzle") int32 RequiredAnchors=2;
    UPROPERTY(EditAnywhere,Category="Puzzle") TArray<FName> RequiredPatterns;
    UPROPERTY(ReplicatedUsing=OnRep_Solved,BlueprintReadOnly,Category="Puzzle") bool bSolved=false;
    UFUNCTION(BlueprintCallable) void TrySolve(const TArray<FVector>& AnchorPositions);
    UFUNCTION() void OnRep_Solved();
    UPROPERTY(BlueprintAssignable) FSimpleMulticastDelegate OnSolved;
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const override;
protected:
    UPROPERTY(VisibleAnywhere) TObjectPtr<UBoxComponent> TriggerBox;
};
