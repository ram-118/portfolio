param(
  [int]$Port = 5500
)

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

$targetUrl = "http://localhost:$Port/amaresam_portfolio_v4.html"
Write-Host "Serving portfolio from: $projectRoot"
Write-Host "Open: $targetUrl"
Write-Host "Press Ctrl+C to stop the server."

Start-Process $targetUrl | Out-Null

if (Get-Command py -ErrorAction SilentlyContinue) {
  py -m http.server $Port
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
  python -m http.server $Port
} else {
  Write-Error "Python is not available. Install Python or run with Node.js static server."
}
