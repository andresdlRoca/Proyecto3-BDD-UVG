CREATE TABLE usuario (
	nombre_usuario VARCHAR(32) NOT NULL,
	contraseña VARCHAR(150) NOT NULL,
	correo	VARCHAR(50)	NOT NULL,
	estado	VARCHAR(12) NOT NULL,
	PRIMARY KEY (nombre_usuario)
);

CREATE TABLE seguridad (
	id_intento VARCHAR(32) NOT NULL,
	fecha DATE	NOT NULL,
	usuario VARCHAR(32) NOT NULL,
	FOREIGN KEY (usuario) REFERENCES usuario(nombre_usuario) ON DELETE CASCADE 
);

CREATE TABLE perfil (
	usuario VARCHAR(32) NOT NULL,
	nombre	VARCHAR(32) NOT NULL,
	id	VARCHAR(32) NOT NULL,
	fecha_nacimiento DATE NOT NULL,
	estado_vista VARCHAR(12) NOT NULL,
	estado_perfil VARCHAR(12) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (usuario) REFERENCES usuario(nombre_usuario) ON DELETE CASCADE
);

CREATE TABLE multimedia (
	id VARCHAR(32) NOT NULL,
	nombre VARCHAR(90) NOT NULL,
	fecha_estreno DATE NOT NULL,
	tipo_contenido VARCHAR(32) NOT NULL,
	links VARCHAR(240) NOT NULL,
	duracion INT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE historial (
	id_contenido VARCHAR(32) NOT NULL,
	fecha_visualizacion TIMESTAMP NOT NULL,
	capitulo int,
	id_perfil VARCHAR(32) NOT NULL,
	FOREIGN KEY(id_contenido) REFERENCES multimedia(id) ON DELETE CASCADE,
	FOREIGN KEY (id_perfil) REFERENCES perfil(id) ON DELETE CASCADE
);

CREATE TABLE premios (
	premio	VARCHAR(32) NOT NULL,
	categoria VARCHAR(90) NOT NULL,
	id_premio VARCHAR(32) NOT NULL,
	PRIMARY KEY (id_premio)
);

CREATE TABLE premios_contenido (
	multimedia_id VARCHAR(32) NOT NULL,
	id VARCHAR(32) NOT NULL,
	FOREIGN KEY (multimedia_id) REFERENCES multimedia(id) ON DELETE CASCADE,
	FOREIGN KEY (id) REFERENCES premios(id_premio) ON DELETE CASCADE
);

CREATE TABLE director (
	id	VARCHAR(32) NOT NULL,
	nombre_completo VARCHAR(90) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE director_contenido (
	multimedia_id VARCHAR(32) NOT NULL,
	id VARCHAR(32) NOT NULL,
	FOREIGN KEY (multimedia_id) REFERENCES multimedia(id) ON DELETE CASCADE,
	FOREIGN KEY (id) REFERENCES director(id) ON DELETE CASCADE
);

CREATE TABLE actor (
	id	VARCHAR(32) NOT NULL,
	nombre_completo VARCHAR(90) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE actor_contenido (
	multimedia_id VARCHAR(32) NOT NULL,
	actor_id VARCHAR(32) NOT NULL,
	FOREIGN KEY (multimedia_id) REFERENCES multimedia(id) ON DELETE CASCADE,
	FOREIGN KEY (actor_id) REFERENCES actor(id) ON DELETE CASCADE
);

CREATE TABLE subscripcion (
	usuario VARCHAR(32) NOT NULL,
	estado VARCHAR(20) NOT NULL,
	tipo VARCHAR(20) NOT NULL,
	fecha_inicio DATE NOT NULL
	FOREIGN KEY (usuario) REFERENCES usuario(nombre_usuario) ON DELETE CASCADE	
);

CREATE TABLE favoritos (
	perfil_id VARCHAR(32) NOT NULL,
	contenido_id VARCHAR(32) NOT NULL,
	estado VARCHAR(20) NOT NULL, 
	FOREIGN KEY (perfil_id) REFERENCES perfil(id) ON DELETE CASCADE,
	FOREIGN KEY (contenido_id) REFERENCES multimedia(id) ON DELETE CASCADE
);

CREATE TABLE generos (
	id_genero VARCHAR(8) NOT NULL,
	nombre VARCHAR(42) NOT NULL,
	PRIMARY KEY (id_genero)
);

CREATE TABLE genero_contenido (
	id_contenido VARCHAR(32) NOT NULL,
	id_genero VARCHAR(8) NOT NULL,
	FOREIGN KEY (id_contenido) REFERENCES multimedia(id) ON DELETE CASCADE,
	FOREIGN KEY (id_genero) REFERENCES generos(id_genero) ON DELETE CASCADE
);

CREATE TABLE recomendaciones (
	id VARCHAR(32) NOT NULL,
	nombre VARCHAR(90) NOT NULL,
	fecha_estreno DATE NOT NULL,
	tipo_contenido VARCHAR(32) NOT NULL,
	links VARCHAR(240) NOT NULL,
	FOREIGN KEY (id) REFERENCES multimedia(id) ON DELETE CASCADE
);

CREATE TABLE anuncios (
	id_anuncio VARCHAR(32) NOT NULL,
	nombre_anunciante VARCHAR(32) NOT NULL,
	links VARCHAR(240) NOT NULL,
	PRIMARY KEY (id_anuncio)
);

CREATE TABLE anuncio_contenido (
	id_anuncio VARCHAR(32) NOT NULL,
	id_contenido VARCHAR(32) NOT NULL,
	FOREIGN KEY (id_anuncio) REFERENCES anuncios(id_anuncio) ON DELETE CASCADE,
	FOREIGN KEY (id_contenido) REFERENCES multimedia(id) ON DELETE CASCADE
);
