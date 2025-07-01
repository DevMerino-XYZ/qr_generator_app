@echo off
title Generador de Codigos QR - Inicio
color 0A

echo ========================================
echo    GENERADOR DE CODIGOS QR
echo ========================================
echo.

echo Activando entorno virtual...
call venv\Scripts\activate.bat

if errorlevel 1 (
    echo ❌ Error: No se pudo activar el entorno virtual
    echo 💡 Asegurate de que el entorno virtual este creado
    echo    Ejecuta: python -m venv venv
    pause
    exit /b 1
)

echo Iniciando aplicacion...
echo.
python run.py

pause 