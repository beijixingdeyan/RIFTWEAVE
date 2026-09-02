using UnrealBuildTool;
public class RiftWeaveEditorTarget : TargetRules {
    public RiftWeaveEditorTarget(TargetInfo Target):base(Target){
        Type=TargetType.Editor;
        DefaultBuildSettings=BuildSettingsVersion.V5;
        IncludeOrderVersion=EngineIncludeOrderVersion.Latest;
        ExtraModuleNames.AddRange(new[]{"RiftWeave"});
    }
}
