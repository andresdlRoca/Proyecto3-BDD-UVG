import psycopg2
from datetime import date
import tkinter as tk
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
import tkinter.font as tkFont
import time

conn = psycopg2.connect("host=localhost dbname=proyecto2 user=postgres password=videogamesfan10")
cur = conn.cursor()



def buscar_bitacora():

    cur.execute("""
        SELECT 	*
        FROM	bitacora
        """)

    bitacora_records = cur.fetchall()

    if bitacora_records is None:
        print("No se ha encontrado ningun resultado")
        return False
    
    print(bitacora_records)
    return bitacora_records

def bitacora(scrollable_frame):
    print("Lol")

    try:
        listabitacora = []
        listabitacora = buscar_bitacora()

        count=0
        if listabitacora:
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            for item in listabitacora:
                labelFecha = tk.Label(scrollable_frame, text=item[0], bg='#ffe4e1')
                labelHora = tk.Label(scrollable_frame, text=item[1], bg='#ffe4e1')
                labelTabla = tk.Label(scrollable_frame, text=item[2], bg='#ffe4e1')
                labelID = tk.Label(scrollable_frame, text=item[3], bg='#ffe4e1')
                labelCambio = tk.Label(scrollable_frame, text=item[4], bg='#ffe4e1')
                labelUser = tk.Label(scrollable_frame, text=item[5], bg='#ffe4e1')            
                labelFecha.grid(row=count, column=0, padx=25, pady=5)
                labelHora.grid(row=count, column=1, padx=25)
                labelTabla.grid(row=count, column=2, padx=25)
                labelID.grid(row=count, column=3, padx=25, pady=5)
                labelCambio.grid(row=count, column=4, padx=25)
                labelUser.grid(row=count, column=5, padx=25)
                count = count + 1
        else:
            labelresultados = tk.Label(scrollable_frame, text="No se ha encontrado nada, ponte a ver algo!", bg='#ffe4e1')
            labelresultados.grid(row=0, column=0, padx=100, pady=5)
    except:
        
        print("No se encontro ningun resultado :(")

def UI_bitacora():
    background = '#ffe4e1'
    foreground = '#79a1e0'
    
    bitacoraWindow = tk.Tk(className="Streameo (Working Title)")
    bitacoraFont = tkFont.Font(family="@MS UI Gothic", size=7, weight="bold" )

    containerbitacora = tk.Frame(bitacoraWindow)
    resultadosbitacora = tk.Canvas(containerbitacora, width=700, height=500, bg=background)
    resultadosbitacora.grid_propagate(False)
    resultadosbitacora.pack_propagate(False)

    scrollbar = tk.Scrollbar(containerbitacora, orient="vertical", command= resultadosbitacora.yview)
    scrollable_frame = tk.Frame(resultadosbitacora)
    scrollable_frame.configure(bg=background)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: resultadosbitacora.configure(
            scrollregion=resultadosbitacora.bbox("all")
        )
    )

    resultadosbitacora.create_window((0,0), window=scrollable_frame, anchor="nw")
    resultadosbitacora.configure(yscrollcommand=scrollbar.set)

    containerbitacora.place(relx=0.5, rely=0.5, anchor="center")
    resultadosbitacora.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


    volver = tk.Button(bitacoraWindow, bg=background, width=5, height=1, text="Volver", font=bitacora, command= lambda: bitacoraWindow.destroy())
    refresh = tk.Button(bitacoraWindow, bg=background, width=5, height=1, text="Refresh", font=bitacora, command=bitacora(scrollable_frame))
    volver.place(relx= 0.05, rely=0.01)
    refresh.place(relx=0.2, rely=0.01)

    #Configuraciones extra de ventana
    bitacoraWindow.configure(bg=foreground)
    bitacoraWindow.geometry("900x600")
    bitacoraWindow.resizable(False,False)
    bitacoraWindow.mainloop()

UI_bitacora
