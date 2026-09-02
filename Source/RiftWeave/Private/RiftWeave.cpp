#include "RiftWeave.h"
#include "Modules/ModuleManager.h"

IMPLEMENT_PRIMARY_GAME_MODULE(FRiftWeaveModule, RiftWeave, "RiftWeave");

void FRiftWeaveModule::StartupModule()
{
    FDefaultGameModuleImpl::StartupModule();
    UE_LOG(LogTemp, Log, TEXT("[RiftWeave] Module startup — Weave the rift."));
}

void FRiftWeaveModule::ShutdownModule()
{
    FDefaultGameModuleImpl::ShutdownModule();
}
