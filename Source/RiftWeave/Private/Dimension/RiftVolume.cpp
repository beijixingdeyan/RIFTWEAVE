#include "Dimension/RiftVolume.h"
ARiftVolume::ARiftVolume(){}
float ARiftVolume::GetBlendAtLocation(FVector Loc) const { if(!BlendCurve) return 0.5f; float d=FVector::Dist(Loc,GetActorLocation())/2000.f; return BlendCurve->GetFloatValue(FMath::Clamp(d,0.f,1.f)); }
