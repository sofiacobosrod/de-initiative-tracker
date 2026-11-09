# DE Initiative Tracker

> Proyecto académico. Todos los datos son ficticios.

## Qué es
Propuesta de un tracker para dar visibilidad y trazabilidad al estado, los responsables y el avance de las iniciativas de mejora, con la metodología PHVA.

## Objetivo
Saber en qué etapa está cada iniciativa, quién la lidera y cuáles están detenidas.

## Tipos de iniciativa
- **Proyecto de mejora:** Discovery → Mapeo del proceso → Análisis de capacidad → Causas raíz → Soluciones → Implementación → Seguimiento.
- **Iniciativa de productividad:** Registro → Validación inicial → Calificación → Automatización o Autoejecución → Validación final.

## Organización
- `docs/`: problema, preguntas, requerimientos, arquitectura y decisiones.
- `tracker/`: plantilla CSV con datos ficticios y diccionario de campos.
- `analysis/`: script que calcula los indicadores.
- `CHANGELOG.md`: registro de cambios.

## Cómo calcular los indicadores
Requiere Python 3. Desde la carpeta del repositorio:

`python analysis/indicadores.py`

## Indicadores
El script calcula tres indicadores principales:

- **Actualizadas:** porcentaje de iniciativas activas cuya `ultima_actualizacion` está dentro de los últimos 14 días. Se usa el umbral de 14 días para considerar una iniciativa actualizada.
- **Días promedio por etapa:** promedio de días que tarda una iniciativa en recorrer cada etapa terminada, según el historial de `fecha_entrada` y `fecha_salida`.
- **Iniciativas detenidas:** listado de iniciativas activas con `estado` igual a "Detenida" o cuya `ultima_actualizacion` supera los 30 días desde la fecha de corte. El umbral para considerar detención es de 30 días.