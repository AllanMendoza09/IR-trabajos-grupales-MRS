# Aportes individuales

Carpeta con los aportes de cada integrante para la Práctica Experimental PE1 (Unidad 1) de **Ingeniería de Requerimientos [20303]**, Universidad Técnica Estatal de Quevedo, período 2026-2027 SPA.

**Proyecto:** Plataforma de ventas con módulo de recomendación basado en IA para el soporte de ventas en establecimientos eléctricos (Quevedo, Ecuador).

Cada integrante desarrolló su parte de forma independiente, en su propia subcarpeta. El informe final integrado se encuentra en `final/`.

## Estructura

```
aportes/
├── allan/      Investigador A
├── freddy/     Investigador B
└── roselyn/    Investigadora C
```

Cada subcarpeta contiene:

| Archivo | Descripción |
|---|---|
| `aporte_NOMBRE.tex` | Documento LaTeX completo y compilable (IEEEtran, una columna) |
| `aporte_NOMBRE.bib` | Referencias BibTeX de las fuentes citadas |
| `aporte_NOMBRE.pdf` | PDF compilado del aporte |
| `README.md` | Descripción de lo realizado por el integrante |

## Distribución del trabajo

| Integrante | Rol | Secciones |
|---|---|---|
| Allan Jeremy Mendoza Palma | Investigador A (además Analista Líder y Documentador) | Sección 0, 2.1, 2.2, 3.1, 3.2 y conclusión |
| Freddy David Rochina Rochina | Investigador B | 2.3, 2.4, 3.3, 3.4, 3.5 y conclusión |
| Roselyn Andreina Sánchez Centeno | Investigadora C | 2.5, 2.6, 3.6, 3.7, 3.8, 3.9 y conclusión |

Numeración de secciones del informe:

- **Sección 0:** descripción del sistema y stakeholders.
- **Sección 2:** fundamento teórico (2.1 a 2.6).
- **Sección 3:** artefactos del procedimiento (3.1 a 3.9).

## Convenciones compartidas

**Citas.** Se citan con `\cite{clave}` y estilo `IEEEtran`. Cada `.tex` incluye un `\nocite` inicial que fija la numeración de las fuentes principales:

| N.º | Clave | Fuente |
|---|---|---|
| [1] | `iso29148` | ISO/IEC/IEEE 29148:2018 |
| [2] | `iso15288` | ISO/IEC/IEEE 15288:2023 |
| [3] | `iso12207` | ISO/IEC/IEEE 12207:2017 |
| [4] | `iso25010` | ISO/IEC 25010:2023 |
| [5] | `pohl2025` | Pohl (2025), *Requirements Engineering*, 2.ª ed. |
| [6] | `swebok4` | SWEBOK v4.0 |
| [7] | `pmbok7` | PMBoK, 7.ª ed. |
| [8] | `ireb2023` | IREB CPRE Foundation Level v3.1 |
| [9] | `moore` | Moore (declaración de visión) |
| [10] | `mavin2009` | Mavin et al. (2009), EARS |

Fuentes adicionales: `glinz2007`, `hull2011`, `wiegers2013`.

**Identificadores de requisitos.**

| Prefijo | Origen |
|---|---|
| `RN`, `RS`, `RU`, `RF`, `RNF`, `RI`, `RR`, `RC` | Tabla de requisitos (Investigador B) |
| `CTX-` | Requisitos de las ocho perspectivas de contexto (Investigadora C) |
| `EJ-` | Requisitos de ejemplo para el artefacto de validación (Investigador A) |

**Bloques del `.tex`.** El cuerpo de cada aporte está delimitado con los comentarios `%%% [SECCION0]`, `%%% [FUNDAMENTO]`, `%%% [ARTEFACTOS]` y `%%% [CONCLUSION]` (cada uno con su cierre `%%% [/...]`), para facilitar la integración en el informe final.

## Compilación

Desde la subcarpeta del integrante:

```bash
pdflatex aporte_NOMBRE.tex
bibtex aporte_NOMBRE
pdflatex aporte_NOMBRE.tex
pdflatex aporte_NOMBRE.tex
```

Requiere una distribución LaTeX con la clase `IEEEtran` (incluida en TeX Live y en Overleaf).

## Integración

Los tres aportes se unifican en `final/` (`main.tex`, `referencias.bib` y el PDF de entrega `PE1_U1_MENDOZA_ROCHINA_SANCHEZ.pdf`), donde se reconcilian las referencias duplicadas y los identificadores de requisitos.