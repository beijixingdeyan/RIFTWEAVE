#pragma once
#include "CoreMinimal.h"
#include "World/WorldPartitionHelper.h"
#include "WorldPartitionHelperEx.generated.h"
/// Extended WP helper: DataLayer streaming, HLOD validation, RVT volume, PCG rebuild triggers.
UCLASS()
class RIFTWEAVE_API UWorldPartitionHelperEx : public UWorldPartitionHelper
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable, Category="World") static void ValidateHLOD();
    UFUNCTION(BlueprintCallable, Category="World") static void RebuildPCGAt(FVector Loc, float Radius);
};
