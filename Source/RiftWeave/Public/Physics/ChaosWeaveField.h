#pragma once
#include "CoreMinimal.h"
#include "Field/FieldSystemTypes.h"
#include "ChaosWeaveField.generated.h"
UCLASS()
class RIFTWEAVE_API UChaosWeaveField : public UObject
{
    GENERATED_BODY()
public:
    static FFieldSystemCommand MakeTearField(FVector Origin,float Radius,float Magnitude);
    static FFieldSystemCommand MakeStitchField(FVector A,FVector B,float BlendAlpha);
    static FFieldSystemCommand MakeAnchorStrainField(FVector AnchorPos,float Stiffness);
};
