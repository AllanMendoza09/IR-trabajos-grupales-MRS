# Aporte de Roselyn Andreina Sánchez Centeno, Investigadora C

**Proyecto:** Plataforma de ventas con módulo de recomendación basado en IA para el soporte de ventas en establecimientos eléctricos (Quevedo, Ecuador).
**Asignatura:** Ingeniería de Requerimientos (ISR-401 / 20303) — Universidad Técnica Estatal de Quevedo (UTEQ).
**Práctica:** PE1 · Unidad 1.
**Rol:** Investigadora C.
**Equipo:** Mendoza Palma Allan Jeremy (Investigador A, Analista Líder y Documentador) · Rochina Rochina Freddy David (Investigador B) · Sánchez Centeno Roselyn Andreina (Investigadora C).

## Alcance

- **2.5 Contexto y tipo de sistema.** Se define el concepto de sistema y de contexto del sistema, se distingue el límite del sistema del límite del contexto, se clasifican los tipos de sistema y se presentan las ocho perspectivas de contexto de Pohl. El apartado cierra con la conclusión justificada del tipo de sistema del PFC.
- **2.6 Actores y framework de ingeniería de requisitos.** Se describen los actores del proceso de requisitos con sus roles y se expone el framework de IR con sus tres actividades core y sus dos actividades transversales.
- **3.6 Actores y framework aplicados al PFC.** Se asigna cada actor del proceso a personas y roles reales del PFC y se mapea cada actividad del framework a una aplicación concreta en la plataforma.
- **3.7 Límite del sistema.** Se identifican las entidades externas de la plataforma con los datos intercambiados, el protocolo supuesto y la frecuencia de cada interfaz, y se dibuja el diagrama de contexto.
- **3.8 Declaración de visión en formato Moore.** Se redactan dos versiones de la declaración de visión y se desglosan sus componentes en una tabla.
- **3.9 Ocho perspectivas de contexto aplicadas al PFC.** Para cada perspectiva se formulan tres preguntas clave y dos requisitos o restricciones con identificador `CTX-`, y se evalúan los dieciséis requisitos contra las propiedades de la norma.
- **Conclusión.** Se cierra con una afirmación, su evidencia citada y la implicación para el PFC.

## Artefactos producidos

| Tipo | Identificador | Contenido |
|---|---|---|
| Tabla | `tab:tipos` | Tipos de sistema de Pohl y su relación con el PFC. |
| Tabla | `tab:perspectivas` | Las ocho perspectivas de contexto, su foco y una pregunta guía. |
| Tabla | `tab:actores` | Actores del proceso de requisitos, definición y rol. |
| Tabla | `tab:actores-pfc` | Personas y roles reales del PFC asignados a cada actor. |
| Tabla | `tab:framework-pfc` | Matriz de las cinco actividades del framework aplicadas al PFC. |
| Tabla | `tab:limite` | Siete entidades externas con datos, protocolo y frecuencia. |
| Tabla | `tab:moore` | Componentes de la declaración de visión en cada versión. |
| Tabla | `tab:ctx` | Evaluación de los dieciséis requisitos `CTX-` contra cuatro propiedades de la norma. |
| Figura | `fig:perspectivas` | Las ocho perspectivas de contexto alrededor del sistema. |
| Figura | `fig:framework` | Framework de IR: actividades core, transversales y artefactos. |
| Figura | `fig:contexto` | Diagrama de contexto del sistema y sus entidades externas. |

Todas las tablas y figuras se dibujan o componen dentro del propio `.tex`, llevan `\caption` y `\label`, y se referencian en el texto con `\ref`. Las figuras se construyen con TikZ, sin archivos externos.

## Resultados concretos

| Resultado | Cantidad | Detalle |
|---|---|---|
| Actores del proceso asignados | 5 | cliente, usuario, ingeniero de requisitos, desarrollador y otros interesados |
| Actividades del framework mapeadas | 5 | 3 core (elicitación, documentación, negociación) y 2 transversales (validación, gestión) |
| Entidades externas del límite | 7 | pasarela de pago, proveedores, clientes, auditor, servicio de recomendación, SRI y hardware POS/impresora |
| Versiones de la declaración de visión | 2 | operativa (cajero) y estratégica (propietario) |
| Perspectivas de contexto trabajadas | 8 | uso, sujeto, sistema de TI, desarrollo, negocio, innovación, sociedad y técnica |
| Requisitos `CTX-` generados | 16 | `CTX-01` … `CTX-16` |
| Diagramas TikZ | 3 | perspectivas de contexto, framework y diagrama de contexto |
| Tablas | 8 | tipos de sistema, perspectivas, actores, actores del PFC, framework del PFC, límite, Moore y evaluación `CTX-` |
| Fuentes citadas | 10 | referencias `[1]` … `[10]` |

## Estructura del documento

El cuerpo del `.tex` está delimitado por comentarios que permiten extraer cada bloque para integrarlo en el informe final:

```
%%% [FUNDAMENTO]   ... %%% [/FUNDAMENTO]     (subsecciones 2.5 y 2.6)
%%% [ARTEFACTOS]   ... %%% [/ARTEFACTOS]     (subsecciones 3.6, 3.7, 3.8 y 3.9)
%%% [CONCLUSION]   ... %%% [/CONCLUSION]     (conclusión)
```

El documento abre con un `\nocite` que fija la numeración de las diez fuentes principales y termina con `\bibliographystyle{IEEEtran}` y `\bibliography{aporte_roselyn}`.

## Archivos

| Archivo | Descripción |
|---|---|
| `aporte_roselyn.tex` | Documento fuente LaTeX completo y compilable, en formato IEEE de una columna, con los tres bloques extraíbles. |
| `aporte_roselyn.bib` | Bibliografía en formato BibTeX con las diez fuentes citadas, en el orden que fija la numeración `[1]`–`[10]`. |
| `aporte_roselyn.pdf` | Documento compilado (10 páginas). |
| `README.md` | Este archivo. |
| `compilar.bat` | Secuencia de compilación para Windows. |

## Compilación

Se requiere una distribución de LaTeX con la clase `IEEEtran`, `pdflatex`, `bibtex` y el estilo `IEEEtran.bst` (incluidos en MiKTeX y TeX Live). Desde la carpeta del aporte, ejecutar:

```bash
pdflatex -interaction=nonstopmode -halt-on-error aporte_roselyn.tex
bibtex aporte_roselyn
pdflatex -interaction=nonstopmode -halt-on-error aporte_roselyn.tex
pdflatex -interaction=nonstopmode -halt-on-error aporte_roselyn.tex
```

El paquete usa `\cite` con BibTeX; no debe compilarse con Biber. En Windows, el archivo `compilar.bat` ejecuta esta misma secuencia.

## Convenciones de citación e identificadores

- Las citas se escriben con `\cite{clave}` y se numeran automáticamente con el estilo IEEE. Las diez fuentes principales y su orden son: `iso29148` [1], `iso15288` [2], `iso12207` [3], `iso25010` [4], `pohl2025` [5], `swebok4` [6], `pmbok7` [7], `ireb2023` [8], `moore` [9] y `mavin2009` [10].
- Los requisitos y restricciones que emergen de las ocho perspectivas de contexto usan el prefijo `CTX-` (`CTX-01` … `CTX-16`), exclusivo de este aporte.

## Relación con el resto del informe

El tipo de sistema concluido para el PFC es un **sistema software-intensivo de información transaccional con un componente de recomendación basado en IA**. Para las interfaces del límite se propusieron **supuestos de diseño** —servicios REST sobre HTTPS con cargas JSON, además de las interfaces propias del SRI y del hardware POS—, que deben validarse con el propietario y con cada proveedor antes de cerrar la especificación.

Los requisitos `CTX-` complementan la tabla de requisitos del Investigador B: mientras su tabla cubre los requisitos funcionales y no funcionales con prefijos `RN`, `RS`, `RU`, `RF`, `RNF`, `RI`, `RR` y `RC`, los `CTX-` documentan los requisitos y restricciones que emergen del contexto, de modo que ambas tablas se enlazan por trazabilidad y no se solapan en identificadores. La delimitación del sistema y la lista de interesados apoyan además la sección 0 y los artefactos de elicitación del Investigador A, y las referencias conservan las claves bibliográficas y el orden compartidos por el equipo para la integración del informe final.
