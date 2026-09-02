#pragma once
#include "CoreMinimal.h"
#include "Platform/PlatformScalability.generated.h"
/// Platform scalability: PC Ultra/High, PS5 Perf, XSX/XSS. Handles Nanite Lumen Mass culling.
/// Called on startup via UWeaveDeveloperSettings + DeviceProfiles.
UCLASS()
class RIFTWEAVE_API UPlatformScalability : public UObject
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable, Category="Platform") static void ApplyForCurrentPlatform();
    UFUNCTION(BlueprintPure, Category="Platform") static FString GetPlatformName();
    UPROPERTY(EditAnywhere, Category="Scalability") float NanitePixelsPerEdge_PC=1.f;
    UPROPERTY(EditAnywhere, Category="Scalability") float NanitePixelsPerEdge_Console=2.f;
};
