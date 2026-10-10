@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
 start "EIFFEL 404" cmd /k "py -3 -m http.server 8000"
) else (
 where python >nul 2>nul
 if errorlevel 1 (
  echo Se necesita Python 3. Instala Python o inicia un servidor local desde VS Code.
  pause
  exit /b 1
 )
 start "EIFFEL 404" cmd /k "python -m http.server 8000"
)
timeout /t 2 >nul
start "" "http://localhost:8000/"
