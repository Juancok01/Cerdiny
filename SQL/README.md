# 🗄️ Capa Transaccional (OLTP) - Base de Datos Local

Este directorio contiene los scripts SQL (DDL) utilizados para inicializar la base de datos PostgreSQL que simula el sistema transaccional bancario del proyecto **Cerdiny**.

## 📌 Arquitectura de Datos Relacional

El modelo de datos está diseñado con un enfoque OLTP clásico, garantizando la integridad referencial y restricciones de negocio. Consta de 4 tablas principales:

1. **`usuarios`**: Datos maestros de los clientes.
2. **`categorias`**: Catálogo que clasifica los tipos de movimientos (Ingresos, Gastos, Ahorros).
3. **`obligaciones`**: Registro de productos financieros de los usuarios (préstamos, metas de ahorro).
4. **`movimientos`**: Tabla transaccional o libro mayor que registra todas las operaciones (volumen de 50k+ registros).

![Diagrama Entidad-Relación de Cerdiny](/assets/diagrama_er.png)
