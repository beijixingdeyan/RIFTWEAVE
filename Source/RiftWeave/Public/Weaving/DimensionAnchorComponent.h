#pragma once
#include "CoreMinimal.h"
#include "Components/SceneComponent.h"
#include "DimensionAnchorComponent.generated.h"
UCLASS(ClassGroup=(Weaving), meta=(BlueprintSpawnableComponent))
class RIFTWEAVE_API UDimensionAnchorComponent : public USceneComponent
{
    GENERATED_BODY()
public:
    UDimensionAnchorComponent();
    UPROPERTY(EditDefaultsOnly, Category="Anchor") float MaxAnchorDistance=4000.f;
    UPROPERTY(EditDefaultsOnly, Category="Anchor") float ChargeTime=0.8f;
    UPROPERTY(Replicated, BlueprintReadOnly, Category="Anchor") bool bAnchored=false;
    UPROPERTY(Replicated, BlueprintReadOnly, Category="Anchor") FVector AnchorLocation;
    UFUNCTION(Server,Reliable,BlueprintCallable) void Server_PlaceAnchor(FVector Location);
    UFUNCTION(Server,Reliable,BlueprintCallable) void Server_ReleaseAnchor();
    UFUNCTION(BlueprintPure) bool IsCharged() const { return ChargeRatio>=1.f; }
protected:
    UPROPERTY(Replicated) float ChargeRatio=0.f;
    virtual void TickComponent(float DT,ELevelTick T,FActorComponentTickFunction* F) override;
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const override;
};
