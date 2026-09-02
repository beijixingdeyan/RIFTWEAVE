#pragma once
#include "CoreMinimal.h"
#include "Field/FieldSystemActor.h"
#include "WeaveFieldSystem.generated.h"

/// Chaos field actor spawned at tear seam — applies strain + fracture to geometry collections.
UCLASS()
class RIFTWEAVE_API AWeaveFieldSystem : public AFieldSystemActor
{
    GENERATED_BODY()
public:
    AWeaveFieldSystem();
    UFUNCTION(BlueprintCallable) void ApplyTearField(const FVector& Origin, float Radius, float Magnitude);
    UFUNCTION(BlueprintCallable) void ApplyStitchField(const FVector& A, const FVector& B, float Blend);
};
