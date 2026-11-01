@echo off
title ISL Interpreter

echo Starting ISL Interpreter Backend...
start "ISL Backend" cmd /k "cd /d ""%~dp0backend"" && ""%~dp0.venv\Scripts\python.exe"" -m uvicorn main:app --reload"

timeout /t 3 /nobreak >nul

echo Starting ISL Interpreter Frontend...

start "ISL Frontend" cmd /k "cd /d ""%~dp0frontend"" && ""%~dp0.venv\Scripts\python.exe"" app.py"

echo.
echo Startup commands launched.
echo Backend: http://127.0.0.1:8000
echo Check the frontend terminal for its URL.
pause

