# PowerShell script to launch both Backend and Frontend in separate windows
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  Launching Veridian IT Support Agent System      " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

Start-Process powershell -ArgumentList "-NoExit", "-File", "$PSScriptRoot\run_backend.ps1"
Start-Sleep -Seconds 2
Start-Process powershell -ArgumentList "-NoExit", "-File", "$PSScriptRoot\run_frontend.ps1"

Write-Host "Both Backend and Frontend have been launched in separate terminal windows." -ForegroundColor Green
Write-Host "Frontend:    http://localhost:5173" -ForegroundColor Green
Write-Host "Backend API: http://127.0.0.1:8000" -ForegroundColor Green
Write-Host "API Docs:    http://127.0.0.1:8000/docs" -ForegroundColor Green
