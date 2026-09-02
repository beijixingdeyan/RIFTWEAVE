#include "Weaving/WeaveFieldSystem.h"
AWeaveFieldSystem::AWeaveFieldSystem(){}
void AWeaveFieldSystem::ApplyTearField(const FVector& Origin,float Radius,float Magnitude){ UE_LOG(LogTemp,Log,TEXT("[Field] Tear at %s r=%.0f"),*Origin.ToString(),Radius); }
void AWeaveFieldSystem::ApplyStitchField(const FVector& A,const FVector& B,float Blend){ UE_LOG(LogTemp,Log,TEXT("[Field] Stitch blend %.2f"),Blend); }
