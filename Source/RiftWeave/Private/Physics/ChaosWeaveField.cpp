#include "Physics/ChaosWeaveField.h"
FFieldSystemCommand UChaosWeaveField::MakeTearField(FVector O,float R,float M){ return FFieldSystemCommand("Tear",nullptr); }
FFieldSystemCommand UChaosWeaveField::MakeStitchField(FVector A,FVector B,float Alpha){ return FFieldSystemCommand("Stitch",nullptr); }
FFieldSystemCommand UChaosWeaveField::MakeAnchorStrainField(FVector P,float S){ return FFieldSystemCommand("AnchorStrain",nullptr); }
