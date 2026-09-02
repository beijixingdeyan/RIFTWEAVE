#pragma once
#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

/// Main game module — registers weaving services + dimension streaming hooks.
class FRiftWeaveModule : public FDefaultGameModuleImpl
{
public:
    virtual void StartupModule() override;
    virtual void ShutdownModule() override;
    virtual bool IsGameModule() const override { return true; }
};
