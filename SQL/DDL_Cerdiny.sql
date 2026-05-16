--DDL Cerdiny

create table usuarios(
    id_usuario varchar primary key not null,
    email varchar not null,
    password_hash varchar not null,
    nombre_completo varchar not null,
    estado_cuenta varchar not null,
    updated_at timestamp,
    created_at timestamp default now()
);

comment on table usuarios is 'Contiene la información personal, credenciales de acceso y estado general de los usuarios en la plataforma cerdiny.';
comment on column usuarios.id_usuario is 'Identificador único alfanumérico del usuario. llave primaria (pk).';
comment on column usuarios.email is 'Correo electrónico principal del usuario. se utiliza como método de contacto y credencial de login.';
comment on column usuarios.password_hash is 'Hash criptográfico de la contraseña del usuario. nunca se almacena en texto plano por normativas de seguridad.';
comment on column usuarios.nombre_completo is 'Nombre y apellidos completos del cliente.';
comment on column usuarios.estado_cuenta is 'Estado operativo actual del usuario en el sistema (ej. activo, suspendido, cancelado).';
comment on column usuarios.updated_at is 'Timestamp de auditoría que registra la fecha y hora de la última modificación de cualquier campo del registro.';
comment on column usuarios.created_at is 'Timestamp de auditoría que indica la fecha y hora exacta en que el usuario fue registrado en el sistema.';

create table categorias(
    id_categoria int primary key not null,
    nombre_categoria varchar not null,
    tipo_movimiento varchar not null,
    id_categoria_padre int,
    updated_at timestamp,
    created_at timestamp default now(),
    constraint fk_categoria_padre 
        foreign key (id_categoria_padre) 
        references categorias(id_categoria)
);

comment on table categorias is 'Define la clasificación taxonómica de los movimientos financieros y permite estructurar subcategorías a través de una relación recursiva.';
comment on column categorias.id_categoria is 'Identificador único numérico de la categoría. llave primaria (pk).';
comment on column categorias.nombre_categoria is 'Nombre descriptivo de la clasificación (ej. alimentación, salario mensual, transporte público).';
comment on column categorias.tipo_movimiento is 'Clasificación de alto nivel que define el impacto financiero (ej. ingreso, gasto, ahorro). crucial para el cálculo de balances y métricas clave.';
comment on column categorias.id_categoria_padre is 'Llave foránea recursiva que apunta al id_categoria de esta misma tabla. permite crear árboles de categorías. un valor null indica que es una categoría raíz (nivel 1).';
comment on column categorias.updated_at is 'Timestamp de auditoría que registra la última modificación de los datos de la categoría.';
comment on column categorias.created_at is 'Timestamp de auditoría que indica cuándo se creó la categoría en el catálogo.';

create table obligaciones(
    id_obligacion varchar primary key not null,
    id_usuario varchar not null,
    id_categoria int not null,
    entidad_o_persona varchar,
    tipo_obligacion varchar not null,
    monto_capital float not null,
    tasa_interes_mensual float,
    numero_cuotas int,
    valor_cuota_mensual float,
    updated_at timestamp,
    created_at timestamp default now(),
    constraint fk_obligacion_usuario 
        foreign key (id_usuario) references usuarios(id_usuario),
    constraint fk_obligacion_categoria 
        foreign key (id_categoria) references categorias(id_categoria)
);

comment on table obligaciones is 'Registro de los productos financieros, deudas o metas de ahorro de los usuarios. establece el contexto y las condiciones para agrupar múltiples movimientos financieros.';
comment on column obligaciones.id_obligacion is 'Identificador único alfanumérico de la obligación financiera. llave primaria (pk).';
comment on column obligaciones.id_usuario is 'Llave foránea que asocia la obligación con un cliente específico de la tabla usuarios.';
comment on column obligaciones.id_categoria is 'Llave foránea que clasifica la obligación (ej. crédito hipotecario, tarjeta de crédito, fondo de emergencia) referenciando la tabla categorias.';
comment on column obligaciones.entidad_o_persona is 'Nombre de la institución financiera, banco o tercero asociado a la obligación.';
comment on column obligaciones.tipo_obligacion is 'Naturaleza del producto financiero (ej. activo/ahorro, pasivo/deuda).';
comment on column obligaciones.monto_capital is 'Monto total del principal prestado o la meta de ahorro total proyectada, sin incluir intereses.';
comment on column obligaciones.tasa_interes_mensual is 'Tasa de interés aplicada a la obligación expresada en formato mensual (ej. 0.015 para 1.5%).';
comment on column obligaciones.numero_cuotas is 'Plazo total acordado para liquidar la obligación o alcanzar la meta, expresado en meses.';
comment on column obligaciones.valor_cuota_mensual is 'Monto fijo calculado a pagar o ahorrar mensualmente para cumplir con la obligación en el plazo pactado.';
comment on column obligaciones.updated_at is 'Timestamp de auditoría que registra la última actualización de las condiciones de la obligación.';
comment on column obligaciones.created_at is 'Timestamp de auditoría de creación del registro en el sistema.';

create table movimientos(
    id_movimiento varchar primary key not null,
    id_usuario varchar not null,
    id_categoria int not null,
    id_obligacion varchar null, 
    monto float not null,
    descripcion_opcional varchar,
    updated_at timestamp,
    created_at timestamp default now(),
    constraint fk_movimiento_usuario foreign key (id_usuario) 
        references usuarios(id_usuario),
    constraint fk_movimiento_categoria foreign key (id_categoria) 
        references categorias(id_categoria),
    constraint fk_movimiento_obligacion foreign key (id_obligacion) 
        references obligaciones(id_obligacion)
);

comment on table movimientos is 'Actúa como el libro mayor registrando cada flujo de dinero (ingreso, gasto o transferencia) realizado por los usuarios.';
comment on column movimientos.id_movimiento is 'Identificador único alfanumérico de la transacción. llave primaria (pk).';
comment on column movimientos.id_usuario is 'Llave foránea que identifica al usuario que realizó la transacción.';
comment on column movimientos.id_categoria is 'Llave foránea que clasifica la naturaleza de la transacción (ej. supermercado, nómina, pago de crédito).';
comment on column movimientos.id_obligacion is 'Llave foránea opcional que vincula la transacción al pago de una deuda o aporte a una meta de ahorro. es null si el movimiento es un gasto o ingreso corriente sin obligación asociada.';
comment on column movimientos.monto is 'Valor monetario de la transacción. el impacto (positivo o negativo) dependerá de la naturaleza de la categoría asociada.';
comment on column movimientos.descripcion_opcional is 'Nota de texto libre, referencia de pago o detalle adicional ingresado por el usuario o el sistema.';
comment on column movimientos.updated_at is 'Timestamp de auditoría de la última modificación del registro.';
comment on column movimientos.created_at is 'Timestamp de auditoría que registra el momento exacto en el que ocurrió la transacción.';