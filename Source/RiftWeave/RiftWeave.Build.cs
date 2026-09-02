using UnrealBuildTool;
public class RiftWeave : ModuleRules
{
    public RiftWeave(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
        PublicDependencyModuleNames.AddRange(new[] {
            "Core", "CoreUObject", "Engine", "InputCore", "EnhancedInput",
            "GameplayTags", "GameplayAbilities", "GameplayTasks",
            "AIModule", "StateTreeModule", "MassEntity", "MassAIBehavior", "MassGameplay",
            "Chaos", "ChaosCaching", "GeometryCollectionEngine", "FieldSystemEngine",
            "ControlRig", "MotionWarping", "Niagara", "MetasoundEngine",
            "ReplicationGraph", "IrisCore", "NetCore",
            "PCG", "CommonUI", "UMG", "Slate", "SlateCore"
        });
        PrivateDependencyModuleNames.AddRange(new[] {
            "Slate", "SlateCore", "RenderCore", "RHI", "Projects"
        });
        if (Target.bBuildEditor) {
            PrivateDependencyModuleNames.AddRange(new[] { "UnrealEd", "LevelEditor", "WorldPartitionHLODUtilities" });
        }
        PublicIncludePaths.AddRange(new[] { "RiftWeave/Public" });
        PrivateIncludePaths.AddRange(new[] { "RiftWeave/Private" });
    }
}
