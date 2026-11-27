# FORM-SIM-01 — Simulación de priorización y negociación entre roles

**Asignatura:** Ingeniería de Requerimientos, ISR-401. **Equipo MRS:** Mendoza Palma Allan Jeremy, Rochina Rochina Freddy David y Sánchez Centeno Roselyn Andreina. **Período:** SPA 2026–2027. **Dominio:** unidad educativa, matrícula y calificaciones. **Cierre:** sábado 28 de noviembre de 2026, 23:59 (hora de Ecuador).

Este directorio es la base reproducible del primer avance de la actividad formativa FORM-SIM-01. La formativa no tiene nota, pero es condición de acceso a TA-IND-02. El PDF del primer avance contiene el fundamento técnico, los métodos y los protocolos iniciales, no resultados de campo. No debe presentarse como el informe final de seis a diez páginas.

## Archivos del primer avance

- `main.tex`: documento IEEEtran de una sola columna, con portada informativa, citas y carga modular de secciones.
- `main.pdf`: compilación verificable del archivo principal.
- `referencias.bib`: seis referencias exigidas, compatibles con IEEEtran.bst y BibTeX.
- `secciones/00_fundamento.tex`: fundamentos, fórmulas de MoSCoW y Spearman, y limitaciones de Kano.
- `secciones/07_uso_ia.tex`: alcance real de la asistencia de IA durante esta preparación.
- `secciones/08_consentimiento.tex`: condiciones de participación voluntaria, anonimización y custodia privada.
- `datos/requisitos.csv`: catálogo inicial de veinte requisitos candidatos, doce RF y ocho RNF medibles; su contenido debe revisarse con roles del dominio y el equipo.
- `datos/caracteristicas_kano.csv`: ocho características seleccionadas y relación con los requisitos.
- `datos/instrumento_kano.csv`: preguntas funcionales y disfuncionales de cada característica.
- `datos/moscow.csv`, `datos/respuestas_kano.csv`, `datos/votos.csv`, `datos/decision.csv`: archivos de entrada con encabezados, sin resultados artificiales ni participantes fabricados.
- `datos/ESQUEMA.md`: diccionario de datos y validaciones.
- `scripts/analisis.py`: validación del catálogo y análisis reproducible de MoSCoW, Kano, votación y Spearman, cuando existan datos.
- `scripts/autoprueba.py`: ensayos matemáticos usando datos sintéticos temporales, eliminados al terminar.
- `scripts/verificar_compilacion.sh`: compilación con chequeos reproducibles.
- `scripts/git_commit_1.sh`: comandos locales de inspección y registro del primer avance; no realiza `push`.
- `.gitignore`: evita incluir archivos auxiliares de LaTeX, sin excluir `main.pdf`.
- `evidencias/MANIFIESTO.md`: tabla sin registros empíricos, para inventariar evidencias custodiadas fuera del repositorio.

No están incorporadas aún las secciones `01_requisitos.tex` a `06_decision.tex` como resultados del equipo: las instrucciones `\IfFileExists` permiten integrar las secciones a medida que se revisen y se recopilen los datos reales. Su ausencia sería un incumplimiento en el informe **final**, no en este primer avance de estructura.

## Compilación del informe

Entornos compatibles: TeX Live 2023 o posterior, MiKTeX u Overleaf con `IEEEtran.cls`, `IEEEtran.bst`, `inputenc`, `fontenc`, `babel` (español y `es-tabla`), `booktabs`, `longtable`, `array`, `graphicx`, `amsmath`, `tikz` y `hyperref`. Seleccionar **pdfLaTeX**; utilizar **BibTeX**, no Biber. La bibliografía sigue IEEEtran.

Ejecutar desde `GA/SIM-01/`:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

La configuración pedida para esta actividad usa **BibTeX + IEEEtran.bst**, aunque el encuadre general permite ejemplos con `biblatex`; ante una indicación específica del docente para el formato bibliográfico, se respetará dicha indicación.

Para verificar el documento, tras compilar:

```bash
python3 scripts/analisis.py --verificar
python3 scripts/autoprueba.py
bash scripts/verificar_compilacion.sh
```

El verificador de estructuras confirma encabezados, claves y cardinalidades del catálogo; **no** considera cumplida la aplicación de Kano, la votación ni la priorización por disponer de sus archivos vacíos. `python3 scripts/analisis.py --procesar` rechaza datos ausentes, incompletos o inconsistentes; cuando se incorporen registros efectivos, genera `datos/calculos/` con las tablas y la correlación.

## Responsabilidades distribuidas

| Integrante | Responsabilidad asignada | Estado de incorporación en este primer avance |
|---|---|---|
| Freddy David Rochina Rochina | Requisitos y evaluación MoSCoW | Catálogo candidato e instrumento CSV creados como soporte técnico; no se atribuye una revisión o una priorización de Freddy sin constancia. |
| Roselyn Andreina Sánchez Centeno | Cuestionario Kano | Instrumento de preguntas creado; no se han recibido respuestas reales ni se atribuyen entrevistas ejecutadas. |
| Allan Jeremy Mendoza Palma | Estructura documental, fundamento, votación, comparación, decisiones, declaración de IA e integración | Se incorpora la base LaTeX, bibliografía, estructura de datos y scripts de validación. Los resultados empíricos aún no existen. |

## Política de evidencias y datos personales

Se utilizarán P01–P05 para Kano y P06–P08 para votación, ocho personas adultas diferentes. Los consentimientos firmados y cualquier evidencia original permanecerán en carpeta privada. No subir nombres, cédulas, correos electrónicos, teléfonos, audio, video ni documentos firmados. El manifiesto público contendrá únicamente código, rol, técnica, fecha, nombre de archivo privado y SHA-256; solo se añadirán filas cuando existan evidencias verificables.

## Reglas para el análisis y la posterior integración

MoSCoW admite Must, Should, Could y Wont con justificación y esfuerzo positivo por requisito. Debe verificarse que el esfuerzo de Must sea como máximo el 60 % del esfuerzo total. La votación exige veinte valores enteros no negativos por cada una de las tres personas; la suma por persona debe ser exactamente 100. Kano exige ocho pares de respuestas por cada uno de cinco participantes, con cinco opciones de respuesta. Las coincidencias de rango se resuelven por **rangos medios** y Spearman se calcula como Pearson sobre esos rangos para admitir empates. Kano clasifica solamente ocho características, de modo que no constituye por sí solo un ranking de veinte requisitos.

La lista final de inclusión y exclusión necesita deliberación y justificación de los integrantes, no un resultado automático atribuido a personas. Las cifras de los RNF son umbrales propuestos que requieren validación institucional, no mediciones de una unidad educativa real.

## Clonar y trabajar en la carpeta

```bash
git clone https://github.com/AllanMendoza09/IR-trabajos-grupales-MRS.git
cd IR-trabajos-grupales-MRS/GA/SIM-01
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

El repositorio remoto no se ha modificado desde esta preparación. El historial y los cambios Git deben comprobarse localmente antes de registrar el commit. El comando sugerido se encuentra en `scripts/git_commit_1.sh` y no incluye `git push`.

## Segundo avance: catálogo y protocolo para el dominio escolar

Se incorporaron `secciones/01_requisitos.tex` (20 requisitos para matrícula y calificaciones) y `secciones/03_kano.tex` (protocolo de Kano, votación, consentimiento y evidencia). La correspondencia de ocho características se vincula a `datos/caracteristicas_kano.csv`. No se han añadido resultados de participantes a `respuestas_kano.csv`, `votos.csv` ni al manifiesto. El catálogo es una propuesta revisable y no demuestra validación con una unidad educativa real.

Este proyecto se limita exclusivamente al dominio **unidad educativa: matrícula y calificaciones**; no se ha incorporado información de otros sistemas.
