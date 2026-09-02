#pragma once
#include "CoreMinimal.h"
#include "Subsystems/WorldSubsystem.h"
#include "DimensionStreamingSubsystem.generated.h"
UCLASS()
class RIFTWEAVE_API UDimensionStreamingSubsystem : public UWorldSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void SetDimensionAlpha(FName Dim, float Alpha);
    UFUNCTION(BlueprintPure) float GetDimensionAlpha(FName Dim) const;
private:
    TMap<FName,float> Alphas;
};
