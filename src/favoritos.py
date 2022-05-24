import psycopg2
from datetime import date
import tkinter as tk
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
import tkinter.font as tkFont
import pafy
import vlc
import keyboard
import time

conn = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
cur = conn.cursor()

def registrar_favs(id_contenido, id_perfil):
    cur.execute("""
        INSERT INTO favoritos (
	        perfil_id, contenido_id, estado
        )
        VALUES 
            (%(perfil_id)s, %(contenido_id)s, %(estado)s)

    """, {
        'contenido_id': id_contenido,
        'perfil_id':id_perfil,
        'estado': "Visto"
    })

    conn.commit()

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

def buscar_favorito(id_perfil):
    cur.execute("""
        SELECT 	multimedia.nombre, multimedia.id_contenido, multimedia.links
        FROM	multimedia
        JOIN	favoritos ON  favoritos.contenido_id = multimedia.id_contenido
        WHERE	favoritos.perfil_id = %(id_perfil)s
    """, {
        'id_perfil': id_perfil
    })

    favorite_records = cur.fetchall()

    if favorite_records is None:
        print("No se ha encontrado ningun resultado")
        return False
    
    print(favorite_records)
    return favorite_records

def favorito(scrollable_frame, id_perfil):
    try:
        listafavorito = []
        listafavorito = buscar_favorito(id_perfil)

        count=0
        if listafavorito:
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            for item in listafavorito:
                print(":)")
                labelTitulo = tk.Label(scrollable_frame, text=item[0], bg='#ffe4e1')
                print(":D")
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

def UI_favorito(id_perfil):
    background = '#ffe4e1'
    foreground = '#79a1e0'
    
    favoritoWindow = tk.Tk(className="Streameo (Working Title)")
    favoritoFont = tkFont.Font(family="@MS UI Gothic", size=7, weight="bold" )

    containerfavorito = tk.Frame(favoritoWindow)
    resultadosfavorito = tk.Canvas(containerfavorito, width=400, height=500, bg=background)
    resultadosfavorito.grid_propagate(False)
    resultadosfavorito.pack_propagate(False)

    scrollbar = tk.Scrollbar(containerfavorito, orient="vertical", command= resultadosfavorito.yview)
    scrollable_frame = tk.Frame(resultadosfavorito)
    scrollable_frame.configure(bg=background)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: resultadosfavorito.configure(
            scrollregion=resultadosfavorito.bbox("all")
        )
    )

    resultadosfavorito.create_window((0,0), window=scrollable_frame, anchor="nw")
    resultadosfavorito.configure(yscrollcommand=scrollbar.set)

    containerfavorito.place(relx=0.5, rely=0.5, anchor="center")
    resultadosfavorito.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    favorito(scrollable_frame, id_perfil)


    volver = tk.Button(favoritoWindow, bg=background, width=5, height=1, text="Volver", font=favorito, command= lambda: favoritoWindow.destroy())
    refresh = tk.Button(favoritoWindow, bg=background, width=5, height=1, text="Refresh", font=favorito, command=favorito(scrollable_frame, id_perfil))
    volver.place(relx= 0.05, rely=0.01)
    refresh.place(relx=0.2, rely=0.01)

    #Configuraciones extra de ventana
    favoritoWindow.configure(bg=foreground)
    favoritoWindow.geometry("500x600")
    favoritoWindow.resizable(False,False)
    favoritoWindow.mainloop()



