#pragma once
#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "WeaveComponent.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnWeaveStateChanged, FName, RiftId, float, Stability);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnWeaveCompleted, FName, RiftId);

/// Core mechanic: tear → drag → stitch. Server-authoritative, Chaos field driven.
UCLASS(ClassGroup=(Weaving), meta=(BlueprintSpawnableComponent))
class RIFTWEAVE_API UWeaveComponent : public UActorComponent
{
    GENERATED_BODY()
public:
    UWeaveComponent();

    UPROPERTY(EditDefaultsOnly, Category="Weave") float TearDuration = 0.6f;
    UPROPERTY(EditDefaultsOnly, Category="Weave") float DragSpringStiffness = 1800.f;
    UPROPERTY(EditDefaultsOnly, Category="Weave") float MaxStitchDistance = 3000.f;

    UPROPERTY(BlueprintAssignable) FOnWeaveStateChanged OnWeaveStateChanged;
    UPROPERTY(BlueprintAssignable) FOnWeaveCompleted OnWeaveCompleted;

    UFUNCTION(BlueprintCallable, Server, Reliable) void Server_BeginTear(const FVector& Start, const FVector& Normal);
    UFUNCTION(BlueprintCallable, Server, Reliable) void Server_UpdateDrag(const FVector& TargetPos);
    UFUNCTION(BlueprintCallable, Server, Reliable) void Server_EndWeave(const FVector& End);

    UFUNCTION(BlueprintPure) bool IsWeaving() const { return bIsWeaving; }
    UFUNCTION(BlueprintPure) float GetStability() const { return Stability; }

protected:
    UPROPERTY(ReplicatedUsing=OnRep_Stability) float Stability = 1.f;
    UPROPERTY(Replicated) bool bIsWeaving = false;
    UFUNCTION() void OnRep_Stability();

    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
    virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;
};
