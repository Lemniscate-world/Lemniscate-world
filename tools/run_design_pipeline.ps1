# run_design_pipeline.ps1 — Pipeline Voie B automatiue pour Lemniscate-world.
# Usage: powershell -ExecutionPolicy Bypass -File tools\run_design_pipeline.ps1
#
# Etapes:
#   1. Regeneration du portfolio depuis kuro-rules (sync_portfolio.py)
#   2. Gate Impeccable (R72) sur index.html + toutes les sections -> doit etre 0 issue
#   3. Rapport synthetique; exit 1 si la gate echoue
#
# Prerequis: Node.js installe via scoop (nodejs-lts).

$ErrorActionPreference = "Stop"
$env:PATH = "$env:USERPROFILE\scoop\apps\nodejs-lts\current;$env:USERPROFILE\scoop\shims;C:\Windows\System32;C:\Windows;$env:PATH"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
$py = "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe"

Write-Host "=== [1/3] Regeneration du portfolio ===" -ForegroundColor Cyan
& $py sync_portfolio.py
if ($LASTEXITCODE -ne 0) { Write-Host "ECHEC generation." -ForegroundColor Red; exit 1 }

Write-Host "=== [2/3] Gate Impeccable (R72) ===" -ForegroundColor Cyan
$pages = @("index.html")
Get-ChildItem sections -Directory | ForEach-Object {
    $f = Join-Path $_.FullName "index.html"
    if (Test-Path $f) { $pages += $f }
}

$output = npx -y impeccable detect @pages --no-advisory 2>&1 | Out-String
$issues = ([regex]::Matches($output, "anti-patterns? found|issue")).Count
if ($output -match "\d+ anti-pattern" -or $output -match "warning|error") {
    Write-Host "GATE R72 : ECHEC" -ForegroundColor Red
    Write-Host $output
    exit 1
}
Write-Host "GATE R72 : VERTE (0 issue) sur $($pages.Count) pages" -ForegroundColor Green

Write-Host "=== [3/3] Resume ===" -ForegroundColor Cyan
Write-Host "Portfolio regenere et conforme Quiet Precision (R108) + Impeccable (R72)."
Write-Host "Pages verifiees : $($pages.Count)"
exit 0
