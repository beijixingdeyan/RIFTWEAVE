#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "RiftWeaveCharacter.generated.h"

class UWeaveComponent;
class UDimensionAnchorComponent;
class UMotionWarpingComponent;

/// The Weaver — 3-button core: Weave / Anchor / Interact. MotionWarping + ControlRig feet.
UCLASS()
class RIFTWEAVE_API ARiftWeaveCharacter : public ACharacter
{
    GENERATED_BODY()
public:
    ARiftWeaveCharacter(const FObjectInitializer& ObjectInitializer);

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Weaver") TObjectPtr<UWeaveComponent> WeaveComp;
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Weaver") TObjectPtr<UDimensionAnchorComponent> AnchorComp;
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Animation") TObjectPtr<UMotionWarpingComponent> WarpingComp;

    UPROPERTY(EditDefaultsOnly, Category="Weaver") float WeaveReach = 2500.f;

    UFUNCTION(BlueprintCallable, Category="Weaver") void RequestWeave(const FVector& Start, const FVector& End);
    UFUNCTION(BlueprintCallable, Category="Weaver") void PlaceAnchor(const FVector& Location);
protected:
    virtual void SetupPlayerInputComponent(UInputComponent* PlayerInputComponent) override;
};
