@echo off
REM ============================================================
REM  Compilacion del aporte de Roselyn Andreina Sanchez Centeno
REM  Secuencia: pdflatex -> bibtex -> pdflatex -> pdflatex
REM ============================================================
setlocal

cd /d "%~dp0"

echo [1/4] Primera pasada de pdflatex...
pdflatex -interaction=nonstopmode -halt-on-error aporte_roselyn.tex
if errorlevel 1 goto :error

echo [2/4] Procesando la bibliografia con bibtex...
bibtex aporte_roselyn
if errorlevel 1 goto :error

echo [3/4] Segunda pasada de pdflatex...
pdflatex -interaction=nonstopmode -halt-on-error aporte_roselyn.tex
if errorlevel 1 goto :error

echo [4/4] Tercera pasada de pdflatex...
pdflatex -interaction=nonstopmode -halt-on-error aporte_roselyn.tex
if errorlevel 1 goto :error

echo.
echo Compilacion completada. Revise aporte_roselyn.pdf
goto :end

:error
echo.
echo Ocurrio un error durante la compilacion. Revise el archivo .log
exit /b 1

:end
endlocal
