#include "Dimension/DimensionManager.h"
void UDimensionManager::SetDimensionWeight(EDimensionId Dim,float W){ Weights.Add(Dim,FMath::Clamp(W,0.f,1.f)); OnBlendChanged.Broadcast(Dim,W); }
float UDimensionManager::GetDimensionWeight(EDimensionId Dim) const { const float* p=Weights.Find(Dim); return p?*p:0.f; }
void UDimensionManager::BlendTo(EDimensionId Target,float Duration){ SetDimensionWeight(Target,1.f); }
