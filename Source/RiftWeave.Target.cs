using UnrealBuildTool;
public class RiftWeaveTarget : TargetRules {
    public RiftWeaveTarget(TargetInfo Target):base(Target){
        Type=TargetType.Game;
        DefaultBuildSettings=BuildSettingsVersion.V5;
        IncludeOrderVersion=EngineIncludeOrderVersion.Latest;
        ExtraModuleNames.AddRange(new[]{"RiftWeave"});
    }
}
