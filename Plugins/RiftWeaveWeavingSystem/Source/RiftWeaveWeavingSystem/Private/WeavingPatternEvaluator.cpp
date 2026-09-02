#include "WeavingPatternEvaluator.h"
float UWeavingPatternEvaluator::EvaluateStability(float Speed,float Angle,int32 Anchors){ float s=1.f - FMath::Clamp(Speed/2000.f,0.f,0.4f) - FMath::Clamp(Angle/90.f,0.f,0.3f); s+=Anchors*0.08f; return FMath::Clamp(s,0.f,1.f); }
FName UWeavingPatternEvaluator::SuggestPattern(const TArray<FName>& Tags){ if(Tags.Contains("Obsidian")&&Tags.Contains("Frostvein")) return "HotSpring"; return "BasicStitch"; }
