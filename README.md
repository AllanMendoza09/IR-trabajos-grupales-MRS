# PC1 · GA-PRAC-01 — Comparación entre modelos de proceso de requisitos

**Asignatura:** Ingeniería de Requisitos (ISR-401), UTEQ, Unidad 1, Semana 2.

**Escenario:** Sistema de gestión de trámites y solicitudes ciudadanas de un GAD municipal ecuatoriano, contratado mediante contratación pública.

**Modelo elegido por el equipo:** iterativo-incremental.

**Integrantes:** Mendoza Palma Allan Jeremy; Rochina Rochina Freddy David; Sánchez Centeno Roselyn Andreina.

## Estado del commit 1

- **Sección 1:** escenario, rasgos clave y supuestos — Mendoza.
- **Sección 2:** pendiente — Rochina.
- **Sección 3:** matriz completa de tres modelos por cinco criterios, con valoración y mejor opción en cada fila — Mendoza.
- **Sección 4:** pendiente — Rochina.
- **Sección 5:** pendiente — Sánchez.
- **Sección 6:** riesgos del modelo iterativo-incremental y mitigaciones — Mendoza.
- **Sección 7:** pendiente — Sánchez.

La sección completada identifica a su autor. Los apartados pendientes permanecen como marcadores técnicos en `main.tex`. El documento puede compilarse sin esperar los commits posteriores.

## Archivos

- `main.tex`: fuente principal, clase IEEEtran, una sola columna.
- `referencias.bib`: las tres fuentes utilizadas en este avance.
- `README.md`: instrucciones de reproducción.
- `main.pdf`: se obtiene compilando `main.tex`. Se generará en el commit final si así se acuerda.

## Compilación

**Compilador:** pdfLaTeX.

**Gestor bibliográfico:** BibTeX (la configuración de `biblatex` es `backend=bibtex`, estilo `ieee`).

**Dependencias:** distribución LaTeX con `IEEEtran`, `biblatex`, `biblatex-ieee`, `babel-spanish`, `longtable`, `booktabs`, `tabularx`, `float`, `microtype` y demás paquetes indicados en `main.tex`.

Ejecutar en este orden desde la carpeta donde está `main.tex`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

La configuración **usa BibTeX y no Biber**. `main.pdf` debe generarse sin editar el código y con las referencias resueltas. El uso de `longtable` mantiene la matriz y la tabla de riesgos dentro de sus secciones, sin moverlas antes del título.

## Alcance de la evidencia

No se ha contado con pliegos, entrevistas, actas, registros del GAD ni datos de campo. Los juicios de la matriz y los riesgos son propuestas basadas en el escenario de la guía. El equipo debe completar con sus revisiones reales la sección final de autoría, la revisión cruzada y la declaración de uso de IA.
