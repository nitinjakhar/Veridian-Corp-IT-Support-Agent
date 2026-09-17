# PowerShell script to run the Veridian IT Support Agent Backend
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  Starting Veridian IT Support Agent - Backend    " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

Set-Location -Path "$PSScriptRoot\backend"

if (-not (Test-Path "venv")) {
    Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

Write-Host "Installing/Verifying dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt --quiet

Write-Host "Ensuring database seed..." -ForegroundColor Yellow
python -m app.database.seed

Write-Host "Starting FastAPI server at http://127.0.0.1:8000 ..." -ForegroundColor Green
Write-Host "Swagger Docs available at: http://127.0.0.1:8000/docs" -ForegroundColor Green
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
