import psycopg2
from datetime import date, datetime
import tkinter as tk
from tkinter import *
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
import random

conn = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
cur = conn.cursor()

def simularRegistro(repeticiones, fecha):

    #Recopilacion de perfiles
    cur.execute("""
        SELECT id FROM perfil
    """)

    users_records = cur.fetchall()

    #Recopilacion de multimedia
    cur.execute("""
        SELECT id_contenido FROM multimedia
    """)

    multimedia_records = cur.fetchall()

    #Asignacion segun las repeticiones
    for i in range(int(repeticiones)):
        cur.execute("""
            INSERT INTO historial(
                id_contenido, fecha_visualizacion, capitulo, id_perfil
            ) 
            VALUES
            (%(id_contenido)s, %(fecha_visualizacion)s, NULL, %(id_perfil)s)
        """, {
            'id_contenido': random.choice(multimedia_records),
            'fecha_visualizacion': fecha,
            'id_perfil': random.choice(users_records)
        })
            
    tk.messagebox.showinfo("Aviso", "Se han simulado correctamente las visualizaciones")
    conn.commit()

