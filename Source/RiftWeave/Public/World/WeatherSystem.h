#pragma once
#include "CoreMinimal.h"
#include "Subsystems/WorldSubsystem.h"
#include "WeatherSystem.generated.h"
UENUM(BlueprintType) enum class EWeatherType : uint8 { Clear, AshFall, SnowStorm, SporeRain, Aurora };
UCLASS()
class RIFTWEAVE_API UWeatherSystem : public UWorldSubsystem
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintCallable) void SetWeather(EWeatherType Type, float TransitionTime=2.f);
    UFUNCTION(BlueprintPure) EWeatherType GetWeather() const { return Current; }
    UPROPERTY(BlueprintAssignable) FOnWeatherChanged OnWeatherChanged;
    DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnWeatherChanged, EWeatherType, NewWeather, float, Intensity);
private:
    UPROPERTY() EWeatherType Current=EWeatherType::Clear;
};
