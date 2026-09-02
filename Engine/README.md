# Engine — Local Unreal Engine Installation (GitIgnored)

This folder is **not committed** (see \.gitignore\ \Engine/\).

## Purpose
User requested UE to be downloaded **into this working directory** (privacy-safe, local-only, 30-60 GB).  
This keeps the project self-contained for GitHub upload without committing binaries.

## Structure (after download)
\\\
helloworld -unrealengine/
├─ Engine/
│  ├─ UE_5.4/                 # Installed build (Epic Launcher) — Binaries/Engine/...
│  ├─ UnrealEngine/           # Source build (if cloned from EpicGames/UnrealEngine)
│  ├─ EpicInstaller-20.1.4.msi # Launcher installer (downloaded via curl -k)
│  └─ README.md               # This file
├─ RiftWeave.uproject         # EngineAssociation: 5.4 (auto-detected in Engine/UE_5.4)
\\\

## Download Status
- Launcher MSI URL: https://epicgames-download1.akamaized.net/Builds/UnrealEngineLauncher/Installers/Windows/EpicInstaller-20.1.4.msi
- Engine: UE 5.4.x (Win64, ~35 GB installed)
- Method: \Scripts/Install-UE.ps1\ (winget → Epic Launcher → UE)

## How to trigger download
\\\powershell
# One-click (creates Engine/UE_5.4):
powershell -ExecutionPolicy Bypass -File Scripts/Install-UE.ps1 -EngineVersion 5.4 -InstallPath "E:\github\dsh\projects\helloworld -unrealengine\Engine\UE_5.4"

# Or manually via Launcher:
# 1. Run Engine/EpicInstaller-20.1.4.msi
# 2. Launcher → Unreal Engine → Library → Engine Versions → + → 5.4 → Browse → select Engine/UE_5.4
\\\

## Verification
\\\powershell
dir Engine/UE_5.4/Engine/Binaries/Win64/UnrealEditor.exe
py Tools/AssetPipeline/validate_assets.py --all
.\Scripts\Build.ps1 -Target Editor
\\\

## Notes
- This folder is intentionally large and gitignored — GitHub push will NOT include it.
- To free space: delete \Engine/\ and re-run \Scripts/Install-UE.ps1\.
- Disk required: ~40 GB for binary, ~80 GB for source build.
