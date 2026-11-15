# PE1 — Unidad 1: Ingeniería de Requerimientos

**Proyecto:** Plataforma de ventas con módulo de recomendación basado en IA para el soporte de ventas en establecimientos eléctricos (Quevedo, Ecuador).

**Institución:** Universidad Técnica Estatal de Quevedo (UTEQ), Facultad de Ciencias de la Computación, carrera de Ingeniería en Software (Rediseño), cuarto nivel, paralelo B.  
**Asignatura:** Ingeniería de Requerimientos (20303).  
**Docente:** Ing. Gleiston Ciceron Guerrero Ulloa.  
**Período:** 2026–2027 SPA.

## Integrantes y aportes

| Integrante | Responsabilidad | Contenido |
|---|---|---|
| Allan Jeremy Mendoza Palma | Analista líder y documentador; investigador A | Descripción del sistema, matriz poder/interés, fundamentos y proceso de IR (2.1–2.2), instrumentos de elicitación y revisión documental de EJ-01–EJ-03 (3.1–3.2). |
| Freddy David Rochina Rochina | Investigador B | Tipos y propiedades de requisitos (2.3–2.4), especificación, evaluación y justificación de requisitos del PFC (3.3–3.5). |
| Roselyn Andreina Sánchez Centeno | Investigadora C | Contexto, límites, actores y framework (2.5–2.6), aplicación, declaración de visión y perspectivas de contexto (3.6–3.9). |

## Estructura

```text
Documento Final/
├── README.md
├── main.tex
├── main.text
├── referencias.bib
├── PE1_U1_MENDOZA_ROCHINA_SANCHEZ.pdf
    └── figura/
    ├── LogoUTEQ.jpg
    ├── mapa_conceptual.pdf
    ├── mapa_conceptual.drawio
    ├── anexo_a_bibliografia_ieee.png
    └── anexo_b_coleccion_zotero.png
```

La imagen `anexo_a_bibliografia_ieee.png` ya preparada por el equipo debe conservarse en la carpeta `final/figura/` al subir el proyecto a Overleaf. El paquete incluye los recursos disponibles aquí y admite la imagen de la captura del equipo sin cambios de código.

## Contenido del informe integrado

- Carátula institucional adaptada a PE1, índice, sistema del PFC, secciones teóricas 2.1–2.6 y artefactos 3.1–3.9.
- Cinco conclusiones, referencias IEEE y anexos bibliográficos A y B.
- **21 requisitos principales** con identificadores únicos (dos categorías de conformidad independientes) y **16 registros de contexto `CTX-`**. La cifra de 37 representa registros de especificación y contexto, no 37 funcionalidades distintas.
- **21 tablas** y **8 figuras**, incluido el mapa conceptual en formato editable y PDF.
- **15 fuentes bibliográficas**, con las diez referencias principales ordenadas según la clave compartida.
- Validación con interesados pendiente; se documenta la inspección de requisitos y la trazabilidad, no una aceptación formal del establecimiento.

## Compilación

Desde la carpeta `final/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

El documento utiliza `IEEEtran` en una columna, tamaño de letra de 12 puntos, hoja A4, `BibTeX` y el estilo `IEEEtran.bst`.

