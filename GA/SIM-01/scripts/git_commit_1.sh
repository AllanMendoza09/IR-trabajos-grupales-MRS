#!/usr/bin/env bash
set -euo pipefail
repo="$(git rev-parse --show-toplevel)"
cd "$repo"
test -d GA/SIM-01
printf '\nEstado inicial de Git:\n'
git status --short
printf '\nEstado de los archivos antes de preparar el commit:\n'
git status --short -- GA/SIM-01

# Se incluyen expresamente los artefactos propios de FORM-SIM-01.
git add -- GA/SIM-01/main.tex GA/SIM-01/main.pdf GA/SIM-01/referencias.bib \
  GA/SIM-01/README.md GA/SIM-01/.gitignore \
  GA/SIM-01/secciones/00_fundamento.tex GA/SIM-01/secciones/07_uso_ia.tex \
  GA/SIM-01/secciones/08_consentimiento.tex GA/SIM-01/evidencias/MANIFIESTO.md \
  GA/SIM-01/datos/ESQUEMA.md GA/SIM-01/datos/requisitos.csv \
  GA/SIM-01/datos/moscow.csv GA/SIM-01/datos/caracteristicas_kano.csv \
  GA/SIM-01/datos/instrumento_kano.csv GA/SIM-01/datos/respuestas_kano.csv \
  GA/SIM-01/datos/votos.csv GA/SIM-01/datos/decision.csv \
  GA/SIM-01/scripts/analisis.py GA/SIM-01/scripts/autoprueba.py \
  GA/SIM-01/scripts/verificar_compilacion.sh GA/SIM-01/scripts/git_commit_1.sh
printf '\nArchivos preparados para el commit:\n'
git diff --cached --name-only
printf '\nResumen de cambios preparados:\n'
git diff --cached --stat
printf '\nRevisión exacta del commit:\n'
git diff --cached --check
printf '\nSi los cambios son de autoría comprobada, ejecutar por separado:\n'
printf '%s\n' 'git commit -m "chore(sim01): estructura GA/SIM-01, main.tex base, README y manifiesto"'
printf '%s\n' 'git status' 'git log -1 --oneline'
