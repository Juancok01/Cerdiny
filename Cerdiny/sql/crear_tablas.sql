PRAGMA foreign_keys = ON;

CREATE TABLE pais (
    id_pais INTEGER PRIMARY KEY,
    pais TEXT NOT NULL
);

CREATE TABLE nivel_riesgo_usuario (
    id_riesgo_usu INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE nivel_riesgo_transaccion (
    id_riesgo_tran INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE categoria_comercio (
    id_categoria INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE tipo_pago (
    id_tipo_pago INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE divisas (
    id_divisa INTEGER PRIMARY KEY,
    codigo TEXT NOT NULL,
    nombre TEXT NOT NULL
);

CREATE TABLE errores (
    id_error INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE comercio (
    id_comercio INTEGER PRIMARY KEY,
    id_categoria INTEGER NOT NULL REFERENCES categoria_comercio (id_categoria),
    id_pais INTEGER NOT NULL REFERENCES pais (id_pais),
    nombre TEXT NOT NULL
);

CREATE TABLE tasa_de_cambio (
    id_tasa_de_cambio INTEGER PRIMARY KEY,
    id_divisa INTEGER NOT NULL REFERENCES divisas (id_divisa),
    fecha TEXT NOT NULL,
    tasa NUMERIC NOT NULL
);

CREATE TABLE usuarios (
    id_usuario INTEGER PRIMARY KEY,
    id_riesgo_usu INTEGER NOT NULL REFERENCES nivel_riesgo_usuario (id_riesgo_usu),
    id_pais INTEGER NOT NULL REFERENCES pais (id_pais),
    nombre TEXT NOT NULL,
    fecha TEXT NOT NULL,
    estado TEXT NOT NULL
);

CREATE TABLE historial_riesgo (
    id_historial INTEGER PRIMARY KEY,
    id_riesgo_anterior INTEGER REFERENCES nivel_riesgo_usuario (id_riesgo_usu),
    id_riesgo_nuevo INTEGER NOT NULL REFERENCES nivel_riesgo_usuario (id_riesgo_usu),
    id_usuario INTEGER NOT NULL REFERENCES usuarios (id_usuario),
    fecha TEXT NOT NULL,
    motivo TEXT NOT NULL
);

CREATE TABLE transaccion (
    id_transaccion INTEGER PRIMARY KEY,
    id_pais INTEGER NOT NULL REFERENCES pais (id_pais),
    id_usuario INTEGER NOT NULL REFERENCES usuarios (id_usuario),
    id_comercio INTEGER REFERENCES comercio (id_comercio),
    id_usuario_contra_parte INTEGER REFERENCES usuarios (id_usuario),
    id_tipo_pago INTEGER NOT NULL REFERENCES tipo_pago (id_tipo_pago),
    id_divisa INTEGER NOT NULL REFERENCES divisas (id_divisa),
    id_tasa_de_cambio INTEGER NOT NULL REFERENCES tasa_de_cambio (id_tasa_de_cambio),
    id_error INTEGER REFERENCES errores (id_error),
    id_riesgo_tran INTEGER NOT NULL REFERENCES nivel_riesgo_transaccion (id_riesgo_tran),
    direccion TEXT NOT NULL,
    monto NUMERIC NOT NULL,
    monto_cop NUMERIC NOT NULL,
    fecha_hora TEXT NOT NULL,
    canal TEXT NOT NULL,
    estado TEXT NOT NULL,
    accion TEXT NOT NULL,
    latitud NUMERIC,
    longitud NUMERIC
);
