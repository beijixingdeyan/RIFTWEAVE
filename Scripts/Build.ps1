param(
    [ValidateSet("Editor","Game","Server")] [string]$Target = "Editor",
    [ValidateSet("Development","Shipping","DebugGame")] [string]$Config = "Development",
    [string]$UEPath = "",
    [switch]$Clean
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path $PSScriptRoot -Parent
$UProject = Join-Path $ProjectRoot "RiftWeave.uproject"

Write-Host "=== RIFTWEAVE Build ===" -ForegroundColor Cyan
Write-Host "Target: $Target  Config: $Config  Project: $UProject"

# Auto-detect UE
if (-not $UEPath) {
    $candidates = @(
        "C:\Program Files\Epic Games\UE_5.4\Engine\Build\BatchFiles\Build.bat",
        "C:\Program Files\Epic Games\UE_5.3\Engine\Build\BatchFiles\Build.bat",
        "E:\Epic\UE_5.4\Engine\Build\BatchFiles\Build.bat"
    )
    foreach ($c in $candidates) { if (Test-Path $c) { $UEPath = $c; break } }
}

if ($Clean) {
    Write-Host "[Clean] Removing Binaries/Intermediate/Saved..." -ForegroundColor Yellow
    @("Binaries","Intermediate","Saved","DerivedDataCache") | ForEach-Object {
        $p = Join-Path $ProjectRoot $_
        if (Test-Path $p) { Remove-Item $p -Recurse -Force; Write-Host "  removed $_" }
    }
}

# Generate project files if missing
if (-not (Test-Path (Join-Path $ProjectRoot "RiftWeave.sln"))) {
    Write-Host "[Setup] Generating Visual Studio project files..." -ForegroundColor Yellow
    $UBT = Join-Path (Split-Path $UEPath -Parent) "..\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.exe"
    if (Test-Path $UBT) {
        & $UBT -projectfiles -project="$UProject" -game -rocket -progress
    } else {
        Write-Host "  UBT not found, please right-click .uproject -> Generate Visual Studio project files" -ForegroundColor Yellow
    }
}

if ($UEPath -and (Test-Path $UEPath)) {
    $TargetName = if ($Target -eq "Editor") { "RiftWeaveEditor" } else { "RiftWeave" }
    $Platform = "Win64"
    Write-Host "[Build] $TargetName $Platform $Config via UBT..." -ForegroundColor Green
    & $UEPath $TargetName $Platform $Config -project="$UProject" -WaitMutex -FromMsBuild
    if ($LASTEXITCODE -ne 0) { throw "Build failed with exit $LASTEXITCODE" }
    Write-Host "=== Build succeeded ===" -ForegroundColor Green
} else {
    Write-Host "[Info] UE not found at $UEPath" -ForegroundColor Yellow
    Write-Host "  This repo is design-complete; to build:" -ForegroundColor White
    Write-Host "  1. Install UE 5.4 via Epic Launcher" -ForegroundColor White
    Write-Host "  2. Right-click RiftWeave.uproject -> Generate Visual Studio project files" -ForegroundColor White
    Write-Host "  3. Open RiftWeave.sln and build, or re-run .\Scripts\Build.ps1" -ForegroundColor White
    Write-Host "  Docs are fully readable without UE: see Documentation/" -ForegroundColor White
}

# Validate assets (optional)
if (Test-Path (Join-Path $ProjectRoot "Tools\AssetPipeline\validate_assets.py")) {
    Write-Host "[Validate] Running asset checks..." -ForegroundColor Cyan
    py (Join-Path $ProjectRoot "Tools\AssetPipeline\validate_assets.py") --quick
}
