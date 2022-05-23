SELECT *
FROM actor;

SELECT *
FROM bitacora

INSERT INTO actor(id, nombre_completo)
VALUES('a17', 'Elizabeth Olsen')

create or replace  function bitacora_functionUIActor() 
returns trigger as $bitacora$
declare
	c varchar;
	t varchar;
	id_act varchar;
	nom varchar;
begin
	--raise notice 'Aqui entro';
	c  := TG_ARGV[0];
    t  := TG_ARGV[1];
   	
	SELECT c.id
	into id_act
    FROM actor c 
   	WHERE id  = new.id;
   
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
	values(current_date, current_time ,t,id_act,c,nom);


RETURN NULL;

END;
$bitacora$ LANGUAGE plpgsql;

create or replace function bitacora_functionDActor() 
returns trigger as $bitacora$
declare
	c varchar;
	t varchar;
	id_act varchar;
	nom varchar;
begin
	--raise notice 'Aqui entro';
	c  := TG_ARGV[0];
    t  := TG_ARGV[1];
   	
	SELECT c.id
	into id_act
    FROM actor c 
   	WHERE id  = new.id;
   
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
	values(current_date, current_time ,t,id_act,c,nom);

RETURN old;

END;
$bitacora$ LANGUAGE plpgsql;

DROP Trigger bitacoraDeleteActor
ON actor

create trigger bitacoraUpdateActor 
after update
on public.actor 
for each row
execute procedure bitacora_functionUIActor("update","actor");

create trigger bitacoraInsertActor 
after insert
on public.actor
for each row
execute procedure bitacora_functionUIActor("insert","actor");

create trigger bitacoraDeleteActor 
before delete
on public.actor
for each row
execute procedure bitacora_functionDActor("delete","actor");


SELECT *
FROM bitacora

SELECT *
FROM director

INSERT INTO director(id, nombre_completo)
VALUES('d17', 'Ryan Coogler')

UPDATE DIRECTOR
SET nombre_completo = 'Ryan Cogler'
WHERE id = 'd17'

create or replace  function bitacora_functionUIDirector() 
returns trigger as $bitacora$
declare
	c varchar;
	t varchar;
	id_act varchar;
	nom varchar;
begin
	--raise notice 'Aqui entro';
	c  := TG_ARGV[0];
    t  := TG_ARGV[1];
   	
	SELECT c.id
	into id_act
    FROM director c 
   	WHERE id  = new.id;
   
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
	values(current_date, current_time ,t,id_act,c,nom);


RETURN NULL;

END;
$bitacora$ LANGUAGE plpgsql;

create or replace function bitacora_functionDDirector() 
returns trigger as $bitacora$
declare
	c varchar;
	t varchar;
	id_act varchar;
	nom varchar;
begin
	--raise notice 'Aqui entro';
	c  := TG_ARGV[0];
    t  := TG_ARGV[1];
   	
	SELECT c.id
	into id_act
    FROM director c 
   	WHERE id  = new.id;
   
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
	values(current_date, current_time ,t,id_act,c,nom);

RETURN old;

END;
$bitacora$ LANGUAGE plpgsql;

create trigger bitacoraUpdateDirector 
after update
on public.director 
for each row
execute procedure bitacora_functionUIDirector("update","director");

create trigger bitacoraInsertDirector 
after insert
on public.director
for each row
execute procedure bitacora_functionUIDirector("insert","director");

create trigger bitacoraDeleteDirector 
before delete
on public.director
for each row
execute procedure bitacora_functionDDirector("delete","director");

SELECT *
FROM anuncios


create or replace  function bitacora_functionUIAnuncio() 
returns trigger as $bitacora$
declare
	c varchar;
	t varchar;
	id_act varchar;
	nom varchar;
begin
	--raise notice 'Aqui entro';
	c  := TG_ARGV[0];
    t  := TG_ARGV[1];
   	
	SELECT c.id_anuncio
	into id_act
    FROM anuncios c 
   	WHERE id_anuncio  = new.id_anuncio;
   
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
	values(current_date, current_time ,t,id_act,c,nom);


RETURN NULL;

END;
$bitacora$ LANGUAGE plpgsql;

create or replace function bitacora_functionDAnuncio() 
returns trigger as $bitacora$
declare
	c varchar;
	t varchar;
	id_act varchar;
	nom varchar;
begin
	--raise notice 'Aqui entro';
	c  := TG_ARGV[0];
    t  := TG_ARGV[1];
   	
	SELECT c.id_anuncio
	into id_act
    FROM anuncios c 
   	WHERE id_anuncio  = new.id_anuncio;
   
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
	values(current_date, current_time ,t,id_act,c,nom);

RETURN old;

END;
$bitacora$ LANGUAGE plpgsql;

create trigger bitacoraUpdateAnuncio
after update
on public.anuncios
for each row
execute procedure bitacora_functionUIDirector("update","anuncio");

create trigger bitacoraInsertAnuncio 
after insert
on public.anuncios
for each row
execute procedure bitacora_functionUIDirector("insert","anuncio");

create trigger bitacoraDeleteAnuncio 
before delete
on public.anuncios
for each row
execute procedure bitacora_functionDDirector("delete","anuncio");
