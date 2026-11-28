# Notas de defensa — FORM-SIM-01, avance de Kano

## Explicación breve

Se trabajó con el catálogo final `datos/requisitos.csv` y su versión en LaTeX `secciones/01_requisitos.tex`. El archivo `datos/01_requisitos.csv` corresponde a una lista anterior con otro esquema; no se usó como catálogo final. Las ocho características Kano y las dieciséis preguntas ya estaban en `datos/caracteristicas_kano.csv` y `datos/instrumento_kano.csv`, y se verificó que sus códigos apunten a requisitos existentes del catálogo final.

El formulario exportado contenía cinco filas y 16 preguntas por fila. Las preguntas del encabezado coinciden literalmente con las 16 preguntas de `datos/instrumento_kano.csv`. Las respuestas se transcribieron a los códigos 1--5 de la escala definitiva y se clasificaron con la matriz documentada en `secciones/03_kano.tex`: la fila es la respuesta funcional y la columna la disfuncional. Q se registró por separado y no decide la categoría predominante.

Se revisaron también los commits 1 y 2 y el avance de MoSCoW de Allan: `secciones/02_moscow.tex` y `datos/moscow.csv` aparecieron tras el pull (`9db01d9`). Sus veinte IDs coinciden con el catálogo final; el esfuerzo total es 92 puntos, el esfuerzo Must es 44 puntos y la proporción es 47,83 %, por debajo del 60 % documentado.

## Resultado obtenido

| Característica | Requisito | A | O | M | I | R | Q | Categoría |
|---|---|---:|---:|---:|---:|---:|---:|---|
| K01 | RF-04 | 1 | 0 | 1 | 3 | 0 | 0 | I |
| K02 | RF-06 | 0 | 3 | 0 | 2 | 0 | 0 | O |
| K03 | RF-08 | 1 | 2 | 1 | 1 | 0 | 0 | O |
| K04 | RF-10 | 0 | 3 | 1 | 1 | 0 | 0 | O |
| K05 | RF-11 | 1 | 2 | 1 | 1 | 0 | 0 | O |
| K06 | RNF-01 | 3 | 1 | 0 | 1 | 0 | 0 | A |
| K07 | RNF-04 | 2 | 0 | 1 | 1 | 0 | 1 | A |
| K08 | RNF-05 | 1 | 0 | 1 | 2 | 1 | 0 | I |

K03 y K05 empataron en la máxima frecuencia. Se aplicó la convención operativa ya documentada por el equipo: verificar Q y redacción, y conservar el orden M > O > A > I > R si el empate persiste. Por eso la categoría informada es O en ambos casos. K07 tiene una respuesta Q; se conserva en el registro pero no interviene en la categoría predominante.

## Limites que deben decirse con claridad

- Hay cinco formularios reales, pero solo cuatro códigos distintos: P01, P02, P04 y P05.
- Hay dos formularios con código P04. El de las 3:53:50 p. m. se conservó como respuesta real independiente; no se reasignó a P03 ni se descartó.
- No hay formulario de P03. No se creó esa participación.
- Rochina comunicó que las personas aceptaron el consentimiento. No se dispone de originales ni de datos para confirmar si fue verbal o escrita, la duración efectiva o los roles por código.
- No se publicaron nombres, cédulas, teléfonos, correos, firmas, audios, videos ni formularios originales.
- No se calcularon hashes SHA-256 porque no se proporcionó ningún archivo original privado. `MANIFIESTO.md` sigue sin filas; las filas preparadas están en `FILAS_MANIFIESTO.md`.
- La muestra es pequeña y no probabilística. Los resultados son descriptivos y no se generalizan.

## Posibles preguntas del docente

**¿Por qué hay dos P04?** Porque el CSV recibido tiene dos filas con ese código. La segunda se conservó tal cual para no inventar ni reasignar datos. La anomalía está declarada en el documento y en los archivos de datos.

**¿Por qué no aparece P03?** Porque no hay ninguna fila de P03 en el formulario exportado. No se imputó una respuesta ausente. Por eso se informan cinco formularios y cuatro códigos distintos.

**¿Cómo se obtuvo la categoría de cada característica?** Cada pareja de respuestas se clasificó con la matriz de Kano. Después se contaron A, O, M, I, R y Q por característica. La categoría predominante es la más frecuente entre A, O, M, I y R; Q se excluye. En K03 y K05 hubo empate y se aplicó la regla operativa documentada.

**¿Qué significa que K07 tenga Q?** Una pareja de respuestas fue inconsistente según la matriz. Se mantiene en el registro como dato real, se cuenta en la columna Q y no se usa para elegir la categoría predominante.

**¿El consentimiento está comprobado con formularios firmados?** No. La aceptación fue comunicada por Rochina. El repositorio no contiene originales ni permite verificar modalidad, duración o firma; por eso no se afirma nada adicional.

**¿Se usó inteligencia artificial?** Sí. Allan registró previamente el uso de ChatGPT (GPT-6). Para este avance, Roselyn usó OpenCode con Big Pickle para tabular, clasificar, redactar resultados y verificar la compilación. El uso está declarado en `secciones/07_uso_ia.tex`. El contenido fue revisado contra los archivos del repositorio y el CSV recibido.

**¿Los resultados son definitivos para priorizar el sistema?** No. Son un insumo comparativo de una muestra pequeña, con una anomalía de codificación y sin roles verificados. Deben contrastarse con MoSCoW y, cuando existan datos reales, con la votación ponderada.

**¿Por qué el script `scripts/analisis.py` no produce los tres órdenes?** En este entorno no hay intérprete de Python disponible. Además, la validación `check_kano` del script exige códigos únicos P01--P05, condición que no coincide con el CSV real. No se alteraron los datos para forzar esa validación; la discrepancia se documentó.
