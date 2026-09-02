#pragma once
#include "CoreMinimal.h"
#include "WeavingPatternEvaluator.generated.h"
UCLASS()
class RIFTWEAVEWEAVINGSYSTEM_API UWeavingPatternEvaluator : public UObject
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable, Category="Weaving") static float EvaluateStability(float DragSpeed,float AngleError,int32 NumAnchors);
    UFUNCTION(BlueprintCallable, Category="Weaving") static FName SuggestPattern(const TArray<FName>& BiomeTags);
};
