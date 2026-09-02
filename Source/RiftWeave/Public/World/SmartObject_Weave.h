#pragma once
#include "CoreMinimal.h"
#include "SmartObjectDefinition.h"
#include "SmartObject_Weave.generated.h"
UCLASS()
class RIFTWEAVE_API USmartObject_WeaveDefinition : public USmartObjectDefinition
{
    GENERATED_BODY()
public:
    UPROPERTY(EditAnywhere, Category="Weave") float RequiredStability=0.7f;
    UPROPERTY(EditAnywhere, Category="Weave") FName PatternId="BasicStitch";
};
