#pragma once
#include "CoreMinimal.h"
#include "GameFramework/SaveGame.h"
#include "WeaveSaveGame.generated.h"
UCLASS()
class RIFTWEAVE_API UWeaveSaveGame : public USaveGame
{
    GENERATED_BODY()
public:
    UPROPERTY(BlueprintReadWrite, Category="Save") TArray<FName> UnlockedPatterns;
    UPROPERTY(BlueprintReadWrite, Category="Save") TMap<FName,float> BestStability;
    UPROPERTY(BlueprintReadWrite, Category="Save") int32 TotalWeaves=0;
    UFUNCTION(BlueprintCallable) void AddPattern(FName Id);
};
