# Calcula indicadores del tracker a partir de los CSV con datos ficticios.
# Uso, desde la carpeta del repositorio: python analysis/indicadores.py

import csv
from collections import defaultdict
from datetime import date
from pathlib import Path

CARPETA_TRACKER = Path(__file__).parent.parent / "tracker"

# Fecha fija para que el resultado sea repetible. Para datos reales: date.today()
FECHA_CORTE = date(2026, 11, 9)
DIAS_PARA_ESTAR_ACTUALIZADA = 14
DIAS_PARA_CONSIDERAR_DETENIDA = 30


def leer_csv(nombre):
    with open(CARPETA_TRACKER / nombre, encoding="utf-8", newline="") as archivo:
        return list(csv.DictReader(archivo))


def dias_desde(fecha_texto):
    return (FECHA_CORTE - date.fromisoformat(fecha_texto)).days


def porcentaje_actualizadas(activas):
    actualizadas = [
        i for i in activas
        if dias_desde(i["ultima_actualizacion"]) <= DIAS_PARA_ESTAR_ACTUALIZADA
    ]
    return 100 * len(actualizadas) / len(activas) if activas else 0


def promedio_por_etapa(historial):
    duraciones = defaultdict(list)
    for fila in historial:
        if fila["fecha_salida"]:  # Solo etapas ya terminadas
            entrada = date.fromisoformat(fila["fecha_entrada"])
            salida = date.fromisoformat(fila["fecha_salida"])
            duraciones[fila["etapa"]].append((salida - entrada).days)
    return {etapa: sum(d) / len(d) for etapa, d in duraciones.items()}


def iniciativas_detenidas(activas):
    return [
        i for i in activas
        if i["estado"] == "Detenida"
        or dias_desde(i["ultima_actualizacion"]) > DIAS_PARA_CONSIDERAR_DETENIDA
    ]


def main():
    iniciativas = leer_csv("iniciativas.csv")
    historial = leer_csv("historial_etapas.csv")
    activas = [i for i in iniciativas if i["estado"] != "Cerrada"]

    print(f"Fecha de corte: {FECHA_CORTE}")
    print(f"Iniciativas activas: {len(activas)} de {len(iniciativas)}")
    print(f"Actualizadas: {porcentaje_actualizadas(activas):.0f}%")

    print("\nDías promedio por etapa:")
    for etapa, promedio in promedio_por_etapa(historial).items():
        print(f"  {etapa}: {promedio:.1f}")

    print("\nIniciativas detenidas:")
    for i in iniciativas_detenidas(activas):
        print(f"  {i['id']} - {i['nombre']} ({i['responsable']})")


if __name__ == "__main__":
    main()