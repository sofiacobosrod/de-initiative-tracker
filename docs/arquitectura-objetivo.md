# Arquitectura objetivo

> Propuesta conceptual. Este repositorio contiene solo un prototipo con CSV y Python.

| Componente | Función |
|---|---|
| Power Apps | Registrar y consultar iniciativas. |
| Base de datos (por definir) | Guardar iniciativas e historial de etapas. |
| Power Automate | Enviar recordatorios y coordinar la integración. |
| Jira | Gestionar el trabajo de las iniciativas que lo requieran. |
| Tablero de KPI (por definir) | Mostrar los indicadores. |

## Flujo general
1. El responsable registra o actualiza una iniciativa.
2. Cada cambio de etapa queda en el historial.
3. La información definida se sincroniza con Jira.
4. Un flujo programado detecta iniciativas sin actualizar y envía recordatorios.
5. El tablero calcula y muestra los KPI.

## Relación con PHVA
- **Planear:** registrar, validar y priorizar.
- **Hacer:** ejecutar las soluciones o automatizaciones.
- **Verificar:** revisar indicadores y resultados.
- **Actuar:** estandarizar y ajustar.