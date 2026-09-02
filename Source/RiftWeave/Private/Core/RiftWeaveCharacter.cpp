#include "Core/RiftWeaveCharacter.h"
#include "Weaving/WeaveComponent.h"
#include "Weaving/DimensionAnchorComponent.h"
#include "MotionWarpingComponent.h"
#include "GameFramework/CharacterMovementComponent.h"
ARiftWeaveCharacter::ARiftWeaveCharacter(const FObjectInitializer& OI):Super(OI){
    WeaveComp=CreateDefaultSubobject<UWeaveComponent>("WeaveComp");
    AnchorComp=CreateDefaultSubobject<UDimensionAnchorComponent>("AnchorComp");
    WarpingComp=CreateDefaultSubobject<UMotionWarpingComponent>("WarpingComp");
    GetCharacterMovement()->MaxWalkSpeed=520.f; GetCharacterMovement()->JumpZVelocity=650.f;
}
void ARiftWeaveCharacter::SetupPlayerInputComponent(UInputComponent* PIC){ Super::SetupPlayerInputComponent(PIC); }
void ARiftWeaveCharacter::RequestWeave(const FVector& S,const FVector& E){ if(WeaveComp) WeaveComp->Server_BeginTear(S,(E-S).GetSafeNormal()); }
void ARiftWeaveCharacter::PlaceAnchor(const FVector& Loc){ if(AnchorComp) AnchorComp->Server_PlaceAnchor(Loc); }
