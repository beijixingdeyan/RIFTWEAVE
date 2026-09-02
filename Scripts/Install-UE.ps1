param(
    [string]$EngineVersion = "5.4",
    [string]$InstallPath = "",
    [switch]$SourceBuild,
    [switch]$SkipLauncher
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path $PSScriptRoot -Parent
if (-not $InstallPath) { $InstallPath = Join-Path $ProjectRoot "Engine\UE_5.4" }
$EngineDir = Split-Path $InstallPath -Parent
$LauncherUrl = "https://epicgames-download1.akamaized.net/Builds/UnrealEngineLauncher/Installers/Windows/EpicInstaller-20.1.4.msi"
$LauncherMsi = Join-Path $EngineDir "EpicInstaller-20.1.4.msi"

Write-Host "=== RIFTWEAVE — Install UE $EngineVersion to $InstallPath ===" -ForegroundColor Cyan
Write-Host "Disk free E: $([math]::Round((Get-PSDrive E).Free/1GB,1)) GB (need ~40 GB binary, ~80 GB source)" -ForegroundColor White

New-Item -ItemType Directory -Force -Path $EngineDir | Out-Null
Set-Content -Path (Join-Path $EngineDir ".gitkeep") -Value "" -Force

# 1. Download Epic Installer MSI to working directory (gitignored)
if (-not (Test-Path $LauncherMsi)) {
    Write-Host "[1/4] Downloading Epic Installer to $LauncherMsi ..." -ForegroundColor Yellow
    try {
        # Try curl -k (bypass revocation issue seen on this host)
        $curl = Get-Command curl.exe -ErrorAction SilentlyContinue
        if ($curl) {
            & curl.exe -k -L -o $LauncherMsi $LauncherUrl
            if ($LASTEXITCODE -ne 0 -or -not (Test-Path $LauncherMsi)) { throw "curl failed" }
        } else {
            # Fallback: BITS (more tolerant)
            Import-Module BitsTransfer -ErrorAction SilentlyContinue
            Start-BitsTransfer -Source $LauncherUrl -Destination $LauncherMsi -ErrorAction Stop
        }
        Write-Host "  -> Downloaded $([math]::Round((Get-Item $LauncherMsi).Length/1MB,1)) MB" -ForegroundColor Green
    } catch {
        Write-Host "  !! Download failed: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "  Manual: open $LauncherUrl in browser and save to $LauncherMsi" -ForegroundColor Yellow
    }
} else {
    Write-Host "[1/4] Launcher MSI already at $LauncherMsi ($([math]::Round((Get-Item $LauncherMsi).Length/1MB,1)) MB)" -ForegroundColor Green
}

# 2. Install / locate Epic Games Launcher
if (-not $SkipLauncher) {
    $launcherExe = "C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe"
    $installed = Test-Path $launcherExe
    if (-not $installed) {
        Write-Host "[2/4] Installing Epic Games Launcher (winget) ..." -ForegroundColor Yellow
        try {
            winget install --id EpicGames.EpicGamesLauncher --accept-package-agreements --accept-source-agreements --silent --disable-interactivity 2>&1 | Out-String | Write-Host
            Start-Sleep -Seconds 5
            $installed = Test-Path $launcherExe
        } catch { Write-Host "  winget install error: $($_.Exception.Message)" -ForegroundColor Yellow }
        if (-not $installed -and (Test-Path $LauncherMsi)) {
            Write-Host "  Trying MSI install ..." -ForegroundColor Yellow
            Start-Process msiexec.exe -ArgumentList "/i `"$LauncherMsi`" /qn /norestart" -Wait
            Start-Sleep -Seconds 10
            $installed = Test-Path $launcherExe
        }
    }
    if ($installed) { Write-Host "[2/4] Launcher found: $launcherExe" -ForegroundColor Green }
    else { Write-Host "[2/4] Launcher not yet installed — you can run $LauncherMsi manually" -ForegroundColor Yellow }
} else { Write-Host "[2/4] SkipLauncher — skipping Epic Launcher install" -ForegroundColor Yellow }

# 3. Download Unreal Engine binary to working directory
Write-Host "[3/4] Unreal Engine $EngineVersion -> $InstallPath" -ForegroundColor Yellow
if (Test-Path "$InstallPath\Engine\Binaries\Win64\UnrealEditor.exe") {
    Write-Host "  Already installed at $InstallPath" -ForegroundColor Green
} else {
    Write-Host "  To download UE $EngineVersion into this folder, use ONE of:" -ForegroundColor White
    Write-Host "" 
    Write-Host "  A) Epic Launcher (recommended, GUI):" -ForegroundColor Cyan
    Write-Host "     1. Launch Epic Games Launcher (log in with Epic account)" -ForegroundColor White
    Write-Host "     2. Unreal Engine -> Library -> Engine Versions -> + -> $EngineVersion" -ForegroundColor White
    Write-Host "     3. Click Browse and select: $InstallPath" -ForegroundColor White
    Write-Host "     4. Install (35-40 GB, 20-60 min depending on network)" -ForegroundColor White
    Write-Host ""
    Write-Host "  B) Source build (for developers, ~80 GB, gitignored):" -ForegroundColor Cyan
    Write-Host "     git clone --depth 1 https://github.com/EpicGames/UnrealEngine.git `"$EngineDir\UnrealEngine`"" -ForegroundColor White
    Write-Host "     # (requires Epic-linked GitHub account, then:)" -ForegroundColor Gray
    Write-Host "     `"$EngineDir\UnrealEngine\Setup.bat`" ; `"$EngineDir\UnrealEngine\GenerateProjectFiles.bat`"" -ForegroundColor White
    Write-Host ""
    if ($SourceBuild) {
        Write-Host "  SourceBuild flag set — attempting git clone ..." -ForegroundColor Yellow
        $env:GIT_SSL_NO_VERIFY = "1"
        $unrealSrc = Join-Path $EngineDir "UnrealEngine"
        if (-not (Test-Path $unrealSrc)) {
            git clone --depth 1 https://github.com/EpicGames/UnrealEngine.git $unrealSrc 2>&1 | Write-Host
        }
        if (Test-Path "$unrealSrc\Setup.bat") {
            Write-Host "  Running Setup.bat (downloads ~15 GB dependencies) ..." -ForegroundColor Yellow
            Push-Location $unrealSrc
            & .\Setup.bat 2>&1 | Tee-Object -FilePath "$EngineDir\Setup.log"
            & .\GenerateProjectFiles.bat 2>&1 | Tee-Object -FilePath "$EngineDir\Generate.log"
            Pop-Location
        }
    }
    Write-Host ""
    Write-Host "  After install, verify:" -ForegroundColor White
    Write-Host "    dir `"$InstallPath\Engine\Binaries\Win64\UnrealEditor.exe`"" -ForegroundColor Gray
    Write-Host "    .\Scripts\Build.ps1 -Target Editor" -ForegroundColor Gray
}

# 4. Update EngineAssociation in .uproject to local Engine if installed
$uproject = Join-Path $ProjectRoot "RiftWeave.uproject"
if ((Test-Path "$InstallPath\Engine\Binaries\Win64\UnrealEditor.exe") -and (Test-Path $uproject)) {
    Write-Host "[4/4] Local Engine detected — .uproject will auto-detect EngineAssociation 5.4" -ForegroundColor Green
    Write-Host "  Tip: Right-click RiftWeave.uproject -> Switch Unreal Engine version -> select $InstallPath" -ForegroundColor White
}

Write-Host "=== Install script done ===" -ForegroundColor Green
Write-Host "Engine folder is gitignored (Engine/ in .gitignore) — GitHub push will NOT include 30-60 GB binaries." -ForegroundColor Cyan
Write-Host "Next: Launch Epic Games Launcher and install UE $EngineVersion to $InstallPath (or re-run with -SourceBuild)" -ForegroundColor White
