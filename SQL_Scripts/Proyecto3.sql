create or replace  function bitacora_functionUIContenido() 
returns trigger as $bitacora$
declare
	c varchar;
	t varchar;
	id varchar;
	nom varchar;
begin
	--raise notice 'Aqui entro';
	c  := TG_ARGV[0];
    t  := TG_ARGV[1];
   	
	SELECT c.id_contenido 
	into id
    FROM multimedia c 
   	WHERE id_contenido  = new.id_contenido;
   
  	select nombre_usuario
  	into nom
	from usuario u inner join (
	   select r.usuario_id 
	   from registros r
		order by r.id desc
	   limit 1
	) r
	on r.usuario_id = u.nombre_usuario;
      
	insert into bitacora (fecha,hora,tabla,id_newcontent, cambio,nombre)
	values(current_date, current_time ,t,id,c,nom);


RETURN NULL;

END;
$bitacora$ LANGUAGE plpgsql;

create or replace function bitacora_functionDContenido() 
returns trigger as $bitacora$
declare
	c varchar;
	t varchar;
	id varchar;
	nom varchar;
begin
	--raise notice 'Aqui entro';
	c  := TG_ARGV[0];
    t  := TG_ARGV[1];
   	
	SELECT c.id_contenido 
	INTO id
    FROM multimedia c 
   	WHERE id_contenido  = old.id_contenido;
   
  	select nombre_usuario
  	into nom
	from usuario u inner join (
	   select r.usuario_id 
	   from registros r
		order by r.id desc
	   limit 1
	) r
	on r.usuario_id = u.nombre_usuario;
	
	insert into bitacora(fecha,hora,tabla,id_newcontent, cambio, nombre)
	values(current_date, current_time ,t,id,c,nom);

RETURN old;

END;
$bitacora$ LANGUAGE plpgsql;

create trigger bitacoraUpdateContenido 
after update
on public.multimedia 
for each row
execute procedure bitacora_functionUIContenido("update","contenido");

create trigger bitacoraInsertContenido 
after insert
on public.multimedia 
for each row
execute procedure bitacora_functionUIContenido("insert","contenido");

create trigger bitacoraDeleteContenido 
before delete
on public.multimedia 
for each row
execute procedure bitacora_functionDContenido("delete","contenido");

SELECT *
FROM MULTIMEDIA

INSERT INTO multimedia(id_contenido, nombre, fecha_estreno, tipo_contenido, links, duracion)
VALUES('mm37', 'The Avengers', '2022/4/27', 'Pelicula', 'https://www.youtube.com/watch?v=oBqqI6NMeaM', 143)


DROP TRIGGER bitacoraDeleteContenido 
ON multimedia

SELECT *
FROM bitacora

DELETE FROM multimedia
WHERE id_contenido = 'mm37'


DROP TRIGGER bitacoraUpdateContenido 
ON multimedia


UPDATE multimedia
SET tipo_contenido = 'Película'
WHERE id_contenido = 'mm02';

ALTER TABLE multimedia
RENAME COLUMN id TO id_contenido;

SELECT *
FROM multimedia
WHERE duracion = 143

DELETE FROM bitacora WHERE tabla='contenido';

SELECT *
FROM id

DROP TABLE id