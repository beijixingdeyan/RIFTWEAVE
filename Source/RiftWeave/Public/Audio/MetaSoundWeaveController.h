#pragma once
#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "MetaSoundWeaveController.generated.h"
class UMetaSoundSource;
UCLASS(ClassGroup=(Audio), meta=(BlueprintSpawnableComponent))
class RIFTWEAVE_API UMetaSoundWeaveController : public UActorComponent
{
    GENERATED_BODY()
public:
    UMetaSoundWeaveController();
    UPROPERTY(EditAnywhere,Category="Audio") TObjectPtr<UMetaSoundSource> LoomSource;
    UFUNCTION(BlueprintCallable) void SetStability(float S);
    UFUNCTION(BlueprintCallable) void SetBiomeBlend(FName A,FName B,float Alpha);
    UFUNCTION(BlueprintCallable) void TriggerWeaveEvent(FName EventId);
protected:
    virtual void BeginPlay() override;
    UPROPERTY() TObjectPtr<UAudioComponent> AudioComp;
};
