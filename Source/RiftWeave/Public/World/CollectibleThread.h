#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "CollectibleThread.generated.h"
UCLASS()
class RIFTWEAVE_API ACollectibleThread : public AActor
{
    GENERATED_BODY()
public:
    ACollectibleThread();
    UPROPERTY(EditAnywhere, Category="Collectible") FName ThreadId;
    UPROPERTY(EditAnywhere, Category="Collectible") int32 Value=1;
    UPROPERTY(ReplicatedUsing=OnRep_Collected, BlueprintReadOnly) bool bCollected=false;
    UFUNCTION() void OnRep_Collected();
    UFUNCTION(BlueprintCallable) void Collect(AActor* Collector);
    UPROPERTY(BlueprintAssignable) FSimpleMulticastDelegate OnCollected;
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const override;
protected:
    UPROPERTY(VisibleAnywhere) TObjectPtr<UStaticMeshComponent> Mesh;
};
