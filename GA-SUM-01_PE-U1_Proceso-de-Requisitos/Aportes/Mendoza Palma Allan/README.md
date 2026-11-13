# Aporte de Allan Jeremy Mendoza Palma, Investigador A

**Proyecto:** Plataforma de ventas con módulo de recomendación basado en IA para establecimientos eléctricos.  
**Asignatura:** Ingeniería de Requerimientos (20303) — Práctica Experimental PE1, Unidad 1.  
**Institución:** Universidad Técnica Estatal de Quevedo (UTEQ).

## Alcance

- **Sección 0:** descripción del establecimiento comercial, delimitación preliminar del sistema, identificación de cinco interesados y su clasificación mediante una matriz poder/interés.
- **Sección 2.1:** fundamentos de Ingeniería de Requisitos, concepto de requisito, objetivos, principios, consecuencias de defectos y relación con el ciclo de vida del software y del sistema.
- **Sección 2.2:** proceso de Ingeniería de Requisitos, elicitación, análisis, especificación, validación, negociación, gestión, trazabilidad, línea base y control de cambios.
- **Sección 3.1:** instrumentos de elicitación: entrevistas para el propietario, cajeros y administrador, ficha de observación y selección justificada de técnicas.
- **Sección 3.2:** revisión documental mediante criterios de calidad y reformulaciones de los tres requisitos de ejemplo `EJ-01`, `EJ-02` y `EJ-03`.
- **Conclusión:** síntesis de la utilidad de la Ingeniería de Requisitos y su aplicación al proyecto comercial de Quevedo.
- **Anexos A y B:** espacios de inserción para la salida bibliográfica IEEE de Zotero y una captura de la colección bibliográfica utilizada.

## Resultados concretos

- Cinco stakeholders clasificados por poder, interés y estrategia de gestión.
- Treinta preguntas de entrevista: diez para el propietario, diez para los cajeros y diez para el administrador.
- Tres requisitos de ejemplo revisados en versión inicial y reformulada mediante ocho criterios (L01--L08), con criterios de aceptación propuestos y pendientes de validación identificados.
- Ocho tablas, una figura TikZ de poder/interés y dos figuras previstas para las capturas de Zotero.
- Trece fuentes en `aporte_allan.bib`: diez fuentes principales y tres complementarias.
- Instrumentos de elicitación preparados para aplicación; el documento no presenta entrevistas u observaciones como ejecutadas.

## Archivos

- `aporte_allan.text`: código LaTeX completo del aporte y sus dos anexos.
- `aporte_allan.bib`: referencias bibliográficas utilizadas con BibTeX y estilo IEEE.
- `aporte_allan.pdf`: salida de compilación del archivo principal, con referencias numeradas.
- `figura/anexo_a_bibliografia_ieee.png`: captura de la bibliografía de las diez fuentes principales generada desde Zotero con estilo IEEE.
- `figura/anexo_b_coleccion_zotero.png`: captura de la colección Zotero que muestra las fuentes principales y complementarias.
- `README.md`: descripción del contenido, recursos y procedimiento de compilación.

## Inclusión de capturas de Zotero

Crear la carpeta `figura/` junto a `aporte_allan.tex` y guardar las imágenes PNG con los nombres exactos señalados arriba. El código LaTeX comprueba si existen esos archivos mediante `\IfFileExists`; cuando están disponibles, los inserta en los anexos con su pie de figura y referencia. Si aún no existen, el documento puede compilarse mostrando espacios reservados. Para actualizar el PDF con las imágenes basta volver a compilar el archivo principal.

El **Anexo A** debe mostrar la bibliografía IEEE de las diez fuentes principales, no las tres complementarias. El **Anexo B** debe mostrar de forma legible la colección `PE1 - Fuentes obligatorias` en Zotero.

## Compilación

Se requiere una distribución LaTeX con la clase `IEEEtran`, los paquetes indicados en el preámbulo, BibTeX y el archivo de estilo `IEEEtran.bst`. Ejecutar desde la carpeta que contiene el `.tex`, el `.bib` y `figura/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error aporte_allan.tex
bibtex aporte_allan
pdflatex -interaction=nonstopmode -halt-on-error aporte_allan.tex
pdflatex -interaction=nonstopmode -halt-on-error aporte_allan.tex
```

## Relación con el resto del informe

Los requisitos de ejemplo `EJ-01`, `EJ-02` y `EJ-03` se reconciliarán con los identificadores definitivos establecidos en la tabla de requisitos de Freddy David Rochina Rochina. La clasificación inicial del sistema y los cinco stakeholders apoyan el desarrollo de contexto, actores, límites y perspectivas de Roselyn Andreina Sánchez Centeno. Las referencias principales conservan las claves bibliográficas y el orden de citación compartido para la integración del informe.

## Estado de validación de requisitos

Los ejemplos `EJ-01`, `EJ-02` y `EJ-03` cuentan con una reformulación y una revisión documental, pero permanecen pendientes de validación con los interesados. Los criterios L08 de los tres ejemplos siguen en estado P; en EJ-03 también están pendientes L03, L04 y L05. No se han ejecutado entrevistas de confirmación, ensayos de campo, evaluación técnica especializada ni aprobaciones institucionales. Los identificadores también deben conciliarse con la tabla de requisitos del equipo antes de integrar la versión definitiva.

## Revisión documental del Cuadro VIII

El Cuadro VIII compara los tres requisitos EJ-01, EJ-02 y EJ-03 en versiones iniciales y reformuladas. C significa cumple en redacción, I significa incumple y P indica una condición pendiente de confirmar. Las marcas no representan resultados de pruebas ni aceptación formal por el establecimiento.

## Referencias en Overleaf

El archivo principal puede llamarse `main.tex` o `aporte_allan.tex`; debe estar en la raíz del proyecto junto con `aporte_allan.bib`. Seleccionar **pdfLaTeX** y usar la sintaxis BibTeX del documento:

```latex
\bibliographystyle{IEEEtran}
\bibliography{aporte_allan}
```

En Overleaf, seleccionar *Recompilar desde cero* en el menú de Recompilar si las citas aparecen como `[?]` o la lista de referencias queda vacía. Comprobar en los registros que BibTeX no indique claves ausentes ni errores de sintaxis. Si se compila localmente usando `main.tex`, la secuencia es:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

No usar Biber con este proyecto, porque emplea `cite` y BibTeX, no `biblatex`.
