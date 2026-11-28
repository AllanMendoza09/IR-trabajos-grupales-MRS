# Diccionario de datos y reglas de consistencia

Las plantillas de respuestas y decisiones se crearon con solo encabezados. En este avance, las tabulaciones de Kano contienen respuestas reales exportadas del formulario; la votación y las decisiones continúan pendientes de datos reales. Los veinte requisitos del catálogo son propuestas para examen y validación por el equipo, no observaciones de campo.

## Archivos

- `requisitos.csv`: `id` (RF-01…RF-12 y RNF-01…RNF-08), `tipo` (RF/RNF), `nombre`, `texto`, `verificacion`. La clave `id` es única y no puede estar vacía.
- `moscow.csv`: `requisito_id` (clave foránea), `prioridad` (Must/Should/Could/Wont), `esfuerzo` (número positivo en unidad acordada por el equipo), `justificacion` (texto no vacío). Exactamente veinte filas al consolidarse.
- `caracteristicas_kano.csv`: `caracteristica_id` K01…K08, `requisito_id` asociado al catálogo, `caracteristica`. Cada requisito relacionado aparece una sola vez.
- `instrumento_kano.csv`: `caracteristica_id`, `tipo_pregunta` (funcional/disfuncional), `pregunta`, `opciones` (cinco opciones comunes). Dieciséis filas de instrumento.
- `respuestas_kano.csv`: `participante_id` P01…P05, `caracteristica_id`, `funcional`, `disfuncional`. En el avance real hay 40 registros, cinco formularios y cuatro códigos distintos: P01, P02, P04 dos veces y P05; no hay P03. La duplicidad se conserva y se declara, no se reasigna.
- `kano_respuestas.csv`: `participante`, `caracteristica`, `funcional`, `disfuncional`, `categoria`. Es el archivo principal de tabulación; contiene las mismas 40 parejas que `respuestas_kano.csv` con la categoría individual ya calculada.
- `kano_clasificacion.csv`: `caracteristica`, `id_requisito`, `A`, `O`, `M`, `I`, `R`, `Q`, `categoria`. Contiene ocho filas, una por característica K01–K08, con frecuencias y categoría predominante.
- `votos.csv`: `participante_id` P06…P08, `requisito_id`, `puntos` (entero >=0). Exactamente veinte registros por votante, con suma de cien puntos. No se permite repetir claves compuestas.
- `decision.csv`: `requisito_id`, `decision` (Incluir/Descartar), `orden_final` (entero consecutivo para los incluidos), `justificacion` (no vacía). Se completa mediante deliberación real de los miembros.

## Salidas calculadas

- `datos/calculos/orden_moscow.csv`, `datos/calculos/orden_votacion.csv`: veinte filas cada uno con rangos medios cuando existan empates.
- `datos/calculos/orden_kano.csv`: ocho categorías relacionadas con las características evaluadas. No es un ranking de los veinte requisitos.
- `datos/calculos/comparacion.csv`: vincula los tres métodos y conserva la ausencia legítima de una categoría Kano en doce requisitos.
- `datos/calculos/resumen.json`: validaciones y coeficiente de Spearman sobre rangos medios; no se guarda si faltan datos reales.

## Política de datos

P01–P05: cuestionario Kano. P06–P08: votación de cien puntos. Ningún registro publicado incluye nombres, correos, cédulas, teléfonos, archivos multimedia o consentimientos firmados. El nombre de un archivo de evidencia puede aparecer solo en el manifiesto; el archivo queda privado.
