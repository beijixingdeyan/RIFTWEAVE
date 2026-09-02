#pragma once
#include "CoreMinimal.h"
#include "PCG/PCGGraph.h"
#include "PCGRiftGraph.generated.h"
/// PCG graph wrapper for Rift cracks: SurfaceSampler -> Noise -> Prune -> Spawner
/// Exposed to designers via DataAsset. HLOD-aware, culls at 80m.
UCLASS(BlueprintType)
class RIFTWEAVE_API UPCGRiftGraph : public UPCGGraph
{
    GENERATED_BODY()
public:
    UPROPERTY(EditAnywhere, Category="PCG") float CrackDensity=4000.f;
    UPROPERTY(EditAnywhere, Category="PCG") float CullingDistance=8000.f;
    UFUNCTION(BlueprintCallable) void RebuildAt(FVector Center, float Radius);
};
