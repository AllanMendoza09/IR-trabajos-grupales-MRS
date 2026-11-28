# Filas preparadas para el manifiesto — FORM-SIM-01

Este archivo no sustituye a `MANIFIESTO.md` y no modifica el contenido de Allan. Solo prepara las filas que podrían incorporarse cuando Allan lo autorice y disponga de los originales privados.

**Hechos verificables:** el CSV exportado contiene cinco formularios con 16 respuestas completas cada uno, enviados el 27 de noviembre de 2026. Los códigos son P01, P04, P04, P02 y P05. No hay P03. Rochina comunicó que las personas aceptaron el consentimiento, pero no se proporcionaron originales, nombres de archivo, roles por código, duración efectiva ni huellas SHA-256.

| Código | Rol en el dominio | Técnica | Fecha | Hora de envío (CSV, GMT-5) | Duración | Consentimiento | Archivo privado | SHA-256 | Observación |
|---|---|---|---|---|---|---|---|---|---|
| P01 | No verificado | Kano | 2026-11-27 | 3:51:03 p. m. | No verificada | Aceptación comunicada por Rochina; modalidad no verificada | Nombre no proporcionado | No disponible | Formulario 1 |
| P04 | No verificado | Kano | 2026-11-27 | 3:51:14 p. m. | No verificada | Aceptación comunicada por Rochina; modalidad no verificada | Nombre no proporcionado | No disponible | Formulario 2 |
| P04 | No verificado | Kano | 2026-11-27 | 3:53:50 p. m. | No verificada | Aceptación comunicada por Rochina; modalidad no verificada | Nombre no proporcionado | No disponible | Formulario 3; se conserva como respuesta real independiente, no se reasigna a P03 |
| P02 | No verificado | Kano | 2026-11-27 | 4:01:36 p. m. | No verificada | Aceptación comunicada por Rochina; modalidad no verificada | Nombre no proporcionado | No disponible | Formulario 4 |
| P05 | No verificado | Kano | 2026-11-27 | 4:05:22 p. m. | No verificada | Aceptación comunicada por Rochina; modalidad no verificada | Nombre no proporcionado | No disponible | Formulario 5 |

**Estado:** cinco formularios, cuatro códigos distintos, ningún formulario de P03. No se inventan nombres, roles, duraciones, nombres de archivo ni hashes. Para calcular cada SHA-256 se necesita la ruta del original privado y ejecutar, sobre ese archivo, `Get-FileHash -Algorithm SHA256 -LiteralPath "RUTA_DEL_ORIGINAL"`.
