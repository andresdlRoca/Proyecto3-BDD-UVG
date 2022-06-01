CREATE VIEW top_by_hour AS
SELECT	EXTRACT(HOUR FROM	fecha_visualizacion) AS hour_time, Count(historial.id_contenido) as amount, multimedia.nombre, fecha_visualizacion
FROM	historial
JOIN	multimedia ON multimedia.id_contenido = historial.id_contenido
WHERE	EXTRACT(HOUR FROM	fecha_visualizacion) > 9
AND 	EXTRACT(HOUR FROM	fecha_visualizacion) <= 24
OR		EXTRACT(HOUR FROM	fecha_visualizacion) = 0
GROUP BY	hour_time, multimedia.nombre, fecha_visualizacion
ORDER BY	hour_time DESC, amount DESC

CREATE VIEW	modifications AS
SELECT	nombre, fecha
FROM	bitacora

CREATE VIEW searches AS
SELECT	busqueda
FROM busquedas

-------------------------------------------------------------------------------------------------------------------------------------------------------------

CREATE INDEX bitacora_date ON bitacora(fecha)

CREATE INDEX view_date ON historial(fecha_visualizacion)

CREATE INDEX searches_index ON busquedas(busqueda)
