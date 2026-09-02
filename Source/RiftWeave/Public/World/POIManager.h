#pragma once
#include "CoreMinimal.h"
#include "Subsystems/WorldSubsystem.h"
#include "POIManager.generated.h"
USTRUCT(BlueprintType) struct FPointOfInterest { GENERATED_BODY() FName Id; FVector Location; FText Title; int32 Difficulty=1; bool bDiscovered=false; };
UCLASS()
class RIFTWEAVE_API UPOIManager : public UWorldSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void RegisterPOI(const FPointOfInterest& POI);
    UFUNCTION(BlueprintCallable) void DiscoverPOI(FName Id);
    UFUNCTION(BlueprintPure) TArray<FPointOfInterest> GetUndiscoveredInRadius(FVector Center,float Radius) const;
private:
    TArray<FPointOfInterest> POIs;
};
