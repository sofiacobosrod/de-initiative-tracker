# Diccionario de campos

> Todos los datos de los CSV son ficticios.

## iniciativas.csv
| Campo | Descripción | Ejemplo |
|---|---|---|
| id | Identificador único | INI-001 |
| nombre | Nombre de la iniciativa | Reducir reprocesos en Proceso A |
| tipo | Proyecto de mejora o Iniciativa de productividad | Proyecto de mejora |
| responsable | Persona a cargo | Persona A |
| equipo | Equipo a cargo | Equipo 1 |
| etapa_actual | Etapa en la que se encuentra | Causas raíz |
| estado | En curso, Detenida o Cerrada | En curso |
| fecha_inicio | Fecha de inicio (AAAA-MM-DD) | 2026-08-03 |
| ultima_actualizacion | Última actualización (AAAA-MM-DD) | 2026-11-02 |

## historial_etapas.csv
| Campo | Descripción | Ejemplo |
|---|---|---|
| id_iniciativa | Identificador de la iniciativa | INI-001 |
| etapa | Nombre de la etapa | Discovery |
| fecha_entrada | Fecha de entrada (AAAA-MM-DD) | 2026-08-03 |
| fecha_salida | Fecha de salida; vacía si sigue en curso | 2026-08-21 |