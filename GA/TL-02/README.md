# GA-TL-02 — Taller de entrevista estructurada y design thinking aplicado al PFC

La carpeta `GA/TL-02/` contiene las fuentes y el PDF de la actividad formativa grupal GA-TL-02 -- FORM de Ingeniería de Requerimientos (ISR-401), Unidad 2, SPA 2026–2027. El caso corresponde al proyecto de plataforma de ventas con recomendaciones basadas en IA para establecimientos eléctricos de Quevedo.

## Documento principal y herramientas

El archivo principal es `main.tex`. Utiliza la clase `IEEEtran` con las opciones `onecolumn` y `12pt` y los paquetes `inputenc` (UTF-8), `fontenc` (T1), `babel` (español), `booktabs`, `longtable`, `array`, `graphicx`, `tikz` y `hyperref` (`hidelinks`). El estilo bibliográfico es `IEEEtran`, con BibTeX.

Se requiere TeX Live 2023 o posterior, u Overleaf con compilador pdfLaTeX y procesamiento de bibliografía mediante BibTeX.

## Compilación

Desde `GA/TL-02/`, ejecutar en este orden:

```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

El documento principal incorpora los archivos de `secciones/` mediante `\IfFileExists` y `\input`. Si un archivo de sección no existe, la compilación conserva la portada, el propósito y las referencias sin producir contenido para esa sección.

## Estructura

```text
GA/TL-02/
├── main.tex
├── main.pdf
├── referencias.bib
├── README.md
├── .gitignore
├── secciones/
│   └── .gitkeep
└── evidencias/
    └── manifiesto.csv
```

La carpeta `secciones/` se conserva con `.gitkeep`; no contiene textos de las sesiones en esta versión estructural. Los archivos de sección previstos son `01_guion.tex`, `02_consentimiento.tex`, `03_ensayo.tex`, `04_empatia.tex`, `05_ajustes.tex` y `06_uso_ia.tex`.

## Distribución de responsabilidades

| Integrante | Secciones asignadas |
|---|---|
| Rochina Rochina Freddy David | `01_guion` (entrevista estructurada) |
| Sánchez Centeno Roselyn Andreina | `02_consentimiento`, `05_ajustes` |
| Mendoza Palma Allan Jeremy | `03_ensayo`, `04_empatia`, `06_uso_ia`, integración, compilación y README |

## Protección y registro de evidencias

No se publican audios, videos, teléfonos, cédulas, correos personales de terceros ni consentimientos firmados. Los registros originales se conservan en una carpeta institucional privada accesible mediante cuenta `@uteq.edu.ec` y compartida con el docente, según la guía de la actividad.

El archivo `evidencias/manifiesto.csv` dispone de las columnas `nombre_archivo`, `fecha`, `duracion` y `sha256`, sin registros de entrevistas en esta versión. Las huellas SHA-256 se obtienen sobre los archivos originales, después de su producción, y se incorporan al manifiesto únicamente cuando existe evidencia real verificable.
