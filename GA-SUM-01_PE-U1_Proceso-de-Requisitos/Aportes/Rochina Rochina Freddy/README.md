# Aporte de Freddy David Rochina Rochina, Investigador B

**Proyecto:** Plataforma de ventas con módulo de recomendación basado en IA para establecimientos eléctricos  
**Asignatura:** Ingeniería de Requerimientos (20303) — Práctica Experimental PE1, Unidad 1  
**Institución:** Universidad Técnica Estatal de Quevedo (UTEQ)

---

## Alcance

* **Sección 2.3 (Tipos de requisitos):** Desarrolla la taxonomía jerárquica y operativa de requisitos (negocio, stakeholder, usuario, sistema, funcionales, no funcionales, rendimiento, interfaz, restricciones y conformidad) articulando ISO/IEC/IEEE 29148:2018, ISO/IEC 25010:2023, Pohl y Glinz, con ejemplos aplicados al establecimiento eléctrico en Quevedo, un esquema visual generado en TikZ y una tabla comparativa de síntesis.
* **Sección 2.4 (Propiedades de calidad de los requisitos):** Define y ejemplifica las nueve propiedades de calidad de un requisito individual y las cinco propiedades de un conjunto de requisitos conforme a ISO/IEC/IEEE 29148:2018, Pohl, Hull et al. y Wiegers y Beatty.
* **Sección 3.3 (Tabla de requisitos del PFC):** Documenta 19 requisitos únicos con identificador, tipo, descripción, prioridad MoSCoW y fuente de trazabilidad, aplicando sintaxis EARS en los requisitos funcionales y métricas cuantificadas de ISO/IEC 25010:2023 en los requisitos no funcionales y de rendimiento.
* **Sección 3.4 (Evaluación de propiedades de calidad):** Presenta una matriz de evaluación de los 19 requisitos frente a las nueve propiedades individuales de ISO/IEC/IEEE 29148:2018, detallando el estado de cumplimiento, su justificación verificable y las versiones corregidas para los enunciados con defectos detectados.
* **Sección 3.5 (Justificación de clasificación):** Explica el fundamento técnico de la categoría asignada a cada requisito y analiza los casos frontera correspondientes a restricciones arquitectónicas y obligaciones de conformidad normativa.
* **Conclusión y Anexos:** Sintetiza los hallazgos de la clasificación y evaluación de calidad de los requisitos junto con sus implicaciones para la etapa de validación en el Proyecto Fin de Curso, e incluye los Anexos A y B de respaldo bibliográfico en Zotero con sus respectivos enlaces DOI e ISBN.

---

## Resultados concretos

* **Cantidad total de requisitos únicos elaborados:** 19 requisitos (`RN-01` a `RC-02`).
* **Distribución por tipo:**
  * Requisitos de negocio (`RN`): 2 (`RN-01`, `RN-02`)
  * Requisitos de stakeholder (`RS`): 1 (`RS-01`)
  * Requisitos de usuario (`RU`): 1 (`RU-01`)
  * Requisitos funcionales (`RF`): 6 (`RF-01`, `RF-02`, `RF-03`, `RF-04`, `RF-05`, `RF-06`)
  * Requisitos no funcionales de calidad (`RNF`): 3 (`RNF-01`, `RNF-02`, `RNF-03`)
  * Requisitos de rendimiento (`RR`): 1 (`RR-01`)
  * Requisitos de interfaz (`RI`): 3 (`RI-01` usuario, `RI-02` hardware, `RI-03` software/comunicaciones)
  * Restricciones (`RC`): 1 (`RC-01`)
  * Requisitos de conformidad (`RC`): 1 (`RC-02`)
* **Requisitos no funcionales y de rendimiento cuantificados:** 4 de 4 (`RNF-01`, `RNF-02`, `RNF-03`, `RR-01`), todos con métricas numéricas y umbrales explícitos.
* **Requisitos funcionales con sintaxis EARS:** 6 de 6 (`RF-01` a `RF-06`), desglosados en 4 patrones dirigidos por eventos, 1 patrón ubicuo y 1 patrón de comportamiento no deseado.
* **Requisitos con propuesta de versión corregida tras la evaluación:** 2 requisitos con corrección de redacción/estructura técnica (`RF-03` y `RI-03`, desdoblado en `RI-03A` y `RI-03B`), más la acción transversal de validación con interesados para la propiedad de corrección (`P8`) en los 19 requisitos.
* **Cantidad de tablas y figuras elaboradas:** 4 tablas (`tab:tipos_req`, `tab:requisitos_pfc`, `tab:eval_propiedades`, `tab:justif_clasif`) y 2 figuras (`fig:taxonomia_req` generada en TikZ y `fig:zotero_freddy` de evidencia bibliográfica).
* **Cantidad de fuentes citadas:** 12 fuentes bibliográficas confiables respaldadas con enlaces DOI/ISBN en formato IEEE comprimido (`[1]` a `[12]`).

---

## Archivos

* `aporte_freddy.tex`: Código fuente principal en LaTeX bajo la clase `IEEEtran` con los bloques delimitados de fundamento teórico, artefactos, conclusión y anexos.
* `aporte_freddy.bib`: Base de datos bibliográfica en formato BibTeX con las 12 referencias normativas y académicas verificadas.
* `aporte_freddy.pdf`: Documento compilado en formato PDF generado a partir de las fuentes LaTeX y BibTeX.
* `README.md`: Documentación descriptiva del alcance, resultados, compilación y convenciones del aporte.

---

## Compilación

Para compilar el documento y resolver correctamente las referencias cruzadas y citas bibliográficas se requiere tener instalada la clase estándar `IEEEtran` (incluida en distribuciones como TeX Live o MiKTeX) y ejecutar la siguiente secuencia en terminal:

```bash
pdflatex aporte_freddy.tex
bibtex aporte_freddy
pdflatex aporte_freddy.tex
pdflatex aporte_freddy.tex