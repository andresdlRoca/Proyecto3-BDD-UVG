from msvcrt import setmode
import psycopg2
import tkinter as tk
from tkinter import *
from tkcalendar import *
import tkinter.font as tkFont
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
from datetime import date, datetime


background = '#ffe4e1'
foreground = '#79a1e0'

def main_screen_more_reports():
    window = tk.Tk(className="Reportes")
    Font = tkFont.Font(family="@MS UI Gothic", size=12, weight="bold" )
    logoCanvas = tk.Canvas(window, width = 150, height = 150, highlightthickness=0, bg=background)
    window.configure(bg=background)
    window.geometry("500x600")
    window.resizable(False,False)
    
    
    button_top10_genre = tk.Button(window, bg=foreground, width=30, height=6, text="top5_per_hour", font=Font, command=lambda: top5_per_hour())
    button_top10_genre.place(relx=0.2, rely=0.2, anchor="w")
    
    button_reproduction_amount = tk.Button(window, bg=foreground, width=30, height=6, text="top10_searches", font=Font, command=lambda: top10_searches())
    button_reproduction_amount.place(relx=0.2, rely=0.5, anchor="w")
    
    button_top10_staff = tk.Button(window, bg=foreground, width=30, height=6, text="top5_staff", font=Font, command=lambda: top5_staff())
    button_top10_staff.place(relx=0.2, rely=0.8, anchor="w")
    
    window.mainloop()
    
def create_screenUI(tittle):
    window = tk.Tk(className= tittle)
    Font = tkFont.Font(family="@MS UI Gothic", size=20, weight="bold" )
    logoCanvas = tk.Canvas(window, width = 150, height = 150, highlightthickness=0, bg=background)
    window.configure(bg=background)
    window.resizable(False,False)

    return window, Font

def top5_per_hour():
    window, Font = create_screenUI("top5_per_hour")
    window.geometry("1600x800")
    
    inputMonth = Entry(window, width=2)
    inputMonth.place(relx=0.1, rely=0.05, anchor="n")
    textMonth = Label(window, text = "Ingrese el numero de mes: ", bg=background)
    textMonth.place(relx=0.05, rely=0.05, anchor='n')

    
    
    entryarea9 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea9.place(relx=0.25, rely=0.12, anchor="center")
    entryarea10 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea10.place(relx=0.45, rely=0.12, anchor="center")
    entryarea11 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea11.place(relx=0.65, rely=0.12, anchor="center")
    entryarea12 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea12.place(relx=0.85, rely=0.12, anchor="center")
    text9 = Label(entryarea9, text = "9:00", bg = foreground, width= 5, font = Font)
    text9.place(relx=0.4, rely=0.1, anchor="w")
    text10 = Label(entryarea10, text = "10:00", bg = foreground, width= 5, font = Font)
    text10.place(relx=0.4, rely=0.1, anchor="w")
    text11 = Label(entryarea11, text = "11:00", bg = foreground, width= 5, font = Font)
    text11.place(relx=0.4, rely=0.1, anchor="w")
    text12 = Label(entryarea12, text = "12:00", bg = foreground, width= 5, font = Font)
    text12.place(relx=0.4, rely=0.1, anchor="w")
    
    entryarea13 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea13.place(relx=0.25, rely=0.35, anchor="center")
    entryarea14 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea14.place(relx=0.45, rely=0.35, anchor="center")
    entryarea15 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea15.place(relx=0.65, rely=0.35, anchor="center")
    entryarea16 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea16.place(relx=0.85, rely=0.35, anchor="center")
    text13 = Label(entryarea13, text = "13:00", bg = foreground, width= 5, font = Font)
    text13.place(relx=0.4, rely=0.1, anchor="w")
    text14 = Label(entryarea14, text = "14:00", bg = foreground, width= 5, font = Font)
    text14.place(relx=0.4, rely=0.1, anchor="w")
    text15 = Label(entryarea15, text = "15:00", bg = foreground, width= 5, font = Font)
    text15.place(relx=0.4, rely=0.1, anchor="w")
    text16 = Label(entryarea16, text = "16:00", bg = foreground, width= 5, font = Font)
    text16.place(relx=0.4, rely=0.1, anchor="w")
    
    entryarea17 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea17.place(relx=0.25, rely=0.60, anchor="center")
    entryarea18 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea18.place(relx=0.45, rely=0.60, anchor="center")
    entryarea19 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea19.place(relx=0.65, rely=0.60, anchor="center")
    entryarea20 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea20.place(relx=0.85, rely=0.60, anchor="center")
    text17 = Label(entryarea17, text = "17:00", bg = foreground, width= 5, font = Font)
    text17.place(relx=0.4, rely=0.1, anchor="w")
    text18 = Label(entryarea18, text = "18:00", bg = foreground, width= 5, font = Font)
    text18.place(relx=0.4, rely=0.1, anchor="w")
    text19 = Label(entryarea19, text = "19:00", bg = foreground, width= 5, font = Font)
    text19.place(relx=0.4, rely=0.1, anchor="w")
    text20 = Label(entryarea20, text = "20:00", bg = foreground, width= 5, font = Font)
    text20.place(relx=0.4, rely=0.1, anchor="w")
    
    entryarea21 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea21.place(relx=0.25, rely=0.85, anchor="center")
    entryarea22 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea22.place(relx=0.45, rely=0.85, anchor="center")
    entryarea23 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea23.place(relx=0.65, rely=0.85, anchor="center")
    entryarea24 = tk.Canvas(window, width=300, height=170, bg=foreground)
    entryarea24.place(relx=0.85, rely=0.85, anchor="center")
    text21 = Label(entryarea21, text = "21:00", bg = foreground, width= 5, font = Font)
    text21.place(relx=0.4, rely=0.1, anchor="w")
    text22 = Label(entryarea22, text = "22:00", bg = foreground, width= 5, font = Font)
    text22.place(relx=0.4, rely=0.1, anchor="w")
    text23 = Label(entryarea23, text = "23:00", bg = foreground, width= 5, font = Font)
    text23.place(relx=0.4, rely=0.1, anchor="w")
    text24 = Label(entryarea24, text = "24:00", bg = foreground, width= 5, font = Font)
    text24.place(relx=0.4, rely=0.1, anchor="w")
    
    button_select = tk.Button(window, bg=foreground, width=10, height=1, text="Seleccionar", font=Font, command=lambda: top5_per_hour_report(inputMonth, entryarea9, entryarea10,entryarea11,entryarea12,entryarea13,entryarea14,entryarea15,entryarea16,entryarea17,entryarea18,entryarea19,entryarea20,entryarea21,entryarea22,entryarea23,entryarea24))
    button_select.place(relx=0.08, rely=0.1, anchor="n")
    
def top5_per_hour_report(inputMonth, entryarea9, entryarea10,entryarea11,entryarea12,entryarea13,entryarea14,entryarea15,entryarea16,entryarea17,entryarea18,entryarea19,entryarea20,entryarea21,entryarea22,entryarea23,entryarea24):
    monthNumber = inputMonth.get()
    try:
        checker = int(monthNumber)
        if(checker >= 1 and checker <=12):
            if checker == 1:
                monthStart = "2022-01-01"
                monthEnd = "2022-02-01"
            elif checker ==2:
                monthStart = "2022-02-01"
                monthEnd = "2022-03-01"
            elif checker ==3:
                monthStart = "2022-03-01"
                monthEnd = "2022-04-01"
            elif checker ==4:
                monthStart = "2022-04-01"
                monthEnd = "2022-05-01"
            elif checker ==5:
                monthStart = "2022-05-01"
                monthEnd = "2022-06-01"
            elif checker ==6:
                monthStart = "2022-06-01"
                monthEnd = "2022-07-01"
            elif checker ==7:
                monthStart = "2022-07-01"
                monthEnd = "2022-08-01"
            elif checker ==8:
                monthStart = "2022-08-01"
                monthEnd = "2022-09-01"
            elif checker ==9:
                monthStart = "2022-09-01"
                monthEnd = "2022-10-01"
            elif checker ==10:
                monthStart = "2022-10-01"
                monthEnd = "2022-11-01"
            elif checker ==11:
                monthStart = "2022-11-01"
                monthEnd = "2022-12-01"
            elif checker ==12:
                monthStart = "2022-12-01"
                monthEnd = "2023-01-01"
            print(monthStart)
            print(monthEnd)

            
            conn = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=12345")
            cur = conn.cursor()
            cur.execute("""
                SELECT  *
                FROM top_by_hour
                WHERE fecha_visualizacion >= %(monthStart)s
                AND fecha_visualizacion < %(monthEnd)s

                """, {
                    'monthStart': monthStart,
                    'monthEnd': monthEnd
                })
            
            report = cur.fetchall()
            print(report)
            tempList24 = []
            tempList23 = []
            tempList22 = []
            tempList21 = []
            tempList20 = []
            tempList19 = []
            tempList18 = []
            tempList17 = []
            tempList16 = []
            tempList15 = []
            tempList14 = []
            tempList13 = []
            tempList12 = []
            tempList11 = []
            tempList10 = []
            tempList9 = []
            infoList = {}
            
            for i in report:
                if(i[0] == 0.0):
                    if(len(tempList24) == 5):
                        break
                    else:
                        tempList24.append(i[2])
                        infoList[i[0]] = tempList24
                
                if(i[0] == 23.0):
                    if(len(tempList23) == 5):
                        break
                    else:
                        tempList23.append(i[2])
                        infoList[i[0]] = tempList23
                        
                if(i[0] == 22.0):
                    if(len(tempList22) == 5):
                        break
                    else:
                        tempList22.append(i[2])
                        infoList[i[0]] = tempList22
                        
                if(i[0] == 21.0):
                    if(len(tempList21) == 5):
                        break
                    else:
                        tempList21.append(i[2])
                        infoList[i[0]] = tempList21
                
                if(i[0] == 20.0):
                    if(len(tempList20) == 5):
                        break
                    else:
                        tempList20.append(i[2])
                        infoList[i[0]] = tempList20
                        
                if(i[0] == 19.0):
                    if(len(tempList19) == 5):
                        break
                    else:
                        tempList19.append(i[2])
                        infoList[i[0]] = tempList19
                        
                if(i[0] == 18.0):
                    if(len(tempList18) == 5):
                        break
                    else:
                        tempList18.append(i[2])
                        infoList[i[0]] = tempList18
                        
                if(i[0] == 17.0):
                    if(len(tempList17) == 5):
                        break
                    else:
                        tempList17.append(i[2])
                        infoList[i[0]] = tempList17
                        
                if(i[0] == 16.0):
                    if(len(tempList16) == 5):
                        break
                    else:
                        tempList16.append(i[2])
                        infoList[i[0]] = tempList16
                        
                if(i[0] == 15.0):
                    if(len(tempList15) == 5):
                        break
                    else:
                        tempList15.append(i[2])
                        infoList[i[0]] = tempList15
                        
                if(i[0] == 14.0):
                    if(len(tempList14) == 5):
                        break
                    else:
                        tempList14.append(i[2])
                        infoList[i[0]] = tempList14
                        
                if(i[0] == 13.0):
                    if(len(tempList13) == 5):
                        break
                    else:
                        tempList13.append(i[2])
                        infoList[i[0]] = tempList13
                        
                if(i[0] == 12.0):
                    if(len(tempList12) == 5):
                        break
                    else:
                        tempList12.append(i[2])
                        infoList[i[0]] = tempList12
                        
                if(i[0] == 11.0):
                    if(len(tempList11) == 5):
                        break
                    else:
                        tempList11.append(i[2])
                        infoList[i[0]] = tempList11
                        
                if(i[0] == 10.0):
                    if(len(tempList10) == 5):
                        break
                    else:
                        tempList10.append(i[2])
                        infoList[i[0]] = tempList10
                        
                if(i[0] == 9.0):
                    if(len(tempList9) == 5):
                        break
                    else:
                        tempList9.append(i[2])
                        infoList[i[0]] = tempList9
            
        else:
            tk.messagebox.showinfo("Error", "Ingrese en el rango de 1 a 12")

        print(infoList)   

        if 0.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[0.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea24, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea24, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 23.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[23.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea23, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea23, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 22.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[22.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea22, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea22, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 21.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[21.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea21, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea21, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
                
        if 20.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[20.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea20, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea20, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 19.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[19.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea19, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea19, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 18.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[18.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea18, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea18, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 17.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[17.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea19, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea19, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 16.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[16.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea16, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea16, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 15.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[15.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea15, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea15, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 14.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[14.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea14, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea14, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 13.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[13.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea13, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea13, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 12.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[12.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea12, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea12, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 11.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[11.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea11, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea11, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 10.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[10.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea10, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea10, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
                
        if 9.0 in infoList.keys():
            txt=""
            x = 1
            y = 0.25
            for i in infoList[9.0]:
                blank = "                                                  "
                txt = str(x) + '.'+ i
                empty = Label(entryarea9, text = blank, bg = foreground)
                empty.place(relx=0.1, rely=y, anchor="w")
                info = Label(entryarea9, text = txt, bg = foreground,font=("Arial", 10, "normal"))
                info.place(relx=0.1, rely=y, anchor="w")
                x = x+1
                y = y+0.1
        
                
    except Exception as e:
        tk.messagebox.showinfo("Error", "Ingrese un mes de forma de 1 a 12")
        print(e)
        
def top5_staff():
    window, Font = create_screenUI("top5_staff")
    window.geometry("900x500")
    
    initialCal = Calendar(window, setmode ='day', date_pattern = 'yyyy-mm-dd')
    initialCal.place(relx=0.3, rely=0.4, anchor="e")
    
    endCal = Calendar(window, setmode ='day', date_pattern = 'yyyy-mm-dd')
    endCal.place(relx=0.45, rely=0.4, anchor="center")


    button_select = tk.Button(window, bg=foreground, width=20, height=2, text="Generar Reporte", font=Font, command=lambda: top5_staff_report(initialCal, endCal,entryarea, Font))
    button_select.place(relx=0.2, rely=0.7, anchor="w")
    
    entryarea = tk.Canvas(window, width=300, height=400, bg=foreground)
    entryarea.place(relx=0.95, rely=0.5, anchor="e")
    
    
def top5_staff_report(initial, final, report_area, Font):
    initial_date = initial.get_date()
    final_date = final.get_date()
    
    conn = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=12345")
    cur = conn.cursor()
    cur.execute("""
        SELECT  nombre, COUNT(nombre)
        FROM modifications
        WHERE     fecha >  %(initial_date)s
        AND       fecha < %(final_date)s
        GROUP BY    nombre
        ORDER BY COUNT(nombre) DESC
        LIMIT 5
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
        txt = str(x) + '.'+ i[0] + ' con '+ str(i[1]) + ' cambios'
        empty = Label(report_area, text = blank, bg = foreground, font = Font)
        empty.place(relx=0.1, rely=y, anchor="w")
        info = Label(report_area, text = txt, bg = foreground,font=("Arial", 10, "normal"))
        info.place(relx=0.1, rely=y, anchor="w")
        x = x+1
        y = y+0.1
       
    conn.close()
    
def top10_searches():
    window, Font = create_screenUI("top5_staff")
    window.geometry("400x400")

    entryarea = tk.Canvas(window, width=300, height=300, bg=foreground)
    entryarea.place(relx=0.5, rely=0.5, anchor="center")
    
    conn = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=12345")
    cur = conn.cursor()
    cur.execute("""
        SELECT  busqueda, COUNT(busqueda)
        FROM searches
        GROUP BY    busqueda
        ORDER BY    COUNT(busqueda) DESC
        LIMIT 10
        """)
    
    report = cur.fetchall()
    txt=""
    x = 1
    y = 0.08
    for i in report:
        blank = "                                                  "
        txt = str(x) + '.'+ i[0] + ' con '+ str(i[1]) + ' busquedas'
        empty = Label(entryarea, text = blank, bg = foreground, font = Font)
        empty.place(relx=0.1, rely=y, anchor="w")
        info = Label(entryarea, text = txt, bg = foreground,font=("Arial", 10, "normal"))
        info.place(relx=0.1, rely=y, anchor="w")
        x = x+1
        y = y+0.1
    
#main_screen_more_reports()

