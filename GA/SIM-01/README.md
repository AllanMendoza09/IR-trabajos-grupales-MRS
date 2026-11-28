# FORM-SIM-01 — Simulación de priorización y negociación entre roles

**Asignatura:** Ingeniería de Requerimientos, ISR-401. **Equipo MRS:** Mendoza Palma Allan Jeremy, Rochina Rochina Freddy David y Sánchez Centeno Roselyn Andreina. **Período:** SPA 2026–2027. **Dominio:** unidad educativa, matrícula y calificaciones. **Cierre:** sábado 28 de noviembre de 2026, 23:59 (hora de Ecuador).

Este directorio reúne el trabajo grupal de la actividad formativa FORM-SIM-01. La actividad no tiene calificación propia, pero su entrega válida es requisito para TA-IND-02. Se consolidan el catálogo de veinte requisitos escolares, MoSCoW, la clasificación Kano y la votación ponderada; la selección de la primera versión se presenta como propuesta sujeta a acuerdo del equipo.

## Archivos del proyecto y avances acumulativos

- `main.tex`: documento IEEEtran de una sola columna, con portada informativa, citas y carga modular de secciones.
- `main.pdf`: versión compilada del informe integrado; se regenera tras incorporar los últimos cambios de las secciones.
- `referencias.bib`: seis referencias exigidas, compatibles con IEEEtran.bst y BibTeX.
- `secciones/00_fundamento.tex`: fundamentos, fórmulas de MoSCoW y Spearman, y limitaciones de Kano.
- `secciones/01_requisitos.tex`: catálogo de doce requisitos funcionales y ocho de calidad, redactados para matrícula y calificaciones.
- `secciones/02_moscow.tex`: clasificación de los veinte requisitos, esfuerzos y verificación del límite Must.
- `secciones/03_kano.tex`: ocho características, instrumento de dieciséis preguntas, clasificación y resultados observados.
- `secciones/04_votacion.tex`: puntuaciones agregadas de P06, P07 y P08 con orden de votación.
- `secciones/05_comparacion.tex`: comparación de MoSCoW, Kano y votación; coeficiente de Spearman con rangos medios.
- `secciones/06_decision.tex`: propuesta de primera versión y justificación de requisitos aplazados.
- `secciones/07_uso_ia.tex`: alcance real de la asistencia de IA durante esta preparación.
- `secciones/08_consentimiento.tex`: condiciones de participación voluntaria, anonimización y custodia privada.
- `datos/requisitos.csv`: catálogo vigente de veinte requisitos candidatos (doce RF y ocho RNF medibles); sus umbrales aún requieren validación institucional.
- `datos/caracteristicas_kano.csv`: ocho características seleccionadas y relación con los requisitos.
- `datos/instrumento_kano.csv`: preguntas funcionales y disfuncionales de cada característica.
- `datos/moscow.csv`: clasificación aportada por Freddy: nueve Must, siete Should y cuatro Could, con 92 puntos relativos de esfuerzo.
- `datos/respuestas_kano.csv`, `datos/kano_respuestas.csv` y `datos/kano_clasificacion.csv`: formularios seudonimizados y categorías agregadas de Kano aportados por Roselyn.
- `datos/votos.csv`: votaciones P06, P07 y P08: veinte registros por votante y cien puntos por participante.
- `datos/decision.csv`: archivo de negociación para documentar una decisión ratificada; no confundir con la propuesta académica de `06_decision.tex`.
- `datos/calcular_resultados.py`: cálculo reproducible de votos, rangos medios, Spearman, resumen y tablas.
- `datos/calculos/`: resultados CSV y JSON calculados a partir de los archivos vigentes.
- `tablas/`: tablas LaTeX generadas que utilizan las secciones de votación y comparación.
- `datos/01_requisitos.csv`: catálogo alternativo existente en GitHub cuyas definiciones no coinciden con el catálogo vigente; no se utiliza en los cálculos.
- `datos/ESQUEMA.md`: diccionario de datos y validaciones.
- `scripts/analisis.py`: herramienta inicial de validación; el análisis integrado utiliza `datos/calcular_resultados.py` debido al encabezado real del archivo MoSCoW.
- `scripts/autoprueba.py`: ensayos matemáticos usando datos sintéticos temporales, eliminados al terminar.
- `scripts/verificar_compilacion.sh`: compilación con chequeos reproducibles.
- `scripts/git_commit_1.sh`: comandos locales de inspección y registro del primer avance; no realiza `push`.
- `.gitignore`: evita incluir archivos auxiliares de LaTeX, sin excluir `main.pdf`.
- `evidencias/MANIFIESTO.md`: ocho consentimientos privados registrados como metadatos, con sus SHA-256 obtenidos sobre copias JPG de nombres cubiertos; no contiene imágenes ni datos de identidad.

Las secciones `01_requisitos.tex` a `03_kano.tex` ya se incorporaron al repositorio durante los aportes de Freddy y Roselyn. Las secciones `04_votacion.tex` a `06_decision.tex` forman el análisis incorporado por Allan. `\IfFileExists` permite integrarlas sin alterar el archivo principal. La reproducibilidad depende de conservar simultáneamente las fuentes, los datos y el PDF actualizado.

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

Para reproducir los cálculos integrados y verificar el PDF desde `GA/SIM-01/`:

```bash
python3 datos/calcular_resultados.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

El script de análisis integrado usa solamente la biblioteca estándar de Python; lee `datos/moscow.csv`, `datos/kano_clasificacion.csv` y `datos/votos.csv` y genera las salidas de `datos/calculos/` y `tablas/`. `scripts/autoprueba.py` y `scripts/verificar_compilacion.sh` permanecen como utilidades del avance estructural. Antes de subir `main.pdf`, se debe verificar que contenga la versión más reciente de las secciones de los tres integrantes.

## Responsabilidades distribuidas

| Integrante | Responsabilidad asignada | Estado documentado |
|---|---|---|
| Freddy David Rochina Rochina | Requisitos y evaluación MoSCoW | Veinte requisitos y priorización MoSCoW incorporados a GitHub, con categorías, esfuerzo y justificaciones; esfuerzo Must 44/92. |
| Roselyn Andreina Sánchez Centeno | Cuestionario Kano | Instrumento y resultados de ocho características Kano incorporados a GitHub, con cinco formularios registrados y un problema de duplicación del identificador P04. |
| Allan Jeremy Mendoza Palma | Estructura documental, fundamento, votación, comparación, decisiones, declaración de IA e integración | Estructura del informe, sesenta votos P06–P08, script de cálculo, Spearman, comparación, propuesta de alcance, README y manifiesto de ocho consentimientos. |

## Política de evidencias y datos personales

Los identificadores P01–P05 se usan en Kano y P06–P08 en votación. Los formularios firmados, incluidos ENC-P01.jpg a ENC-P05.jpg y VOT-P06.jpg a VOT-P08.jpg, permanecen en almacenamiento privado; no se suben imágenes ni originales a GitHub. El manifiesto público recoge código, técnica, nombre del archivo privado, duración no aplicable y SHA-256 comunicado por el equipo. La fecha y el rol se registran como no informados cuando no hay respaldo. Los nombres tapados en los JPG no constituyen anonimización absoluta.

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

El historial de commits se conserva en GitHub y permite distinguir aportes progresivos del equipo. Los cambios se revisan con `git status` y `git diff` antes de cada commit; no se deben publicar originales de encuestas o consentimientos.

## Segundo avance: catálogo y protocolo para el dominio escolar

Se incorporaron `secciones/01_requisitos.tex` (20 requisitos para matrícula y calificaciones), `secciones/02_moscow.tex` (priorización por esfuerzo) y `secciones/03_kano.tex` (instrumento y resultados del cuestionario). La correspondencia de ocho características se vincula a `datos/caracteristicas_kano.csv`. Los resultados proceden de respuestas registradas, no de mediciones operativas de una unidad educativa.

Este proyecto se limita exclusivamente al dominio **unidad educativa: matrícula y calificaciones**; no se ha incorporado información de otros sistemas.


## Tercer avance: votación, comparación y propuesta de alcance

Los participantes P06, P07 y P08 asignaron cien puntos cada uno entre los veinte requisitos. La suma conjunta fue de 300 puntos. El límite de esfuerzo MoSCoW se cumple: Must suma 44 puntos sobre un total de 92 (47,83 %, menor que 60 %). La correlación de Spearman entre los rangos medios de MoSCoW y votación es 0,6605 (n = 20 requisitos); indica una asociación positiva apreciable para los datos analizados, sin permitir generalizar a toda una comunidad educativa.

La clasificación Kano asignó las siguientes categorías predominantes: K01 y K08 indiferente; K02, K03, K04 y K05 unidimensional; K06 y K07 atractiva. Kano solo evalúa ocho características. La fuente publicada contiene dos bloques identificados como P04 y ninguno como P03; la existencia de un archivo de consentimiento rotulado P03 no prueba por sí sola qué respuestas le corresponden. Se preservan las respuestas y se registra esta limitación.

Se propone incluir los nueve Must en una primera versión y aplazar los siete Should y cuatro Could. Esta regla debe ratificarse por el equipo antes de reportarla como acuerdo definitivo. Los requisitos aplazados mantienen su identificador para análisis posteriores; no hay requisitos Won't en el archivo MoSCoW.

## Evidencias y auditoría del manifiesto

El manifiesto incluye ocho entradas seudonimizadas. Sus huellas SHA-256 fueron calculadas sobre las copias JPG privadas y comunicadas por el responsable de la actividad; no se cotejaron de forma independiente en este repositorio. Las copias no se publican. Cualquier cambio de bytes (edición, nueva exportación o recompresión) invalida la huella anterior y exige recalcularla.
