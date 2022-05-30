import psycopg2
from datetime import date, datetime
import vlc
import pafy
import keyboard
import time

conn = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
cur = conn.cursor()

def registrar_historial(busqueda, id_perfil):
    fecha_busqueda = datetime.now()
    cur.execute("""
        INSERT INTO busquedas (
	        id_perfil, fecha_busqueda, busqueda
        )
        VALUES 
            (%(id_perfil)s, %(fecha_busqueda)s, %(busqueda)s)

    """, {
        'id_perfil': id_perfil,
        'fecha_busqueda': fecha_busqueda,
        'busqueda': busqueda
    })

    conn.commit()

registrar_historial("busquedaprueba", "21")