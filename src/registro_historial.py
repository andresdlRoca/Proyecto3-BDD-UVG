import psycopg2
from datetime import date, datetime
import tkinter as tk
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
import tkinter.font as tkFont
import vlc
import pafy
import keyboard
import time

conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
cur = conn.cursor()

def registrar_historial(id_contenido, id_perfil):
    fecha_visualizacion = datetime.now()
    print(fecha_visualizacion)
    cur.execute("""
        INSERT INTO historial (
	        id_contenido, fecha_visualizacion, capitulo, id_perfil
        )
        VALUES 
            (%(id_contenido)s, %(fecha_visualizacion)s, NULL, %(id_perfil)s)

    """, {
        'id_contenido': id_contenido,
        'fecha_visualizacion':fecha_visualizacion,
        'id_perfil': id_perfil
    })

    conn.commit()

def buscar_historial(id_perfil):
    cur.execute("""
        SELECT 	multimedia.nombre, historial.fecha_visualizacion, multimedia.id, multimedia.links
        FROM	historial
        JOIN	multimedia ON historial.id_contenido = multimedia.id
        WHERE	id_perfil = %(id_perfil)s
        ORDER BY historial.fecha_visualizacion DESC
    """, {
        'id_perfil': id_perfil
    })

    history_records = cur.fetchall()

    if history_records is None:
        print("No se ha encontrado ningun resultado")
        return False
    
    print(history_records)
    return history_records

def historial(scrollable_frame, id_perfil):
    try:
        listaHistorial = []
        listaHistorial = buscar_historial(id_perfil)

        count=0
        if listaHistorial:
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            for item in listaHistorial:
                labelTitulo = tk.Label(scrollable_frame, text=item[0], bg='#ffe4e1')
                labelFecha = tk.Label(scrollable_frame, text=item[1], bg='#ffe4e1')
                labelVisualizar = tk.Button(scrollable_frame, text="Ver", bg='#ffe4e1', command=lambda x=item[3], y=item[2]: visualizar(x, id_perfil, y))

                labelTitulo.grid(row=count, column=0, padx=25, pady=5)
                labelFecha.grid(row=count, column=1, padx=15)
                labelVisualizar.grid(row=count, column=2, padx=25)
                count = count + 1
        else:
            labelresultados = tk.Label(scrollable_frame, text="No se ha encontrado nada, ponte a ver algo!", bg='#ffe4e1')
            labelresultados.grid(row=0, column=0, padx=100, pady=5)
    except:
        print("No se encontro ningun resultado :(")

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
    registrar_historial(id_contenido, id_perfil) 
    tiempo = 5
    time.sleep(1)
    while True:
        if playing:
            time.sleep(tiempo - time.time() % tiempo) #Se muestra un anuncio cada X tiempo (segundos)
            player.pause()
            messagebox.showinfo("Anuncio!", f"Id anuncio X\nAnuncio X\n")
            player.play()
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


def UI_historial(id_perfil):
    background = '#ffe4e1'
    foreground = '#79a1e0'
    
    historialWindow = tk.Tk(className="Streameo (Working Title)")
    historialFont = tkFont.Font(family="@MS UI Gothic", size=1, weight="bold" )

    containerHistorial = tk.Frame(historialWindow)
    resultadosHistorial = tk.Canvas(containerHistorial, width=400, height=500, bg=background)
    resultadosHistorial.grid_propagate(False)
    resultadosHistorial.pack_propagate(False)

    scrollbar = tk.Scrollbar(containerHistorial, orient="vertical", command= resultadosHistorial.yview)
    scrollable_frame = tk.Frame(resultadosHistorial)
    scrollable_frame.configure(bg=background)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: resultadosHistorial.configure(
            scrollregion=resultadosHistorial.bbox("all")
        )
    )

    resultadosHistorial.create_window((0,0), window=scrollable_frame, anchor="nw")
    resultadosHistorial.configure(yscrollcommand=scrollbar.set)

    containerHistorial.place(relx=0.5, rely=0.5, anchor="center")
    resultadosHistorial.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    historial(scrollable_frame, id_perfil)


    volver = tk.Button(master=historialWindow, bg=background, width=3, height=1, text="Volver", font=historialFont, command=lambda: historialWindow.destroy(), padx=10, pady=1)
    refresh = tk.Button(master=historialWindow, bg=background, width=3, height=1, text="Refresh", font=historialFont, command=lambda: historial(scrollable_frame, id_perfil), padx=15, pady=1)
    volver.grid(row=0, column=0, padx=10, pady=1)
    refresh.grid(row=0, column=1, padx=10, pady=1)

    #Configuraciones extra de ventana
    historialWindow.configure(bg=foreground)
    historialWindow.geometry("500x600")
    historialWindow.resizable(False,False)
    historialWindow.mainloop()

#UI_historial("6")