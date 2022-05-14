import psycopg2
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
from datetime import date
import pafy
import vlc
import keyboard
import time


background = '#ffe4e1'
foreground = '#79a1e0'

def recommendation_UI(perfil):
    window = tk.Tk(className="Recomendaciones")
    Font = tkFont.Font(family="@MS UI Gothic", size=12, weight="bold" )

    containerRec = tk.Frame(window)
    entryarea = tk.Canvas(containerRec, width=400, height=500, bg=background)
    entryarea.place(relx=0.5, rely=0.5, anchor="center")
    entryarea.grid_propagate(False)
    entryarea.pack_propagate(False)
    
    scrollbar = tk.Scrollbar(containerRec, orient="vertical", command= entryarea.yview)
    scrollable_frame = tk.Frame(entryarea)
    scrollable_frame.configure(bg=background)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: entryarea.configure(
            scrollregion=entryarea.bbox("all")
        )
    )

    entryarea.create_window((0,0), window=scrollable_frame, anchor="nw")
    entryarea.configure(yscrollcommand=scrollbar.set)


    containerRec.place(relx=0.5, rely=0.5, anchor="center")
    entryarea.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    recommendation(scrollable_frame, perfil)
    window.configure(bg=foreground)
    window.geometry("500x600")
    window.resizable(False,False)
    window.mainloop()
    
def visualizar(link, id_perfil, id_contenido):
    print(link)
    url=link
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    playing = True
    player.play()
    while True:
        if keyboard.read_key() == "p" and playing == True:
            player.pause()
            playing = False
        elif keyboard.read_key() == "p" and playing == False:
            player.play()
            playing == True
        elif keyboard.read_key() == "e":
            player.stop()
            return False

def buscar_reccommendation(id_perfil):
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
        SELECT  generos.id_genero, COUNT(generos.id_genero) 
        FROM    generos
        JOIN    genero_contenido ON genero_contenido.id_genero = generos.id_genero
        JOIN    multimedia ON multimedia.id = genero_contenido.id_contenido
        JOIN    historial ON historial.id_contenido = multimedia.id
        JOIN    perfil  ON  perfil.id = historial.id_perfil
        WHERE   %(id_perfil)s = historial.id_perfil
        AND     historial.id_contenido = multimedia.id
        GROUP BY    generos.id_genero
        ORDER BY    COUNT(generos.id_genero) DESC
        """, {
            'id_perfil': id_perfil
        })

    search_records = cur.fetchall()
    
    
    recommendation_records = []
    
    for i in search_records:
        cur.execute("""
            SELECT  multimedia.nombre, multimedia.id, multimedia.links
            FROM    multimedia
            JOIN    genero_contenido ON genero_contenido.id_contenido = multimedia.id
            WHERE   id_genero = %(genre)s
            LIMIT %(amount)s
        """, {
            'genre': i[0],
            'amount': i[1]
        })
        
        initial_recommendation_records = cur.fetchall()
        recommendation_records.extend(initial_recommendation_records)
        '''
        x = 0 
        for i in initial_recommendation_records:
            recommendation_records.append(i[x])
            x = x+1
        '''
        
         
    if recommendation_records is None:
        print("No se ha encontrado ningun resultado")
        return False
        
    print(recommendation_records)
    return recommendation_records
    

def recommendation(scrollable_frame, id_perfil):
    try:
        lista_recommendation = []
        lista_recommendation = buscar_reccommendation(id_perfil)

        count=0
        if lista_recommendation:
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            for item in lista_recommendation:
                labelTitulo = tk.Label(scrollable_frame, text=item[0], bg='#ffe4e1')
                labelFecha = tk.Label(scrollable_frame, text=item[1], bg='#ffe4e1')
                labelVisualizar = tk.Button(scrollable_frame, text="Ver", bg='#ffe4e1', command=lambda x=item[2], y=item[2]: visualizar(x, id_perfil, y))
                
                labelTitulo.grid(row=count, column=0, padx=25, pady=5)
                labelFecha.grid(row=count, column=1, padx=25)
                labelVisualizar.grid(row=count, column=2, padx=25)
                count = count + 1
        else:
            labelresultados = tk.Label(scrollable_frame, text="No se ha encontrado nada, ponte a ver algo!", bg='#ffe4e1')
            labelresultados.grid(row=0, column=0, padx=100, pady=5)
    except:
        
        print("No se encontro ningun resultado :(")
        
    


