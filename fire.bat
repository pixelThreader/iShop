@echo off
setlocal

REM Get the current directory (assumed to be the same as where manage.py is located)
set "DJANGO_PROJECT_PATH=%~dp0"

REM Open PowerShell and activate the virtual environment, then start the Django server
start powershell -NoExit -Command "& {cd '%DJANGO_PROJECT_PATH%'; .\venv\Scripts\activate; python manage.py runserver}"

REM Wait a few seconds to ensure the server starts
timeout /t 5 /nobreak > nul

REM Open the default web browser to http://localhost:8000
start http://localhost:8000

endlocal
