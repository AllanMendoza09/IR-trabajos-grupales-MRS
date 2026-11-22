# GA-TL-02 — Taller de entrevista estructurada y design thinking aplicado al PFC

Actividad formativa GA-TL-02 -- FORM, de Ingeniería de Requerimientos (ISR-401), Unidad 2, SPA 2026–2027, de la Universidad Técnica Estatal de Quevedo. El proyecto de fin de curso estudia una plataforma de ventas con un módulo de recomendación basado en inteligencia artificial para establecimientos eléctricos de Quevedo, Ecuador.

## Organización del documento

Archivo principal: `main.tex`. Documento generado: `main.pdf`. Bibliografía: `referencias.bib`, procesada con BibTeX y el estilo `IEEEtran`.

Las secciones se incorporan mediante `\input` y se presentan en este orden:

1. `secciones/01_guion.tex`: guion de trece preguntas de entrevista estructurada (incluye consentimiento verbal).
2. `secciones/02_consentimiento.tex`: protocolo de consentimiento informado y modelo sin completar.
3. `secciones/03_ensayo.tex`: condiciones y análisis del ensayo de entrevista.
4. `secciones/04_empatia.tex`: mapa de empatía con TikZ, hallazgos, trazabilidad y definición del problema.
5. `secciones/05_ajustes.tex`: revisión y ajustes del guion.
6. `secciones/06_uso_ia.tex`: declaración de asistencia de IA correspondiente a Allan y Roselyn.

El ejercicio fue una simulación académica efectuada el 21 de noviembre de 2026 mediante Microsoft Teams. Mendoza Palma Allan Jeremy realizó las preguntas y Sánchez Centeno Roselyn Andreina interpretó el rol de cajera y se encargó de la grabación. Las respuestas no representan testimonios de personal real de un establecimiento.

## Compilación reproducible

Requiere TeX Live 2023 o posterior, o Overleaf. Clase `IEEEtran` (una columna, 12 puntos), compilador `pdfLaTeX` y procesador bibliográfico `BibTeX`. Paquetes utilizados en `main.tex`: `inputenc` (utf8), `fontenc` (T1), `babel` (spanish), `booktabs`, `longtable`, `array`, `graphicx`, `tikz` y `hyperref` (`hidelinks`).

Desde `GA/TL-02/` ejecutar, en este orden:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

La compilación genera `main.pdf`. Los archivos `.tex`, `.bib` y el PDF se mantienen en el repositorio. Los archivos auxiliares de compilación se excluyen mediante `.gitignore`.

## Estructura del proyecto

```text
GA/TL-02/
├── main.tex
├── main.pdf
├── referencias.bib
├── README.md
├── .gitignore
├── secciones/
│   ├── 01_guion.tex
│   ├── 02_consentimiento.tex
│   ├── 03_ensayo.tex
│   ├── 04_empatia.tex
│   ├── 05_ajustes.tex
│   └── 06_uso_ia.tex
└── evidencias/
    └── manifiesto.csv
```

## Responsabilidades de las secciones

| Integrante | Contribución registrada para esta versión |
|---|---|
| Mendoza Palma Allan Jeremy | Elaboración de `01_guion.tex` tras la redistribución de tareas, `03_ensayo.tex`, `04_empatia.tex`, integración, README, compilación y preparación del registro de uso de IA. |
| Sánchez Centeno Roselyn Andreina | `02_consentimiento.tex`, `05_ajustes.tex` y participación en el ensayo de entrevista como cajera simulada y responsable de la grabación. |
| Rochina Rochina Freddy David | Integrante del equipo originalmente asignado al guion; no se registró una contribución ni un commit suyo para esta actividad, según informó la coordinación del equipo. |

Debido a una situación personal comunicada por el equipo, la responsabilidad del guion inicialmente asignada a Freddy fue asumida por Allan. Este registro describe la distribución informada para la versión entregada y no sustituye el historial verificable de GitHub. No se incluyen detalles familiares privados.

## Protección de evidencias

La grabación de audio `ENV-ENSAYO.m4a` y cualquier consentimiento firmado se mantienen fuera del repositorio público, en almacenamiento institucional privado. El archivo público `evidencias/manifiesto.csv` registra nombre, fecha del ensayo, duración comunicada y huella SHA-256 calculada por el equipo. El repositorio no contiene audio, video, transcripciones completas ni consentimientos firmados.

La grabación se informó como audio de 5 minutos y 10 segundos. La huella SHA-256 del manifiesto corresponde al valor comunicado tras el cálculo local con PowerShell; la comparación con el archivo de audio original requiere acceso al almacenamiento privado.
