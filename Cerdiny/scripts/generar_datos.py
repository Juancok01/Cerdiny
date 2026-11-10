"""Genera los datos de Cerdiny para septiembre de 2026.

El resultado sigue el diagrama entidad-relación: una fila por tabla,
con los identificadores que las claves foráneas esperan.
"""

from __future__ import annotations

import csv
import json
import random
from datetime import date, datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

SEED = 7
MES_INICIO = date(2026, 9, 1)
MES_FIN = date(2026, 9, 30)
RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "data"

DOS = Decimal("0.01")
SEIS = Decimal("0.000001")


def dinero(valor: Decimal) -> str:
    return str(valor.quantize(DOS, rounding=ROUND_HALF_UP))


def tasa_txt(valor: Decimal) -> str:
    return str(valor.quantize(SEIS, rounding=ROUND_HALF_UP))


def coord(valor: float) -> str:
    return tasa_txt(Decimal(str(valor)))


PAISES = [
    (1, "Colombia"),
    (2, "México"),
    (3, "Estados Unidos"),
    (4, "España"),
]

NIVEL_USUARIO = [(1, "bajo"), (2, "medio"), (3, "fuerte")]
NIVEL_TX = [(1, "bajo"), (2, "medio"), (3, "alto"), (4, "critico")]
NIVEL_USUARIO_ID = {nombre: id_ for id_, nombre in NIVEL_USUARIO}
NIVEL_TX_ID = {nombre: id_ for id_, nombre in NIVEL_TX}

CATEGORIAS = [
    (1, "Restaurantes"),
    (2, "Tecnología"),
    (3, "Supermercados"),
    (4, "Transporte"),
    (5, "Entretenimiento"),
    (6, "Servicios"),
]

TIPOS_PAGO = [
    (1, "pago_tarjeta"),
    (2, "transferencia"),
    (3, "nomina"),
    (4, "retiro"),
]
TIPO_ID = {nombre: id_ for id_, nombre in TIPOS_PAGO}

DIVISAS = [
    (1, "COP", "Peso colombiano"),
    (2, "USD", "Dólar"),
    (3, "EUR", "Euro"),
    (4, "MXN", "Peso mexicano"),
]
DIVISA_ID = {codigo: id_ for id_, codigo, _ in DIVISAS}
MONEDA_PAIS = {1: "COP", 2: "MXN", 3: "USD", 4: "EUR"}

ERRORES = [
    (1, "PASARELA_TIMEOUT"),
    (2, "PASARELA_NO_DISPONIBLE"),
    (3, "FONDOS_INSUFICIENTES"),
]

# id, nombre, categoria, pais
COMERCIOS = [
    (1, "Café Bogotá", 1, 1),
    (2, "Arepa Real", 1, 1),
    (3, "Mercado Central", 3, 1),
    (4, "TecnoAndes", 2, 1),
    (5, "Metro Línea", 4, 1),
    (6, "Cine Plaza", 5, 1),
    (7, "Servicios del Norte", 6, 1),
    (8, "Panadería Luna", 1, 1),
    (9, "Super Ahorro", 3, 1),
    (10, "Móvil Store", 2, 1),
    (11, "Taxi Verde", 4, 1),
    (12, "Teatro Libre", 5, 1),
    (13, "Clínica del Parque", 6, 1),
    (14, "Hamburguesas 24", 1, 1),
    (15, "Ferretería Centro", 6, 1),
    (16, "Mercado Express", 3, 1),
    (17, "Tacos Reforma", 1, 2),
    (18, "Super Roma", 3, 2),
    (19, "Tech Polanco", 2, 2),
    (20, "Metro CDMX", 4, 2),
    (21, "Cine Condesa", 5, 2),
    (22, "Pago de Servicios MX", 6, 2),
    (23, "Brooklyn Deli", 1, 3),
    (24, "Market 5th", 3, 3),
    (25, "Circuit Store", 2, 3),
    (26, "NY Transit", 4, 3),
    (27, "Broadway Tickets", 5, 3),
    (28, "Casa Pepe", 1, 4),
    (29, "Mercado Salamanca", 3, 4),
    (30, "Metro Madrid", 4, 4),
]

NOMBRES = [
    "Ana Gómez",
    "Camila Restrepo",
    "Juan Pérez",
    "Valentina Ruiz",
    "Santiago Morales",
    "Mariana López",
    "Andrés Herrera",
    "Laura Castillo",
    "Daniel Mejía",
    "Sofía Vargas",
    "Mateo Jiménez",
    "Isabella Torres",
    "Nicolás Rojas",
    "Gabriela Díaz",
    "Samuel Ortiz",
    "Lucía Fernández",
    "Diego Ramírez",
    "Luis Ramírez",
    "Paula Gutiérrez",
    "Tomás Aguilar",
    "Renata Salazar",
    "Emilio Cruz",
    "Antonella Peña",
    "Martín Ibáñez",
    "Elena Duarte",
    "Joaquín Navarro",
    "Regina Solís",
    "Fernando Pardo",
    "Camila Herrera",
    "Sebastián León",
    "Jimena Cruz",
    "Diego Hernández",
    "Paulina Vega",
    "Alejandro Ruiz",
    "Fernanda Soto",
    "Hugo Delgado",
    "Emma Brooks",
    "Noah Carter",
    "Olivia Bennett",
    "Liam Foster",
    "Sophia Reed",
    "Ethan Price",
    "Mia Collins",
    "Lucía Navarro",
    "Martina Iglesias",
    "Hugo Serrano",
    "Alba Romero",
    "Pablo Méndez",
    "Carla Domínguez",
    "Inés Cabrera",
]

# País de residencia: 30 Colombia, 8 México, 7 Estados Unidos, 5 España.
PAIS_USUARIO = [1] * 30 + [2] * 8 + [3] * 7 + [4] * 5

# Usuarios a los que se les inyectan señales. El nivel final se calcula
# después, contando las transacciones, no se escribe a mano.
PERFILES = {
    1: "critico",
    2: "critico",
    3: "tres_altos",
    4: "un_alto",
    5: "un_alto",
    6: "varios_medios",
    7: "varios_medios",
    8: "varios_medios",
    9: "varios_medios",
}

CIUDAD = {
    1: (4.7110, -74.0721),
    2: (19.4326, -99.1332),
    3: (40.7128, -74.0060),
    4: (40.4168, -3.7038),
}

RANGOS_COP = {
    1: (12_000, 150_000),
    2: (80_000, 2_500_000),
    3: (20_000, 400_000),
    4: (5_000, 80_000),
    5: (15_000, 200_000),
    6: (30_000, 500_000),
}


def dias_del_mes() -> list[date]:
    dias = []
    actual = MES_INICIO
    while actual <= MES_FIN:
        dias.append(actual)
        actual += timedelta(days=1)
    return dias


def construir_tasas() -> tuple[list[dict], dict[tuple[int, date], dict]]:
    rng = random.Random(SEED)
    bases = {
        1: Decimal("1"),
        2: Decimal("4000"),
        3: Decimal("4400"),
        4: Decimal("220"),
    }
    filas = []
    indice: dict[tuple[int, date], dict] = {}
    id_tasa = 1
    for dia in dias_del_mes():
        for id_divisa, base in bases.items():
            if id_divisa == 1:
                valor = base
            else:
                variacion = Decimal(str(rng.uniform(-0.015, 0.015)))
                valor = base * (Decimal("1") + variacion)
            fila = {
                "id_tasa_de_cambio": id_tasa,
                "id_divisa": id_divisa,
                "fecha": dia.isoformat(),
                "tasa": tasa_txt(valor),
                "_tasa": valor.quantize(SEIS, rounding=ROUND_HALF_UP),
                "_fecha": dia,
            }
            filas.append(fila)
            indice[(id_divisa, dia)] = fila
            id_tasa += 1
    return filas, indice


def monto_en_divisa(rng: random.Random, codigo: str, minimo_cop: int, maximo_cop: int, tasa: Decimal) -> Decimal:
    cop = Decimal(rng.randint(minimo_cop, maximo_cop))
    if codigo == "COP":
        return cop.quantize(DOS, rounding=ROUND_HALF_UP)
    return (cop / tasa).quantize(DOS, rounding=ROUND_HALF_UP)


def geolocalizacion(rng: random.Random, id_pais: int, vacia: bool) -> tuple[str, str]:
    if vacia:
        return "", ""
    lat, lon = CIUDAD[id_pais]
    return coord(lat + rng.uniform(-0.04, 0.04)), coord(lon + rng.uniform(-0.04, 0.04))


class Generador:
    def __init__(self) -> None:
        self.rng = random.Random(SEED)
        self.tasas, self.tasa_por_dia = construir_tasas()
        self.transacciones: list[dict] = []
        self.siguiente_id = 1
        self.comercios_por_pais: dict[int, list[tuple]] = {}
        for comercio in COMERCIOS:
            self.comercios_por_pais.setdefault(comercio[3], []).append(comercio)

    def fecha_aleatoria(self, hora_min: int, hora_max: int) -> datetime:
        dia = self.rng.choice(dias_del_mes())
        return datetime(dia.year, dia.month, dia.day, self.rng.randint(hora_min, hora_max), self.rng.randint(0, 59), 0)

    def tasa_de(self, codigo: str, momento: datetime) -> dict:
        return self.tasa_por_dia[(DIVISA_ID[codigo], momento.date())]

    def nueva(
        self,
        *,
        id_usuario: int,
        id_pais: int,
        tipo: str,
        direccion: str,
        codigo_divisa: str,
        monto: Decimal,
        momento: datetime,
        nivel: str,
        canal: str,
        id_comercio: int | None = None,
        id_contraparte: int | None = None,
        id_error: int | None = None,
        latitud: str = "",
        longitud: str = "",
    ) -> dict:
        tasa = self.tasa_de(codigo_divisa, momento)
        monto_cop = (monto * tasa["_tasa"]).quantize(DOS, rounding=ROUND_HALF_UP)
        accion, estado = self.decision(nivel, id_error)
        fila = {
            "id_transaccion": self.siguiente_id,
            "id_pais": id_pais,
            "id_usuario": id_usuario,
            "id_comercio": id_comercio or "",
            "id_usuario_contra_parte": id_contraparte or "",
            "id_tipo_pago": TIPO_ID[tipo],
            "id_divisa": DIVISA_ID[codigo_divisa],
            "id_tasa_de_cambio": tasa["id_tasa_de_cambio"],
            "id_error": id_error or "",
            "id_riesgo_tran": NIVEL_TX_ID[nivel],
            "direccion": direccion,
            "monto": dinero(monto),
            "monto_cop": dinero(monto_cop),
            "fecha_hora": momento.isoformat(timespec="seconds"),
            "canal": canal,
            "estado": estado,
            "accion": accion,
            "latitud": latitud,
            "longitud": longitud,
        }
        self.siguiente_id += 1
        self.transacciones.append(fila)
        return fila

    @staticmethod
    def decision(nivel: str, id_error: int | None) -> tuple[str, str]:
        if id_error:
            return {
                "bajo": "aprobar",
                "medio": "revisar",
                "alto": "retener",
                "critico": "rechazar",
            }[nivel], "fallida"
        return {
            "bajo": ("aprobar", "aprobada"),
            "medio": ("revisar", "aprobada"),
            "alto": ("retener", "retenida"),
            "critico": ("rechazar", "rechazada"),
        }[nivel]

    def casos_de_ana(self) -> None:
        """Nómina, café en Bogotá y cobro crítico. Quedan al inicio del archivo."""
        nomina = self.tasa_de("COP", datetime(2026, 9, 1, 8, 0, 0))
        self.nueva(
            id_usuario=1,
            id_pais=1,
            tipo="nomina",
            direccion="entrada",
            codigo_divisa="COP",
            monto=Decimal("2500000.00"),
            momento=datetime(2026, 9, 1, 8, 0, 0),
            nivel="bajo",
            canal="app",
        )
        self.nueva(
            id_usuario=1,
            id_pais=1,
            tipo="pago_tarjeta",
            direccion="salida",
            codigo_divisa="COP",
            monto=Decimal("45000.00"),
            momento=datetime(2026, 9, 12, 14, 30, 0),
            nivel="bajo",
            canal="app",
            id_comercio=1,
            latitud=coord(4.7110),
            longitud=coord(-74.0721),
        )
        self.nueva(
            id_usuario=1,
            id_pais=2,
            tipo="pago_tarjeta",
            direccion="salida",
            codigo_divisa="MXN",
            monto=Decimal("180.00"),
            momento=datetime(2026, 9, 20, 15, 10, 0),
            nivel="critico",
            canal="app",
            id_comercio=1,
            latitud=coord(19.4326),
            longitud=coord(-99.1332),
        )
        tasa_usd = self.tasa_de("USD", datetime(2026, 9, 18, 11, 0, 0))
        monto = Decimal("100.00")
        momento = datetime(2026, 9, 18, 11, 0, 0)
        self.nueva(
            id_usuario=1,
            id_pais=1,
            tipo="transferencia",
            direccion="salida",
            codigo_divisa="USD",
            monto=monto,
            momento=momento,
            nivel="bajo",
            canal="app",
            id_contraparte=18,
        )
        self.nueva(
            id_usuario=18,
            id_pais=1,
            tipo="transferencia",
            direccion="entrada",
            codigo_divisa="USD",
            monto=monto,
            momento=momento,
            nivel="bajo",
            canal="app",
            id_contraparte=1,
        )
        # La tasa se usa arriba; se deja referenciada para que el ejemplo no quede suelto.
        assert tasa_usd["id_divisa"] == DIVISA_ID["USD"]
        assert nomina["id_divisa"] == DIVISA_ID["COP"]

    def nomina(self, id_usuario: int, id_pais: int) -> None:
        if id_usuario == 1:
            return
        codigo = MONEDA_PAIS[id_pais]
        momento = datetime(2026, 9, 1, 8, self.rng.randint(0, 40), 0)
        tasa = self.tasa_de(codigo, momento)
        self.nueva(
            id_usuario=id_usuario,
            id_pais=id_pais,
            tipo="nomina",
            direccion="entrada",
            codigo_divisa=codigo,
            monto=monto_en_divisa(self.rng, codigo, 1_800_000, 4_200_000, tasa["_tasa"]),
            momento=momento,
            nivel="bajo",
            canal="app",
        )

    def pago_domestico(self, id_usuario: int, id_pais: int, extranjero: bool) -> None:
        comercio = self.rng.choice(self.comercios_por_pais[id_pais])
        codigo = self.rng.choice(["USD", "EUR", "MXN"]) if extranjero else MONEDA_PAIS[id_pais]
        momento = self.fecha_aleatoria(8, 21)
        tasa = self.tasa_de(codigo, momento)
        minimo, maximo = RANGOS_COP[comercio[2]]
        vacia = self.rng.random() < 0.12
        lat, lon = geolocalizacion(self.rng, id_pais, vacia)
        self.nueva(
            id_usuario=id_usuario,
            id_pais=id_pais,
            tipo="pago_tarjeta",
            direccion="salida",
            codigo_divisa=codigo,
            monto=monto_en_divisa(self.rng, codigo, minimo, maximo, tasa["_tasa"]),
            momento=momento,
            nivel="bajo",
            canal=self.rng.choice(["app", "app", "web"]),
            id_comercio=comercio[0],
            latitud=lat,
            longitud=lon,
        )

    def retiro(self, id_usuario: int, id_pais: int) -> None:
        codigo = MONEDA_PAIS[id_pais]
        momento = self.fecha_aleatoria(8, 20)
        tasa = self.tasa_de(codigo, momento)
        self.nueva(
            id_usuario=id_usuario,
            id_pais=id_pais,
            tipo="retiro",
            direccion="salida",
            codigo_divisa=codigo,
            monto=monto_en_divisa(self.rng, codigo, 20_000, 400_000, tasa["_tasa"]),
            momento=momento,
            nivel="bajo",
            canal="cajero",
        )

    def transferencia(self, id_usuario: int, id_pais: int) -> None:
        otros = [i for i in range(1, 51) if i != id_usuario]
        destino = self.rng.choice(otros)
        codigo = MONEDA_PAIS[id_pais]
        if self.rng.random() < 0.25:
            codigo = self.rng.choice(["USD", "EUR", "MXN", "COP"])
        momento = self.fecha_aleatoria(8, 21)
        tasa = self.tasa_de(codigo, momento)
        monto = monto_en_divisa(self.rng, codigo, 10_000, 300_000, tasa["_tasa"])
        falla = self.rng.random() < 0.04
        self.nueva(
            id_usuario=id_usuario,
            id_pais=id_pais,
            tipo="transferencia",
            direccion="salida",
            codigo_divisa=codigo,
            monto=monto,
            momento=momento,
            nivel="bajo",
            canal="app",
            id_contraparte=destino,
            id_error=self.rng.choice([1, 2, 3]) if falla else None,
        )
        if falla:
            return
        self.nueva(
            id_usuario=destino,
            id_pais=id_pais,
            tipo="transferencia",
            direccion="entrada",
            codigo_divisa=codigo,
            monto=monto,
            momento=momento,
            nivel="bajo",
            canal="app",
            id_contraparte=id_usuario,
        )

    def movimiento_normal(self, id_usuario: int, id_pais: int) -> None:
        sorteo = self.rng.random()
        if sorteo < 0.68:
            self.pago_domestico(id_usuario, id_pais, extranjero=False)
        elif sorteo < 0.80:
            self.pago_domestico(id_usuario, id_pais, extranjero=True)
        elif sorteo < 0.92:
            self.transferencia(id_usuario, id_pais)
        else:
            self.retiro(id_usuario, id_pais)

    def senal(self, id_usuario: int, id_pais_usuario: int, nivel: str) -> None:
        if nivel == "critico":
            comercio = COMERCIOS[0]
            pais_operacion = 2 if comercio[3] != 2 else 1
            codigo = MONEDA_PAIS[pais_operacion]
            momento = self.fecha_aleatoria(12, 18)
        elif nivel == "alto":
            comercio = self.rng.choice([c for c in COMERCIOS if c[3] != id_pais_usuario])
            pais_operacion = comercio[3]
            codigo = MONEDA_PAIS[pais_operacion]
            momento = self.fecha_aleatoria(0, 4)
        else:
            comercio = self.rng.choice([c for c in COMERCIOS if c[3] != id_pais_usuario])
            pais_operacion = comercio[3]
            codigo = MONEDA_PAIS[pais_operacion]
            momento = self.fecha_aleatoria(10, 19)
        tasa = self.tasa_de(codigo, momento)
        minimo, maximo = RANGOS_COP[comercio[2]]
        lat, lon = geolocalizacion(self.rng, pais_operacion, False)
        self.nueva(
            id_usuario=id_usuario,
            id_pais=pais_operacion,
            tipo="pago_tarjeta",
            direccion="salida",
            codigo_divisa=codigo,
            monto=monto_en_divisa(self.rng, codigo, minimo, maximo, tasa["_tasa"]),
            momento=momento,
            nivel=nivel,
            canal="app",
            id_comercio=comercio[0],
            latitud=lat,
            longitud=lon,
        )

    def inyectar_perfil(self, id_usuario: int, id_pais: int) -> None:
        perfil = PERFILES.get(id_usuario)
        if perfil is None or id_usuario == 1:
            return
        if perfil == "critico":
            self.senal(id_usuario, id_pais, "critico")
        elif perfil == "tres_altos":
            for _ in range(3):
                self.senal(id_usuario, id_pais, "alto")
        elif perfil == "un_alto":
            self.senal(id_usuario, id_pais, "alto")
        elif perfil == "varios_medios":
            for _ in range(4):
                self.senal(id_usuario, id_pais, "medio")

    def fallos_de_pasarela(self) -> None:
        """Algunos pagos normales fallan. El caso crítico de Ana no se toca."""
        for fila in self.transacciones:
            if fila["id_transaccion"] <= 5:
                continue
            if fila["id_tipo_pago"] == TIPO_ID["transferencia"]:
                continue
            if fila["id_riesgo_tran"] != NIVEL_TX_ID["bajo"]:
                continue
            if fila["direccion"] != "salida" or fila["id_error"]:
                continue
            if self.rng.random() < 0.03:
                fila["id_error"] = self.rng.choice([1, 2, 3])
                fila["estado"] = "fallida"

    def construir(self) -> None:
        self.casos_de_ana()
        for id_usuario, id_pais in enumerate(PAIS_USUARIO, start=1):
            self.nomina(id_usuario, id_pais)
            for _ in range(self.rng.randint(70, 95)):
                self.movimiento_normal(id_usuario, id_pais)
            self.inyectar_perfil(id_usuario, id_pais)
        self.fallos_de_pasarela()
        self.transacciones.sort(key=lambda fila: (fila["fecha_hora"], fila["id_transaccion"]))


def nivel_persona(conteo: dict[str, int]) -> tuple[str, str, str]:
    if conteo["critico"] >= 1:
        texto = "transacción crítica" if conteo["critico"] == 1 else "transacciones críticas"
        return "fuerte", "bloqueado", f"{conteo['critico']} {texto} en el mes"
    if conteo["alto"] >= 3:
        return "fuerte", "bloqueado", f"{conteo['alto']} transacciones de riesgo alto en el mes"
    if conteo["alto"] >= 1:
        texto = "transacción de riesgo alto" if conteo["alto"] == 1 else "transacciones de riesgo alto"
        return "medio", "activo", f"{conteo['alto']} {texto} en el mes"
    if conteo["medio"] >= 3:
        return "medio", "activo", f"{conteo['medio']} transacciones de riesgo medio en el mes"
    return "bajo", "activo", "Sin transacciones de riesgo en el mes"


def usuarios_e_historial(transacciones: list[dict]) -> tuple[list[dict], list[dict]]:
    conteos = {id_usuario: {"bajo": 0, "medio": 0, "alto": 0, "critico": 0} for id_usuario in range(1, 51)}
    nombres_nivel = {id_: nombre for id_, nombre in NIVEL_TX}
    for fila in transacciones:
        nombre = nombres_nivel[fila["id_riesgo_tran"]]
        conteos[fila["id_usuario"]][nombre] += 1

    rng = random.Random(SEED)
    usuarios = []
    historial = []
    for id_usuario, nombre in enumerate(NOMBRES, start=1):
        nivel, estado, motivo = nivel_persona(conteos[id_usuario])
        alta = date(2024, 1, 1) + timedelta(days=rng.randint(0, 600))
        usuarios.append(
            {
                "id_usuario": id_usuario,
                "id_riesgo_usu": NIVEL_USUARIO_ID[nivel],
                "id_pais": PAIS_USUARIO[id_usuario - 1],
                "nombre": nombre,
                "fecha": alta.isoformat(),
                "estado": estado,
            }
        )
        historial.append(
            {
                "id_historial": id_usuario,
                "id_riesgo_anterior": "",
                "id_riesgo_nuevo": NIVEL_USUARIO_ID[nivel],
                "id_usuario": id_usuario,
                "fecha": MES_FIN.isoformat(),
                "motivo": motivo,
            }
        )
    return usuarios, historial


def escribir_csv(ruta: Path, filas: list[dict], columnas: list[str]) -> None:
    with ruta.open("w", newline="", encoding="utf-8-sig") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=columnas, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(filas)


def a_json(fila: dict) -> dict:
    salida = {}
    for clave, valor in fila.items():
        if clave.startswith("_"):
            continue
        salida[clave] = None if valor == "" else valor
    return salida


def main() -> None:
    SALIDA.mkdir(parents=True, exist_ok=True)
    generador = Generador()
    generador.construir()
    usuarios, historial = usuarios_e_historial(generador.transacciones)

    catalogos = {
        "pais": ([{"id_pais": id_, "pais": nombre} for id_, nombre in PAISES], ["id_pais", "pais"]),
        "nivel_riesgo_usuario": (
            [{"id_riesgo_usu": id_, "nombre": nombre} for id_, nombre in NIVEL_USUARIO],
            ["id_riesgo_usu", "nombre"],
        ),
        "nivel_riesgo_transaccion": (
            [{"id_riesgo_tran": id_, "nombre": nombre} for id_, nombre in NIVEL_TX],
            ["id_riesgo_tran", "nombre"],
        ),
        "categoria_comercio": (
            [{"id_categoria": id_, "nombre": nombre} for id_, nombre in CATEGORIAS],
            ["id_categoria", "nombre"],
        ),
        "tipo_pago": (
            [{"id_tipo_pago": id_, "nombre": nombre} for id_, nombre in TIPOS_PAGO],
            ["id_tipo_pago", "nombre"],
        ),
        "divisas": (
            [{"id_divisa": id_, "codigo": codigo, "nombre": nombre} for id_, codigo, nombre in DIVISAS],
            ["id_divisa", "codigo", "nombre"],
        ),
        "errores": (
            [{"id_error": id_, "nombre": nombre} for id_, nombre in ERRORES],
            ["id_error", "nombre"],
        ),
        "comercio": (
            [
                {"id_comercio": id_, "id_categoria": categoria, "id_pais": pais, "nombre": nombre}
                for id_, nombre, categoria, pais in COMERCIOS
            ],
            ["id_comercio", "id_categoria", "id_pais", "nombre"],
        ),
    }
    for nombre, (filas, columnas) in catalogos.items():
        escribir_csv(SALIDA / f"{nombre}.csv", filas, columnas)

    tasas_publicas = [
        {clave: valor for clave, valor in fila.items() if not clave.startswith("_")}
        for fila in generador.tasas
    ]
    escribir_csv(
        SALIDA / "tasa_de_cambio.csv",
        tasas_publicas,
        ["id_tasa_de_cambio", "id_divisa", "fecha", "tasa"],
    )
    escribir_csv(
        SALIDA / "usuarios.csv",
        usuarios,
        ["id_usuario", "id_riesgo_usu", "id_pais", "nombre", "fecha", "estado"],
    )
    escribir_csv(
        SALIDA / "historial_riesgo.csv",
        historial,
        ["id_historial", "id_riesgo_anterior", "id_riesgo_nuevo", "id_usuario", "fecha", "motivo"],
    )
    columnas_tx = [
        "id_transaccion",
        "id_pais",
        "id_usuario",
        "id_comercio",
        "id_usuario_contra_parte",
        "id_tipo_pago",
        "id_divisa",
        "id_tasa_de_cambio",
        "id_error",
        "id_riesgo_tran",
        "direccion",
        "monto",
        "monto_cop",
        "fecha_hora",
        "canal",
        "estado",
        "accion",
        "latitud",
        "longitud",
    ]
    escribir_csv(SALIDA / "transaccion.csv", generador.transacciones, columnas_tx)
    with (SALIDA / "transaccion.json").open("w", encoding="utf-8") as archivo:
        json.dump([a_json(fila) for fila in generador.transacciones], archivo, ensure_ascii=False)

    ana = [fila for fila in generador.transacciones if fila["id_transaccion"] in {1, 2, 3}]
    ana.sort(key=lambda fila: fila["id_transaccion"])
    with (SALIDA / "ejemplos_ana.json").open("w", encoding="utf-8") as archivo:
        json.dump([a_json(fila) for fila in ana], archivo, ensure_ascii=False, indent=2)

    print(f"transacciones={len(generador.transacciones)}")
    print(f"usuarios={len(usuarios)} historial={len(historial)}")
    ana_usuario = usuarios[0]
    print(f"ana nivel={ana_usuario['id_riesgo_usu']} estado={ana_usuario['estado']}")
    for fila in ana:
        print(
            f"id={fila['id_transaccion']} tipo={fila['id_tipo_pago']} "
            f"pais={fila['id_pais']} comercio={fila['id_comercio']} "
            f"riesgo={fila['id_riesgo_tran']} estado={fila['estado']} monto={fila['monto']}"
        )


if __name__ == "__main__":
    main()
