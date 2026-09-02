#pragma once
#include "CoreMinimal.h"
#include "MassProcessor.h"
#include "WeaverCrowdProcessor.generated.h"
UCLASS()
class RIFTWEAVE_API UWeaverCrowdProcessor : public UMassProcessor
{
    GENERATED_BODY()
public:
    UWeaverCrowdProcessor();
    virtual void ConfigureQueries(const TSharedRef<FMassEntityManager>& EM) override;
    virtual void Execute(FMassEntityManager& EM, FMassExecutionContext& Ctx) override;
protected:
    FMassEntityQuery HerdQuery;
};
