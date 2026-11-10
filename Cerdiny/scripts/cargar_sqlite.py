"""Crea data/cerdiny.db y carga los CSV en las tablas del diagrama."""

from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DATA = RAIZ / "data"
SQL = RAIZ / "sql" / "crear_tablas.sql"
REPORTE = RAIZ / "sql" / "reporte_mensual.sql"
DB = DATA / "cerdiny.db"

VACIOS_A_NULO = {
    "id_comercio",
    "id_usuario_contra_parte",
    "id_error",
    "id_riesgo_anterior",
    "latitud",
    "longitud",
}

TABLAS = [
    "pais",
    "nivel_riesgo_usuario",
    "nivel_riesgo_transaccion",
    "categoria_comercio",
    "tipo_pago",
    "divisas",
    "errores",
    "comercio",
    "tasa_de_cambio",
    "usuarios",
    "historial_riesgo",
    "transaccion",
]


def leer_csv(nombre: str) -> tuple[list[str], list[tuple]]:
    ruta = DATA / f"{nombre}.csv"
    with ruta.open(encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        columnas = list(lector.fieldnames or [])
        filas = []
        for fila in lector:
            valores = []
            for columna in columnas:
                valor = fila[columna]
                if columna in VACIOS_A_NULO and valor == "":
                    valores.append(None)
                else:
                    valores.append(valor)
            filas.append(tuple(valores))
    return columnas, filas


def main() -> None:
    if DB.exists():
        DB.unlink()

    with sqlite3.connect(DB) as conexion:
        conexion.execute("PRAGMA foreign_keys = ON")
        conexion.executescript(SQL.read_text(encoding="utf-8"))
        for tabla in TABLAS:
            columnas, filas = leer_csv(tabla)
            marcas = ", ".join("?" for _ in columnas)
            nombres = ", ".join(columnas)
            conexion.executemany(
                f"INSERT INTO {tabla} ({nombres}) VALUES ({marcas})",
                filas,
            )
        conexion.executescript(REPORTE.read_text(encoding="utf-8"))
        conteos = {
            tabla: conexion.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]
            for tabla in TABLAS
        }

    print(f"base={DB}")
    for tabla, total in conteos.items():
        print(f"{tabla}={total}")


if __name__ == "__main__":
    main()
