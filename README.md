# PC1 · GA-PRAC-01 — Comparación entre modelos de proceso de requisitos

**Asignatura:** Ingeniería de Requisitos (ISR-401), UTEQ, Unidad 1, Semana 2.  
**Caso:** Sistema de gestión de trámites y solicitudes ciudadanas de un GAD municipal del Ecuador, contratado por procedimiento público.  
**Modelo seleccionado:** iterativo-incremental.

**Integrantes:** Mendoza Palma Allan Jeremy; Rochina Rochina Freddy David; Sánchez Centeno Roselyn Andreina.

## Contenido del informe

1. Escenario y rasgos clave.
2. Caracterización de cascada, iterativo-incremental y ágil.
3. Matriz comparativa de tres modelos por cinco criterios, con resultado contextualizado por fila.
4. Actores y framework: actividades, artefactos y momentos I0--I3.
5. Recomendación del modelo iterativo-incremental con cuatro razones y descarte de alternativas.
6. Riesgos del modelo elegido (cinco situaciones con causas y mitigaciones).
7. Conclusión, distribución del trabajo, revisión cruzada y declaración de uso de IA **en subsecciones separadas**.

## Distribución de secciones acordada

| Sección | Responsable |
|---|---|
| 1. Escenario y rasgos clave | Mendoza Palma Allan Jeremy |
| 2. Caracterización de los modelos | Rochina Rochina Freddy David |
| 3. Matriz comparativa contextualizada | Mendoza Palma Allan Jeremy |
| 4. Actores y framework de IR | Rochina Rochina Freddy David |
| 5. Recomendación | Sánchez Centeno Roselyn Andreina |
| 6. Riesgos | Mendoza Palma Allan Jeremy |
| 7. Conclusión y documentación final | Sánchez Centeno Roselyn Andreina |

Las aportaciones efectivas deben corresponder a los cambios y revisiones realmente realizados en GitHub. La tabla de revisión cruzada del documento contiene campos pendientes, no evidencias ya obtenidas.

## Archivos finales

- `main.tex`: fuente LaTeX IEEEtran de una columna.
- `referencias.bib`: tres referencias académicas base citadas (Pohl, SWEBOK e IREB).
- `README.md`: estas instrucciones de reproducción.
- `main.pdf`: PDF compilado desde `main.tex`.
- `Mensaje_Commit_3.txt`: título y descripción del tercer commit.
- `Cambios_Commit_2_a_3.diff`: diferencias con el documento acumulado del commit anterior.

## Compilación reproducible

**Archivo principal:** `main.tex`.  
**Compilador:** pdfLaTeX.  
**Bibliografía:** `biblatex`, estilo IEEE, **backend `bibtex`** (no Biber).

Dependencias: instalación TeX Live o MiKTeX con la clase `IEEEtran` y los paquetes `biblatex`, `biblatex-ieee`, `babel-spanish`, `booktabs`, `longtable`, `tabularx`, `float`, `microtype`, `lmodern`, `csquotes`, `amsmath`, `hyperref` y demás declarados en el preámbulo.

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

El PDF generado debe coincidir con `main.pdf` a nivel de contenido. Las tablas usan `longtable` o `[H]` para permanecer en sus secciones.

## Límites del caso

No se dispone de pliegos municipales, entrevistas, actas, inventario de sistemas ni evidencias de campo. Los juicios de la matriz y los riesgos son hipótesis académicas contextualizadas y requieren contraste con las fuentes y reglas reales antes de aplicarse a una contratación pública concreta.

La sección de declaración de IA señala asistencia empleada en el desarrollo del borrador. El equipo debe completar y validar su propio registro de revisiones, correcciones y verificaciones, de acuerdo con el encuadre de ISR-401.
