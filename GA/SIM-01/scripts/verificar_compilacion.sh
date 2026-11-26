#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
command -v pdflatex >/dev/null
if command -v bibtex >/dev/null; then BIBTEX=bibtex; elif command -v bibtex.original >/dev/null; then BIBTEX=bibtex.original; else echo "BibTeX no disponible" >&2; exit 1; fi
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
"$BIBTEX" main >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
test -s main.pdf
if grep -Ei 'undefined references|Citation.*undefined|Reference.*undefined' main.log >/dev/null; then
  echo 'Error: referencias LaTeX sin resolver' >&2
  exit 2
fi
if grep -Ei 'overfull \\hbox|overfull \\vbox' main.log >/dev/null; then
  echo 'Advertencia: se detectaron cajas overfull; revisar maquetación' >&2
  exit 3
fi
if git rev-parse --show-toplevel >/dev/null 2>&1; then
  if git check-ignore -q main.pdf; then
    echo 'Error: .gitignore excluye main.pdf' >&2
    exit 4
  fi
fi
echo 'Compilación comprobada: main.pdf, citas resueltas, sin overfull.'
