### USUARIO
*La dueña de la billetera.*

| Campo | Clave 
| :--- | :--- 
| usuario_id | PK
| nombre | | Ana Gómez |
| pais_residencia | | CO |
| fecha_registro | | 2024-03-12 |
| estado | | activo o bloqueado |
| nivel_riesgo | | bajo, medio o fuerte |


---

### CATEGORIA_COMERCIO

| Campo | Clave | Ejemplo |
| :--- | :--- | :--- |
| categoria_id | primaria | CAT01 |
| nombre | | Restaurantes |


---

### COMERCIO

| Campo | Clave | Ejemplo |
| :--- | :--- | :--- |
| comercio_id | primaria | C012 |
| nombre | | Café Bogotá |
| categoria_id | foránea | CAT01 |
| pais | | CO |

---

### TRANSACCION
*Un movimiento en la cuenta de una persona.*

| Campo | Clave | Ejemplo |
| :--- | :--- | :--- |
| transaccion_id | primaria | T10001 |
| usuario_id | foránea | U001 |
| comercio_id | foránea, opcional | C012 |
| usuario_contraparte_id | foránea, opcional | U018 |
| tipo | | pago_tarjeta, transferencia, nomina, retiro |
| direccion | | entrada o salida |
| monto | | 100 |
| divisa | | COP, USD, EUR, MXN |
| tasa_cambio_cop | | 4000 |
| monto_cop | | 400000 |
| fecha_hora | | 2026-10-07T14:30:00 |
| pais_operacion | | CO |
| canal | | app, web, cajero |
| lat, lon | opcionales | vacíos a veces |
| estado | | aprobada, retenida, rechazada, fallida |
| codigo_error | opcional | PASARELA_TIMEOUT |
| nivel_riesgo | | bajo, medio, alto, critico |
| accion | | aprobar, revisar, retener, rechazar |


---

### HISTORIAL_RIESGO
*El rastreo de la persona.*

| Campo | Clave | Ejemplo |
| :--- | :--- | :--- |
| historial_id | primaria | H001 |
| usuario_id | foránea | U001 |
| fecha | | 2026-10-07 |
| nivel_anterior | | medio |
| nivel_nuevo | | fuerte |
| motivo | | 1 transacción crítica en el mes |