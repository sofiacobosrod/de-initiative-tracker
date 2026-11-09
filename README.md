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