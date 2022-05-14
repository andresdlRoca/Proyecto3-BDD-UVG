import psycopg2
import tkinter as tk
from tkinter import *
from tkcalendar import *
import tkinter.font as tkFont
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
from datetime import date

background = '#ffe4e1'
foreground = '#79a1e0'

def main_screen():
    window = tk.Tk(className="Reportes")
    Font = tkFont.Font(family="@MS UI Gothic", size=12, weight="bold" )
    logoCanvas = tk.Canvas(window, width = 150, height = 150, highlightthickness=0, bg=background)
    window.configure(bg=background)
    window.geometry("900x500")
    window.resizable(False,False)
    
    
    button_top10_genre = tk.Button(window, bg=foreground, width=30, height=4, text="top10_genre", font=Font, command=lambda: top10_genre())
    button_top10_genre.place(relx=0.1, rely=0.2, anchor="w")
    
    button_reproduction_amount = tk.Button(window, bg=foreground, width=30, height=4, text="reproduction_amount", font=Font, command=lambda: reproduction_amount())
    button_reproduction_amount.place(relx=0.9, rely=0.2, anchor="e")
    
    button_top10_staff = tk.Button(window, bg=foreground, width=30, height=4, text="top10_staff", font=Font, command=lambda: top10_staff())
    button_top10_staff.place(relx=0.1, rely=0.5, anchor="w")
    
    button_premium_accounts = tk.Button(window, bg=foreground, width=30, height=4, text="premium_accounts", font=Font, command=lambda: premium_accounts())
    button_premium_accounts.place(relx=0.9, rely=0.5, anchor="e")
    
    button_peak_hour = tk.Button(window, bg=foreground, width=30, height=4, text="peak_hour", font=Font, command=lambda: peak_hour())
    button_peak_hour.place(relx=0.5, rely=0.8, anchor="center")
    
    window.mainloop()

def create_screenUI(tittle):
    window = tk.Tk(className= tittle)
    Font = tkFont.Font(family="@MS UI Gothic", size=12, weight="bold" )
    logoCanvas = tk.Canvas(window, width = 150, height = 150, highlightthickness=0, bg=background)
    window.configure(bg=background)
    window.geometry("900x500")
    window.resizable(False,False)

    return window, Font
  

def top10_genre():
    window, Font = create_screenUI("top10_genre")
    
    initialCal = Calendar(window, setmode ='day', date_pattern = 'yyyy-mm-dd')
    initialCal.place(relx=0.3, rely=0.4, anchor="e")
    
    endCal = Calendar(window, setmode ='day', date_pattern = 'yyyy-mm-dd')
    endCal.place(relx=0.45, rely=0.4, anchor="center")


    button_select = tk.Button(window, bg=foreground, width=20, height=2, text="Generar Reporte", font=Font, command=lambda: top10_genre_report(initialCal, endCal,entryarea, Font))
    button_select.place(relx=0.2, rely=0.7, anchor="w")
    
    entryarea = tk.Canvas(window, width=300, height=400, bg=foreground)
    entryarea.place(relx=0.95, rely=0.5, anchor="e")
    
    
def top10_genre_report(initial, final, report_area, Font):
    initial_date = initial.get_date()
    final_date = final.get_date()
    

    
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
        SELECT  generos.nombre, SUM(multimedia.duracion) 
        FROM    generos
        JOIN    genero_contenido ON genero_contenido.id_genero = generos.id_genero
        JOIN    multimedia ON multimedia.id = genero_contenido.id_contenido
        JOIN    historial ON historial.id_contenido = multimedia.id
        WHERE   historial.id_contenido = multimedia.id
        AND     historial.fecha_visualizacion >  %(initial_date)s
        AND     historial.fecha_visualizacion < %(final_date)s
        GROUP BY    generos.nombre
        ORDER BY    COUNT(generos.nombre) DESC
        """, {
            'initial_date': initial_date,
            'final_date': final_date
        })
    
    report = cur.fetchall()
    txt=""
    x = 1
    y = 0.2
    for i in report:
        blank = "                                                  "
        txt = str(x) + '.'+ i[0] + ' con '+ str(i[1]) + ' minutos'
        empty = Label(report_area, text = blank, bg = foreground, font = Font)
        empty.place(relx=0.1, rely=y, anchor="w")
        info = Label(report_area, text = txt, bg = foreground,font=("Arial", 10, "normal"))
        info.place(relx=0.1, rely=y, anchor="w")
        x = x+1
        y = y+0.1
       
    conn.close()

def reproduction_amount():
    window, Font = create_screenUI("reproduction_amount")
    
    initialCal = Calendar(window, setmode ='day', date_pattern = 'yyyy-mm-dd')
    initialCal.place(relx=0.3, rely=0.4, anchor="e")
    
    endCal = Calendar(window, setmode ='day', date_pattern = 'yyyy-mm-dd')
    endCal.place(relx=0.45, rely=0.4, anchor="center")


    button_select = tk.Button(window, bg=foreground, width=20, height=2, text="Generar Reporte", font=Font, command=lambda: reproduction_amount_report(initialCal, endCal,entryarea, Font))
    button_select.place(relx=0.2, rely=0.7, anchor="w")
    
    entryarea = tk.Canvas(window, width=300, height=400, bg=foreground)
    entryarea.place(relx=0.95, rely=0.5, anchor="e")
    
def reproduction_amount_report(initial, final, report_area, Font):
    initial_date = initial.get_date()
    final_date = final.get_date()
    
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
        SELECT  subscripcion.tipo, COUNT(historial.fecha_visualizacion)
        FROM    subscripcion
        JOIN    perfil ON perfil.usuario = subscripcion.usuario
        JOIN    historial ON historial.id_perfil = perfil.id
        WHERE   historial.fecha_visualizacion > %(initial_date)s
        AND     historial.fecha_visualizacion < %(final_date)s
        GROUP BY    subscripcion.tipo
        """, {
            'initial_date': initial_date,
            'final_date': final_date
        })
    
    report = cur.fetchall()
    txt=""
    x = 1
    y = 0.2
    for i in report:
        txt = 'Cuenta '+ i[0] + ' con '+ str(i[1]) + ' reproducciones'
        info = Label(report_area, text = txt, bg = foreground, font = ("Arial", 10, "normal"))
        info.place(relx=0.05, rely=y, anchor="w")
        x = x+1
        y = y+0.1
       
    conn.close()
    
    
def top10_staff():
    window, Font = create_screenUI("top10_staff")
    
    #Crear lado de cuentas normales
    normal_txt = Label(window, text = "Perfiles Estandar", bg = background, font = Font)
    normal_txt.place(relx=0.3, rely=0.05, anchor="center")
    normalArea = tk.Canvas(window, width=350, height=400, bg=foreground)
    normalArea.place(relx=0.1, rely=0.5, anchor="w")
    normalArea.create_line(0,200,360,200, fill= "white", width =1)
    normal_director_txt = Label(normalArea, text = "Actores", bg = foreground, font = Font)
    normal_director_txt.place(relx=0.5, rely=0.05, anchor="n")
    normal_actor_txt = Label(normalArea, text = "Directores", bg = foreground, font = Font)
    normal_actor_txt.place(relx=0.5, rely=0.55, anchor="center")
    
    #Creat lado de cuentas premium
    premium_text = Label(window, text = "Perfiles Avanzados", bg = background, font = Font)
    premium_text.place(relx=0.75, rely=0.05, anchor="center")
    premiumArea = tk.Canvas(window, width=350, height=400, bg=foreground)
    premiumArea.place(relx=0.95, rely=0.5, anchor="e")
    premiumArea.create_line(0,200,360,200, fill= "white", width =1)
    normal_director_txt = Label(premiumArea, text = "Actores", bg = foreground, font = Font)
    normal_director_txt.place(relx=0.5, rely=0.05, anchor="n")
    normal_actor_txt = Label(premiumArea, text = "Directores", bg = foreground, font = Font)
    normal_actor_txt.place(relx=0.5, rely=0.55, anchor="center")
    
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
    SELECT  actor.nombre_completo, COUNT(actor_contenido.actor_id)
    FROM    perfil
    JOIN    subscripcion ON subscripcion.usuario = perfil.usuario
    JOIN    historial ON historial.id_perfil = perfil.id
    JOIN    multimedia ON multimedia.id = historial.id_contenido
    JOIN    actor_contenido ON  actor_contenido.multimedia_id = multimedia.id
    JOIN    actor ON actor.id = actor_contenido.actor_id
    WHERE   subscripcion.tipo = '1'
    GROUP BY    actor.nombre_completo
    ORDER BY    COUNT(actor_contenido.actor_id) DESC
    LIMIT       10
    """)
    
    actors_basic = cur.fetchall()
    
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
    SELECT  director.nombre_completo, COUNT(director_contenido.id)
    FROM    perfil
    JOIN    subscripcion ON subscripcion.usuario = perfil.usuario
    JOIN    historial ON historial.id_perfil = perfil.id
    JOIN    multimedia ON multimedia.id = historial.id_contenido
    JOIN    director_contenido ON   director_contenido.multimedia_id = multimedia.id
    JOIN    director ON director.id = director_contenido.id
    WHERE   subscripcion.tipo = '1'
    GROUP BY    director.nombre_completo
    ORDER BY    COUNT(director_contenido.id) DESC
    LIMIT       10
    """)
    
    directors_basic = cur.fetchall()
    txt=""
    x = 1
    y = 0.15
    y2 = 0.15
    for i in actors_basic:
        if x > 5:
            txt = str(x) + '.'+ i[0]
            info = Label(normalArea, text = txt, bg = foreground,font=("Arial", 10, "normal"))
            info.place(relx=0.55, rely=y2, anchor="w")
            x = x+1
            y2 = y2+0.05
        else: 
            txt = str(x) + '.'+ i[0]
            info = Label(normalArea, text = txt, bg = foreground,font=("Arial", 10, "normal"))
            info.place(relx=0.05, rely=y, anchor="w")
            x = x+1
            y = y+0.05
    txt="" 
    x = 1
    y = 0.65
    y2 = 0.65
    for i in directors_basic:
        if x > 5:
            txt = str(x) + '.'+ i[0]
            info = Label(normalArea, text = txt, bg = foreground,font=("Arial", 10, "normal"))
            info.place(relx=0.55, rely=y2, anchor="w")
            x = x+1
            y2 = y2+0.05
        else: 
            txt = str(x) + '.'+ i[0]
            info = Label(normalArea, text = txt, bg = foreground,font=("Arial", 10, "normal"))
            info.place(relx=0.05, rely=y, anchor="w")
            x = x+1
            y = y+0.05
    
            
    
            
            
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
    SELECT  actor.nombre_completo, COUNT(actor_contenido.actor_id)
    FROM    perfil
    JOIN    subscripcion ON subscripcion.usuario = perfil.usuario
    JOIN    historial ON historial.id_perfil = perfil.id
    JOIN    multimedia ON multimedia.id = historial.id_contenido
    JOIN    actor_contenido ON  actor_contenido.multimedia_id = multimedia.id
    JOIN    actor ON actor.id = actor_contenido.actor_id
    WHERE   subscripcion.tipo = '2' OR subscripcion.tipo='3'
    GROUP BY    actor.nombre_completo
    ORDER BY    COUNT(actor_contenido.actor_id) DESC
    LIMIT       10
    """)
    
    actors_advanzed = cur.fetchall()
    
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
    SELECT  director.nombre_completo, COUNT(director_contenido.id)
    FROM    perfil
    JOIN    subscripcion ON subscripcion.usuario = perfil.usuario
    JOIN    historial ON historial.id_perfil = perfil.id
    JOIN    multimedia ON multimedia.id = historial.id_contenido
    JOIN    director_contenido ON   director_contenido.multimedia_id = multimedia.id
    JOIN    director ON director.id = director_contenido.id
    WHERE   subscripcion.tipo = '2' OR subscripcion.tipo='3'
    GROUP BY    director.nombre_completo
    ORDER BY    COUNT(director_contenido.id) DESC
    LIMIT       10
    """)
    
    directors_advanzed = cur.fetchall()
    txt=""
    x = 1
    y = 0.15
    y2 = 0.15
    for i in actors_advanzed:
        if x > 5:
            txt = str(x) + '.'+ i[0]
            info = Label(premiumArea, text = txt, bg = foreground,font=("Arial", 10, "normal"))
            info.place(relx=0.55, rely=y2, anchor="w")
            x = x+1
            y2 = y2+0.05
        else: 
            txt = str(x) + '.'+ i[0]
            info = Label(premiumArea, text = txt, bg = foreground,font=("Arial", 10, "normal"))
            info.place(relx=0.05, rely=y, anchor="w")
            x = x+1
            y = y+0.05
    txt=""
    x = 1
    y = 0.65
    y2 = 0.65
    for i in directors_advanzed:
        if x > 5:
            txt = str(x) + '.'+ i[0]
            info = Label(premiumArea, text = txt, bg = foreground,font=("Arial", 10, "normal"))
            info.place(relx=0.55, rely=y2, anchor="w")
            x = x+1
            y2 = y2+0.05
        else: 
            txt = str(x) + '.'+ i[0]
            info = Label(premiumArea, text = txt, bg = foreground,font=("Arial", 10, "normal"))
            info.place(relx=0.05, rely=y, anchor="w")
            x = x+1
            y = y+0.05

def premium_accounts():
    window, Font = create_screenUI("premium_accounts")
    number_font = tkFont.Font(family="@MS UI Gothic", size=30, weight="bold" )
    
    label_txt = Label(window, text = "Cantidad de cuentas premium en los ultimos 6 meses", bg = background, font = Font)
    label_txt.place(relx=0.5, rely=0.15, anchor="center")
    entryarea = tk.Canvas(window, width=600, height=300, bg=foreground)
    entryarea.place(relx=0.5, rely=0.5, anchor="center")
    
    
    fecha = date.today()
    today_year = int(fecha.strftime("%Y"))
    today_month = fecha.strftime("%m")
    today_day = fecha.strftime("%d")

    
    if (today_month == "01"):
        today_year = today_year - 1 
        today_year = str(today_year)
        whole_date = today_year + "-" + "07" + "-" + today_day

        
    elif (today_month =="02"):
        today_year = today_year - 1 
        today_year = str(today_year)
        whole_date = today_year + "-" + "08" + "-" + today_day
        
    elif (today_month =="03"):
        today_year = today_year - 1 
        today_year = str(today_year)
        whole_date = today_year + "-" + "09" + "-" + today_day
        
    elif (today_month =="04"):
        today_year = today_year - 1 
        today_year = str(today_year)
        whole_date = today_year + "-" + "10" + "-" + today_day
        
        
    elif (today_month =="05"):
        today_year = today_year - 1 
        today_year = str(today_year)
        whole_date = today_year + "-" + "11" + "-" + today_day
        
    elif (today_month =="06"):
        today_year = today_year - 1 
        today_year = str(today_year)
        whole_date = today_year + "-" + "12" + "-" + today_day
        
    elif (today_month =="07"):
        today_year = str(today_year)
        whole_date = today_year + "-" + "01" + "-" + today_day
        
    elif (today_month =="08"):
        today_year = str(today_year)
        whole_date = today_year + "-" + "02" + "-" + today_day
        
    elif (today_month =="09"):
        today_year = str(today_year)
        whole_date = today_year + "-" + "03" + "-" + today_day
        
    elif (today_month =="10"):
        today_year = str(today_year)
        whole_date = today_year + "-" + "04" + "-" + today_day
        
    elif (today_month =="11"):
        today_year = str(today_year)
        whole_date = today_year + "-" + "05" + "-" + today_day
        
    elif (today_month =="12"):
        today_year = str(today_year)
        whole_date = today_year + "-" + "06" + "-" + today_day
        
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
    SELECT  tipo, COUNT(tipo)
    FROM    subscripcion
    WHERE   fecha_inicio > %(whole_date)s
    GROUP BY    tipo
    ORDER BY    COUNT(tipo) DESC
    """, {
        'whole_date': whole_date
    })
    
        
    report = cur.fetchall()
    print(report)
    txt=""
    y = 0.2
    for i in report:
        if(i[1] > 1):
            txt = str(i[1]) + ' cuentas de tipo: ' + i[0]
        elif(i[1] == 1):
            txt = str(i[1]) + ' cuenta de tipo: ' + i[0]
        info = Label(entryarea, text = txt, bg = foreground, font = Font)
        info.place(relx=0.5, rely=y, anchor="center")
        y = y+0.15
    



def peak_hour():
    window, Font = create_screenUI("peak_hour")
    
    myCal = Calendar(window, setmode ='day', date_pattern = 'yyyy-mm-dd')
    myCal.place(relx=0.35, rely=0.4, anchor="e")
    
    button_select = tk.Button(window, bg=foreground, width=20, height=2, text="Generar Reporte", font=Font, command=lambda: peak_hour_report(myCal, entryarea, Font))
    button_select.place(relx=0.125, rely=0.7, anchor="w")
    
    entryarea = tk.Canvas(window, width=450, height=400, bg=foreground)
    entryarea.place(relx=0.95, rely=0.5, anchor="e")
    
def peak_hour_report(date, report_area, Font):
    given_date = date.get_date()
    date_list = given_date.split("-")
    
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
    SELECT  EXTRACT(HOUR FROM   fecha_visualizacion), COUNT(fecha_visualizacion)
    FROM    historial
    WHERE   EXTRACT(YEAR FROM fecha_visualizacion) = %(date_list[0])s
    AND     EXTRACT(MONTH FROM fecha_visualizacion) = %(date_list[1])s
    AND     EXTRACT(DAY FROM fecha_visualizacion) = %(date_list[2])s
    GROUP BY    EXTRACT(HOUR FROM   fecha_visualizacion)
    """, {
        'date_list[0]': date_list[0],
        'date_list[1]': date_list[1],
        'date_list[2]': date_list[2]
        
    })
    
        
    report = cur.fetchall()
    
    try:
        txt = """
        El servicio es mas utilizado a las
        """ + str(report[0][0]) + """ horas
        """
        
        info = Label(report_area, text = txt, bg = foreground, font = Font)
        info.place(relx=0.5, rely=0.2, anchor="center")
    except Exception:
        tk.messagebox.showinfo("Error", "En esa fecha no hay ningun registro de historial")
        

#main_screen()