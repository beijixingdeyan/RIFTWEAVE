#include "AI/AIWeaverCompanion.h"
#include "Components/StateTreeComponent.h"
AAIWeaverCompanion::AAIWeaverCompanion(){ StateTreeComp=CreateDefaultSubobject<UStateTreeComponent>("StateTree"); }
void AAIWeaverCompanion::BeginPlay(){ Super::BeginPlay(); }
void AAIWeaverCompanion::CommandAnchor(FVector L){ UE_LOG(LogTemp,Log,TEXT("[Companion] Anchor at %s"),*L.ToString()); }
void AAIWeaverCompanion::FollowPlayer(AActor* P){ UE_LOG(LogTemp,Log,TEXT("[Companion] Follow %s"),*GetNameSafe(P)); }
