#pragma once
#include "CoreMinimal.h"
#include "MassEntityTypes.h"
#include "MassWeaverAI.generated.h"
USTRUCT() struct FFragment_FrostElk : public FMassFragment { GENERATED_BODY() FVector Velocity; float Panic=0.f; };
USTRUCT() struct FFragment_ForgeDrone : public FMassFragment { GENERATED_BODY() FVector Target; bool bCarryingHeat=false; };
USTRUCT() struct FFragment_CanopySprite : public FMassFragment { GENERATED_BODY() float GlowPhase=0.f; };
USTRUCT() struct FTag_InRift : public FMassTag { GENERATED_BODY() };
