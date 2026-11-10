DROP VIEW IF EXISTS reporte_mensual;

CREATE VIEW reporte_mensual AS
WITH movimientos_aprobados AS (
    SELECT
        id_usuario,
        substr(fecha_hora, 1, 7) AS mes,
        direccion,
        monto_cop
    FROM transaccion
    WHERE estado = 'aprobada'
),
dinero AS (
    SELECT
        id_usuario,
        mes,
        SUM(CASE WHEN direccion = 'entrada' THEN monto_cop ELSE 0 END) AS entradas_cop,
        SUM(CASE WHEN direccion = 'salida' THEN monto_cop ELSE 0 END) AS gastos_cop
    FROM movimientos_aprobados
    GROUP BY id_usuario, mes
),
senales AS (
    SELECT
        t.id_usuario,
        substr(t.fecha_hora, 1, 7) AS mes,
        SUM(CASE WHEN n.nombre = 'medio' THEN 1 ELSE 0 END) AS n_medio,
        SUM(CASE WHEN n.nombre = 'alto' THEN 1 ELSE 0 END) AS n_alto,
        SUM(CASE WHEN n.nombre = 'critico' THEN 1 ELSE 0 END) AS n_critico
    FROM transaccion AS t
    JOIN nivel_riesgo_transaccion AS n
        ON n.id_riesgo_tran = t.id_riesgo_tran
    GROUP BY t.id_usuario, mes
),
nivel AS (
    SELECT
        id_usuario,
        mes,
        n_medio,
        n_alto,
        n_critico,
        CASE
            WHEN n_critico >= 1 OR n_alto >= 3 THEN 'fuerte'
            WHEN n_alto >= 1 OR n_medio >= 3 THEN 'medio'
            ELSE 'bajo'
        END AS nivel_riesgo
    FROM senales
)
SELECT
    u.id_usuario,
    u.nombre,
    p.pais AS pais_residencia,
    d.mes,
    ROUND(d.entradas_cop, 2) AS entradas_cop,
    ROUND(d.gastos_cop, 2) AS gastos_cop,
    ROUND(d.entradas_cop - d.gastos_cop, 2) AS neto_cop,
    nv.nivel_riesgo,
    nv.n_medio,
    nv.n_alto,
    nv.n_critico,
    CASE
        WHEN nv.nivel_riesgo = 'fuerte' THEN 'bloqueado'
        ELSE 'activo'
    END AS estado_cuenta
FROM dinero AS d
JOIN usuarios AS u
    ON u.id_usuario = d.id_usuario
JOIN pais AS p
    ON p.id_pais = u.id_pais
JOIN nivel AS nv
    ON nv.id_usuario = d.id_usuario
    AND nv.mes = d.mes;
