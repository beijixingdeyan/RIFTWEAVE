#include "World/WeatherSystem.h"
void UWeatherSystem::SetWeather(EWeatherType T,float TT){ Current=T; OnWeatherChanged.Broadcast(T,1.f); UE_LOG(LogTemp,Log,TEXT("[Weather] %d"),(int32)T); }
