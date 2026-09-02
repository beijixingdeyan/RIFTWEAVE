#pragma once
#include "CoreMinimal.h"
#include "Engine/DeveloperSettings.h"
#include "WeaveDeveloperSettings.generated.h"
UCLASS(Config=Game, DefaultConfig, meta=(DisplayName="RiftWeave Settings"))
class RIFTWEAVE_API UWeaveDeveloperSettings : public UDeveloperSettings
{
    GENERATED_BODY()
public:
    UPROPERTY(Config, EditAnywhere, Category="Weave") float MaxWeaveReach=4000.f;
    UPROPERTY(Config, EditAnywhere, Category="Weave") float DefaultStability=1.f;
    UPROPERTY(Config, EditAnywhere, Category="World") int32 TargetMassCount=3000;
    UPROPERTY(Config, EditAnywhere, Category="Audio") bool bEnableMetaSounds=true;
    virtual FName GetCategoryName() const override { return FName("Game"); }
};
