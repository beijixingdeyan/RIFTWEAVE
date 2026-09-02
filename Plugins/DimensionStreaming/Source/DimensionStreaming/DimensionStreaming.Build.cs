using UnrealBuildTool;
public class DimensionStreaming : ModuleRules {
    public DimensionStreaming(ReadOnlyTargetRules T):base(T){
        PCHUsage=PCHUsageMode.UseExplicitOrSharedPCHs;
        PublicDependencyModuleNames.AddRange(new[]{"Core","CoreUObject","Engine","RenderCore"});
    }
}
