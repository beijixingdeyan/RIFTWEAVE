#pragma once
#include "CoreMinimal.h"
#include "StateTreeTaskBase.h"
#include "WeaveTasks.generated.h"
// StateTree tasks for MassAI and companion
USTRUCT()
struct FWeaveStateTreeTask_Anchor : public FStateTreeTaskCommonBase
{
    GENERATED_BODY()
    UPROPERTY(EditAnywhere, Category="Weave") FVector AnchorLocation;
    UPROPERTY(EditAnywhere, Category="Weave") float Tolerance=50.f;
    virtual EStateTreeRunStatus Tick(FStateTreeExecutionContext& Context, const float DeltaTime) override;
};
USTRUCT()
struct FWeaveStateTreeTask_FollowWeaver : public FStateTreeTaskCommonBase
{
    GENERATED_BODY()
    UPROPERTY(EditAnywhere, Category="AI") float FollowDistance=300.f;
    virtual EStateTreeRunStatus Tick(FStateTreeExecutionContext& Context, const float DeltaTime) override;
};
USTRUCT()
struct FWeaveStateTreeEvaluator_BiomeBlend : public FStateTreeEvaluatorCommonBase
{
    GENERATED_BODY()
    UPROPERTY(EditAnywhere, Category="Eval") float BlendThreshold=0.5f;
    virtual void Tick(FStateTreeExecutionContext& Context, const float DeltaTime) override;
};
