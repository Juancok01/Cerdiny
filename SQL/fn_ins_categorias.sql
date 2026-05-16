drop function if exists ins_categorias;

create function ins_categorias(
in iid_categoria int,
in inombre_categoria varchar,
in itipo_movimiento varchar,
in iid_categoria_padre int
)
returns categorias language plpgsql as $$ declare v_fila_insertada categorias; begin
--Funcion para insertar en la tabla categorias
	
insert into categorias 
(id_categoria, nombre_categoria, tipo_movimiento, id_categoria_padre) 
values
(iid_categoria, inombre_categoria, itipo_movimiento, iid_categoria_padre)

returning * into v_fila_insertada; return v_fila_insertada; end;$$;

--Ejemplo de consumo
/*
select * from ins_categorias(
1,
'Arriendo',
'Salida',
null
);
*/