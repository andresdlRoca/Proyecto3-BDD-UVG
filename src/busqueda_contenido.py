import psycopg2
import tkinter as tk
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
import tkinter.font as tkFont
import vlc
import pafy
import time
import keyboard
from favoritos import UI_favorito, registrar_favs
from registro_historial import *
from recommendation import recommendation_UI

conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
cur = conn.cursor()

def clear_entradas(event, entry):
    entry.delete(0, tk.END)

def busqueda_estreno(busqueda):
    cur.execute("""
    SELECT nombre,links, id
    FROM multimedia
    WHERE EXTRACT(YEAR FROM fecha_estreno) = %(busqueda)s;
    """, {
        'busqueda': busqueda
    })

    search_records = cur.fetchall()

    if search_records is None:
        print("No se ha encontrado ningun resultado")
        return False

    return search_records

def busquedaGeneral(busqueda):

    cur.execute(f"""
        SELECT	multimedia.nombre, multimedia.links, multimedia.id
        FROM	multimedia
        WHERE	multimedia.id IN(
            SELECT multimedia_id
            FROM actor_contenido
            WHERE actor_contenido.actor_id IN (
                SELECT id
                FROM actor
                WHERE nombre_completo ILIKE '%{busqueda}%'
            )
        )
        OR	multimedia.id IN(
            SELECT multimedia_id
            FROM director_contenido
            WHERE director_contenido.id IN (
                SELECT id
                FROM director
                WHERE nombre_completo ILIKE '%{busqueda}%'
            )
        )
        OR	multimedia.id IN(
            SELECT id_contenido
            FROM genero_contenido
            WHERE genero_contenido.id_genero IN (
                SELECT id_genero
                FROM generos
                WHERE nombre ILIKE '%{busqueda}%'
            )
        )
        OR	multimedia.tipo_contenido = '%{busqueda}%'
        OR	multimedia.id IN(
            SELECT multimedia_id
            FROM premios_contenido
            WHERE premios_contenido.id IN (
                SELECT id_premio
                FROM premios
                WHERE premio ILIKE '%{busqueda}%'
            )
        )
        OR	multimedia.nombre ILIKE '%{busqueda}%'

    """)

    search_records = cur.fetchall()

    if search_records is None:
        print("No se ha encontrado ningun resultado")
        return False

    print(search_records)
    return search_records
###Fin de Busqueda por Queries###


#Busqueda de contenido por medio de queries
def busqueda(scrollable_frame, busqueda, id_perfil, subscripcion):
    try:
        listaBusqueda = []

        if busqueda == "":
            labelresultados = tk.Label(scrollable_frame, text="No se ha encontrado ningun resultado :(", bg='#ffe4e1')
            labelresultados.grid(row=0, column=0, padx=200, pady=5)

        listaBusqueda = busquedaGeneral(busqueda)
        count=0
        if listaBusqueda:
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            for item in listaBusqueda:
                labelTitulo = tk.Label(scrollable_frame, text=item[0], bg='#ffe4e1')
                labelLink = tk.Button(scrollable_frame, text="Ver", bg='#ffe4e1', command=lambda x=item[1], y=item[2]:  visualizar(x, id_perfil, y, subscripcion))
                labelFav = tk.Button(scrollable_frame, text="Fav", bg='#ffe4e1', command=lambda y=item[2]:  registrar_favs(y, id_perfil))
                labelTitulo.grid(row=count, column=0, padx=20, pady=5)
                labelLink.grid(row=count, column=1, padx=20)
                labelFav.grid(row=count, column=2)
                count = count + 1

        else:
            listaBusqueda = busqueda_estreno(busqueda)
            if listaBusqueda:
                for widget in scrollable_frame.winfo_children():
                    widget.destroy()

                for item in listaBusqueda:
                    labelTitulo = tk.Label(scrollable_frame, text=item[0], bg='#ffe4e1')
                    labelLink = tk.Button(scrollable_frame, text="Ver", bg='#ffe4e1', command=lambda x=item[1], y=item[2]:  visualizar(x, id_perfil, y, subscripcion))
                    labelFav = tk.Button(scrollable_frame, text="Fav", bg='#ffe4e1', command=lambda y=item[2]:  registrar_favs(y, id_perfil))
                    labelTitulo.grid(row=count, column=0, padx=20, pady=5)
                    labelLink.grid(row=count, column=1, padx=20)
                    labelFav.grid(row=count, column=2)
                    count = count + 1
            else:
                labelresultados = tk.Label(scrollable_frame, text="No se ha encontrado ningun resultado :(", bg='#ffe4e1')
                labelresultados.grid(row=0, column=0, padx=200, pady=5)
    except:
        labelresultados = tk.Label(scrollable_frame, text="No se ha encontrado ningun resultado :(", bg='#ffe4e1')
        labelresultados.grid(row=0, column=0, padx=200, pady=5)
        conn.rollback()


#Visualizacion de contenido por medio de la libreria de VLC media player y pafy     
def visualizar(link, id_perfil, id_contenido, subscripcion):
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
    registrar_historial(id_contenido, id_perfil) 
    tiempo = 5
    while True:
        if playing and int(subscripcion) == 1:
            time.sleep(tiempo - time.time() % tiempo) #Se muestra un anuncio cada X tiempo (segundos)
            player.pause()
            messagebox.showinfo("Anuncio!", f"Id anuncio X\nAnuncio X\n")
            player.play()
            playing=True
        if keyboard.read_key() == "p":
            player.pause()
            playing=False
            print("Pause")
            time.sleep(0.1)
        elif keyboard.read_key() == "r":
            player.play()
            playing=True
            print("Play")
        elif keyboard.read_key() == "e":
            player.stop()
            return False

            
#Interfaz de usuario de busqueda de contenido y visualizacion
def UI_busqueda(id_perfil, subscripcion):
    background = '#ffe4e1'
    foreground = '#79a1e0'
    #pastWindow.destroy()

    searchWindow = tk.Tk(className="Streameo (Working Title)")
    entryarea = tk.Canvas(searchWindow, width=750, height=650, bg=foreground)
    entryarea.place(relx=0.5, rely=0.5, anchor="center")
    searchFont = tkFont.Font(family="@MS UI Gothic", size=8, weight="bold" )

    #Render del logo de la aplicacion
    logoCanvas = tk.Canvas(searchWindow, width = 150, height = 150, highlightthickness=0, bg=foreground)
    logo = tk.PhotoImage(master=searchWindow, file="src/assets/streameologo.png")
    logoCanvas.create_image(130,10, anchor="ne", image=logo)
    logoCanvas.place(relx=0.49, rely=0.15, anchor="center")
    containerBusqueda = tk.Frame(searchWindow)
    
    resultadosBusqueda = tk.Canvas(containerBusqueda, width=600, height=300, bg=background)
    resultadosBusqueda.grid_propagate(False)
    resultadosBusqueda.pack_propagate(False)
    scrollbar = tk.Scrollbar(containerBusqueda, orient="vertical", command=resultadosBusqueda.yview)
    scrollable_frame = tk.Frame(resultadosBusqueda)
    scrollable_frame.configure(bg=background)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: resultadosBusqueda.configure(
            scrollregion=resultadosBusqueda.bbox("all")
        )
    )
    resultadosBusqueda.create_window((0,0), window=scrollable_frame, anchor="nw")
    resultadosBusqueda.configure(yscrollcommand=scrollbar.set)

    containerBusqueda.place(relx=0.5, rely=0.7, anchor="center")
    resultadosBusqueda.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    inputBusqueda = tk.Entry(entryarea, width=90)
    inputBusqueda.configure(bg=background)
    inputBusqueda.insert(0, "Busqueda...")
    inputBusqueda.bind("<Button-1>", lambda event: clear_entradas(event, inputBusqueda))
    inputBusqueda.place(relx=0.5, rely=0.28, anchor="center")

    buscar = tk.Button(searchWindow, bg=background, width=8, height=3, text="Buscar", font=searchFont, command=lambda: busqueda(scrollable_frame, inputBusqueda.get(), id_perfil, subscripcion))
    buscar.place(relx = 0.6, rely=0.35, anchor="center")

    favoritos = tk.Button(searchWindow, bg=background, width=15, height=3, text="Favoritos", font=searchFont, command=lambda: UI_favorito(id_perfil))
    historial = tk.Button(searchWindow, bg=background, width=15, height=3, text="Historial", font=searchFont, command=lambda: UI_historial(id_perfil))
    recomendaciones = tk.Button(searchWindow, bg=background, width=15, height=3, text="Recomendaciones", font=searchFont, command = lambda: recommendation_UI(id_perfil))
    volver = tk.Button(searchWindow, bg=background, width=8, height=3, text="Cerrar", font=searchFont, command= lambda: searchWindow.destroy())
    favoritos.place(relx=0.3, rely=0.4)
    historial.place(relx=0.45, rely=0.4)
    recomendaciones.place(relx=0.6, rely=0.4)
    volver.place(relx=0.15, rely=0.05)

    #Configuraciones extra de ventana
    searchWindow.configure(bg=background)
    searchWindow.geometry("1000x700")
    searchWindow.resizable(False,False)
    searchWindow.mainloop()

#UI_busqueda("6", "2")
