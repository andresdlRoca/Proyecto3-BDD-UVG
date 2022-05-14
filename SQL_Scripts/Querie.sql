SELECT	 	actor_id, SUM(duracion)
FROM 		(
				SELECT *
				FROM MULTIMEDIA INNER JOIN ACTOR_CONTENIDO ON multimedia.id = actor_contenido.multimedia_id
				WHERE ACTOR_CONTENIDO.actor_id = 'MH1') PELICULAS 
				INNER JOIN FAVORITOS ON PELICULAS.id = favoritos.contenido_id
WHERE 		perfil_id = '1234'
GROUP BY	actor_Id


