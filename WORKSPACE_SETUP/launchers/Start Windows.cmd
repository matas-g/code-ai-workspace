@echo off
setlocal DisableDelayedExpansion
cd /d "%~dp0"
if errorlevel 1 goto location_error
rem Use installed interpreters with an adjacent Python core DLL. Skip Store aliases and manager shims.
rem -Command uses built-in PowerShell without profiles; no execution-policy change or downloaded script.
powershell.exe -NoLogo -NoProfile -Command "$paths = @(Get-Command python.exe,python3.exe -CommandType Application -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source); foreach ($root in @('HKCU:\Software\Python\PythonCore','HKLM:\Software\Python\PythonCore','HKLM:\Software\WOW6432Node\Python\PythonCore')) { foreach ($key in @(Get-ChildItem -LiteralPath $root -ErrorAction SilentlyContinue)) { $dir = (Get-ItemProperty -LiteralPath ($key.PSPath + '\InstallPath') -ErrorAction SilentlyContinue).'(default)'; if ($dir) { $paths += (Join-Path $dir 'python.exe') } } }; foreach ($p in @($paths | Select-Object -Unique)) { if ($p -match '\\WindowsApps\\' -or -not (Test-Path -LiteralPath $p -PathType Leaf)) { continue }; if (@(Get-ChildItem -LiteralPath (Split-Path -Parent $p) -Filter 'python3*.dll' -File -ErrorAction SilentlyContinue).Count -eq 0) { continue }; & $p -I -S -B -c 'import sys; sys.exit(0 if sys.version_info >= (3,9) else 1)' 2>$null; if ($LASTEXITCODE -eq 0) { Write-Host ('Using Python: ' + $p); & $p -I -S -B 'WORKSPACE_SETUP\scripts\start.py'; exit $LASTEXITCODE } }; Write-Host 'No installed Python 3.9+ interpreter found. Use an approved interpreter; nothing was installed.'; exit 2"
set "AI_SETUP_EXIT=%ERRORLEVEL%"
if "%AI_SETUP_EXIT%"=="4" exit /b 0
echo.
echo Setup exit code: %AI_SETUP_EXIT%
goto finish
:location_error
echo Could not open the launcher's directory. Nothing was created.
:finish
echo.
echo ------------------------------------------------------------
echo   Review the output above before closing.
echo   Type q or quit to close setup.
echo ------------------------------------------------------------
echo.
rem Read a literal input string in PowerShell; never interpolate it into a cmd command.
powershell.exe -NoLogo -NoProfile -Command "while ($true) { try { $answer = Read-Host '  Close setup [q/quit]' -ErrorAction Stop } catch { exit }; if ($null -eq $answer) { exit }; if ($answer.Trim() -ieq 'q' -or $answer.Trim() -ieq 'quit') { exit }; Write-Host '  Type q or quit when you are ready; the output stays here.' }"
endlocal
exit /b 0
