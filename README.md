# PC1 · GA-PRAC-01 — Comparación entre modelos de proceso de requisitos

**Asignatura:** Ingeniería de Requisitos (ISR-401), UTEQ, Unidad 1, Semana 2.

**Escenario:** Sistema de gestión de trámites y solicitudes ciudadanas de un GAD municipal ecuatoriano, contratado mediante contratación pública.

**Modelo elegido por el equipo:** iterativo-incremental.

**Integrantes:** Mendoza Palma Allan Jeremy; Rochina Rochina Freddy David; Sánchez Centeno Roselyn Andreina.

## Estado del commit 2

- **Sección 1:** escenario, rasgos clave y supuestos — Mendoza.
- **Sección 2:** caracterización de cascada, iterativo-incremental y ágil — incorporada en este avance.
- **Sección 3:** matriz completa de tres modelos por cinco criterios, con valoración y mejor opción en cada fila — Mendoza.
- **Sección 4:** actores y framework (actividades, momentos y artefactos) — incorporada en este avance.
- **Sección 5:** pendiente — Sánchez.
- **Sección 6:** riesgos del modelo iterativo-incremental y mitigaciones — Mendoza.
- **Sección 7:** pendiente — Sánchez.

Las secciones incorporadas y sus responsables se identifican en este README; no se añaden líneas de autoría debajo de los encabezados del artículo. Las secciones 5 y 7 permanecen como marcadores técnicos para el siguiente avance. El documento puede compilarse sin esperar el commit final.

## Archivos

- `main.tex`: fuente principal, clase IEEEtran, una sola columna.
- `referencias.bib`: las tres fuentes base utilizadas en las secciones acumuladas.
- `README.md`: instrucciones de reproducción.
- `main.pdf`: se obtiene compilando `main.tex`. Se generará en el commit final, según el reparto acordado.

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

## Distribución de secciones por integrante

| Sección | Integrante asignado | Estado en este commit |
|---|---|---|
| 1. Escenario y rasgos | Mendoza Palma Allan Jeremy | Incluida desde el commit 1 |
| 2. Caracterización de modelos | Rochina Rochina Freddy David | Incorporada en el commit 2 |
| 3. Matriz comparativa | Mendoza Palma Allan Jeremy | Incluida desde el commit 1 |
| 4. Actores y framework de IR | Rochina Rochina Freddy David | Incorporada en el commit 2 |
| 5. Recomendación | Sánchez Centeno Roselyn Andreina | Pendiente de integrar |
| 6. Riesgos | Mendoza Palma Allan Jeremy | Incluida desde el commit 1 |
| 7. Conclusión, distribución y uso de IA | Sánchez Centeno Roselyn Andreina | Pendiente de integrar |

Esta asignación refleja el plan del grupo. El historial de GitHub y la revisión del equipo deberán documentar quién realizó cada cambio.
