using UnrealBuildTool;
public class RiftWeaveWeavingSystem : ModuleRules {
    public RiftWeaveWeavingSystem(ReadOnlyTargetRules T):base(T){
        PCHUsage=PCHUsageMode.UseExplicitOrSharedPCHs;
        PublicDependencyModuleNames.AddRange(new[]{"Core","CoreUObject","Engine","Niagara","Chaos","GeometryCollectionEngine","FieldSystemEngine"});
    }
}
