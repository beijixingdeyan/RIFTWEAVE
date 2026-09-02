param([string]$UEPath = "")

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path $PSScriptRoot -Parent
Write-Host "=== RIFTWEAVE Setup ===" -ForegroundColor Cyan

# Checks
function Test-Command($cmd) { $null -ne (Get-Command $cmd -ErrorAction SilentlyContinue) }

Write-Host "[Check] Visual Studio 2022..." -NoNewline
if (Test-Path "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe") { Write-Host " OK" -ForegroundColor Green } else { Write-Host " NOT FOUND (need VS2022 + Game dev with C++)" -ForegroundColor Yellow }

Write-Host "[Check] .NET SDK..." -NoNewline
if (Test-Command dotnet) { Write-Host " $(dotnet --version)" -ForegroundColor Green } else { Write-Host " NOT FOUND" -ForegroundColor Yellow }

Write-Host "[Check] Python..." -NoNewline
if (Test-Command py) { Write-Host " $(py --version)" -ForegroundColor Green } else { Write-Host " NOT FOUND" -ForegroundColor Yellow }

Write-Host "[Check] Git LFS..." -NoNewline
if (Test-Command git) { git lfs version 2>$null; if ($LASTEXITCODE -eq 0) { Write-Host " OK" -ForegroundColor Green } else { Write-Host " install: git lfs install" -ForegroundColor Yellow } }

# UE detection
if (-not $UEPath) {
    $UEPaths = @(
        "C:\Program Files\Epic Games\UE_5.4",
        "C:\Program Files\Epic Games\UE_5.3",
        "E:\Epic\UE_5.4"
    )
    foreach ($p in $UEPaths) { if (Test-Path "$p\Engine\Binaries\Win64\UnrealEditor.exe") { $UEPath = "$p"; break } }
}
if ($UEPath) { Write-Host "[UE] Found at $UEPath" -ForegroundColor Green } else { Write-Host "[UE] Not found — docs remain readable, install UE 5.4 to open .uproject" -ForegroundColor Yellow }

# Git LFS setup
Write-Host "[Git] Configuring LFS..." -ForegroundColor Cyan
Push-Location $ProjectRoot
try {
    git lfs install 2>$null
    git lfs track "*.uasset" 2>$null
    git lfs track "*.umap" 2>$null
} catch {}
Pop-Location

Write-Host "=== Setup complete ===" -ForegroundColor Green
Write-Host "Next: .\Scripts\Build.ps1 -Target Editor" -ForegroundColor White
Write-Host "Or: Double-click RiftWeave.uproject" -ForegroundColor White
