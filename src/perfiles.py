
import psycopg2

from tkinter import *
import tkinter.font as tkFont

from busqueda_contenido import UI_busqueda

background = '#ffe4e1'
foreground = '#79a1e0'



usuario = ""
def setUsuario(inputUsuario):
    global usuario
    usuario = inputUsuario

window = Tk(className="Streameo (Working title)")
window.title("Register")
window.withdraw()

botonesFont = tkFont.Font(family="@MS UI Gothic", size=16, weight="bold" )
loginFont = tkFont.Font(family="@MS UI Gothic", size=8, weight="bold" )


def nuevo():
    for widgets in window.winfo_children():
      widgets.destroy()
    window.entry = Entry()
    window.entry.pack()
    window.e=Button(window, text="Aceptar", command=click, height = 3, width = 20, bg=background, font=botonesFont)
    window.e.pack()
    window.e=Button(window, text="Volver", command=perfiles, height = 3, width = 20, bg=background, font=botonesFont)
    window.e.pack()
    window.mainloop()



def click():
    name = window.entry.get()
    connection = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
    cursor = connection.cursor()
    cursor.execute('''SELECT COUNT(*) FROM perfil''')
    cantidad = cursor.fetchall()
    cantidad = cantidad[0][0]
    cursor.execute(f'''SELECT COUNT(*) FROM perfil WHERE usuario = '{usuario}';''')
    result1 = cursor.fetchall()
    perfiles = int(result1[0][0])
    cursor.execute(f'''SELECT * FROM perfil WHERE usuario = '{usuario}';''')
    result2 = cursor.fetchall()
    cursor.execute(f'''SELECT * FROM usuario INNER JOIN subscripcion ON usuario.nombre_usuario = subscripcion.usuario WHERE nombre_usuario = '{usuario}';''')
    result3 = cursor.fetchall()
    subscription = int(result3[0][7])
    for widgets in window.winfo_children():
      widgets.destroy()
    if subscription == 1 and perfiles < 1:
        l = Label(window, text = "Nuevo Perfil Añadido!")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
        cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{usuario}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
    elif subscription == 1 and perfiles >=1:
        l = Label(window, text = "Ya no puede crear perfiles. Debe de mejorar su cuenta.")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
    if subscription == 2 and perfiles < 4:
        l = Label(window, text = "Nuevo Perfil Añadido!")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
        print(name)
        cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{usuario}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
    elif subscription == 2 and perfiles >=4:
        l = Label(window, text = "Ya no puede crear perfiles. Debe de mejorar su cuenta.")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
    if subscription == 3 and perfiles < 8:
        l = Label(window, text = "Nuevo Perfil Añadido!")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
        cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{usuario}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
    elif subscription == 3 and perfiles >=8:
        l = Label(window, text = "Ha llegado a la mayor cantidad de perfiles disponibles.")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
    connection.commit()
    connection.close()
    
    window.e=Button(window, text="Volver", command=hola, height = 3, width = 20, bg=background, font=botonesFont)
    window.e.pack()
    window.mainloop()
    
def hola():
    for widgets in window.winfo_children():
      widgets.destroy()
    connection = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
    cursor = connection.cursor()
    cursor.execute('''SELECT COUNT(*) FROM perfil''')
    cantidad = cursor.fetchall()
    cantidad = cantidad[0][0]
    cursor.execute(f'''SELECT COUNT(*) FROM perfil WHERE usuario = '{usuario}';''')
    result1 = cursor.fetchall()
    perfiles = int(result1[0][0])
    cursor.execute(f'''SELECT * FROM perfil WHERE usuario = '{usuario}';''')
    result2 = cursor.fetchall()
    cursor.execute(f'''SELECT * FROM usuario INNER JOIN subscripcion ON usuario.nombre_usuario = subscripcion.usuario WHERE nombre_usuario = '{usuario}';''')
    result3 = cursor.fetchall()
    #print(result3[0][6])
    subscription = int(result3[0][7])
    window.geometry("300x350")
    l = Label(window, text = "Seleccione!")
    l.config(font =("Courier", 14))
    window.configure(bg=foreground)
    l.pack()
    e=Button(window, text="Crear Nuevo Perfil", command=nuevo, height = 3, width = 20, bg=background, font=botonesFont)
    e.pack()
    for x in range(perfiles):
        e=Button(window, text=result2[x][1], command= lambda x=x: select(x), height = 3, width = 20, bg=background, font=botonesFont)
        e.pack()
    window.mainloop()
    connection.commit()
    connection.close()
    
def select(X):
    connection = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
    cursor = connection.cursor()
    cursor.execute('''SELECT COUNT(*) FROM perfil''')
    cantidad = cursor.fetchall()
    cantidad = cantidad[0][0]
    cursor.execute(f'''SELECT COUNT(*) FROM perfil WHERE usuario = '{usuario}';''')
    result1 = cursor.fetchall()
    perfiles = int(result1[0][0])
    cursor.execute(f'''SELECT * FROM perfil WHERE usuario = '{usuario}';''')
    result2 = cursor.fetchall()
    cursor.execute(f'''SELECT * FROM usuario INNER JOIN subscripcion ON usuario.nombre_usuario = subscripcion.usuario WHERE nombre_usuario = '{usuario}';''')
    result3 = cursor.fetchall()
    print(result3[0][7])
    subscription = int(result3[0][7])
    print("lol")
    elegido = result2[X][1]
    print("El usario elegido fue " + elegido + "\n")
    cursor.execute(f'''SELECT * FROM favoritos WHERE perfil_id = '{result2[X][2]}';''')
    result4 = cursor.fetchall()
    print(f"Contenido Visto:\n {result4}")
    window.destroy()
    UI_busqueda(result2[X][2], result3[0][7])



def perfiles():
    window.deiconify()
    for widgets in window.winfo_children():
      widgets.destroy()
    connection = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
    cursor = connection.cursor()
    cursor.execute('''SELECT COUNT(*) FROM perfil''')
    cantidad = cursor.fetchall()
    cantidad = cantidad[0][0]
    cursor.execute(f'''SELECT COUNT(*) FROM perfil WHERE usuario = '{usuario}';''')
    result1 = cursor.fetchall()
    perfiles = int(result1[0][0])
    cursor.execute(f'''SELECT * FROM perfil WHERE usuario = '{usuario}';''')
    result2 = cursor.fetchall()
    cursor.execute(f'''SELECT * FROM usuario INNER JOIN subscripcion ON usuario.nombre_usuario = subscripcion.usuario WHERE nombre_usuario = '{usuario}';''')
    result3 = cursor.fetchall()
    #print(result3[0][6])
    print(result3)
    subscription = int(result3[0][7])
    window.geometry("300x700")
    l = Label(window, text = "Seleccione!")
    l.config(font =("Courier", 14))
    window.configure(bg=foreground)
    l.pack()
    e=Button(window, text="Crear Nuevo Perfil", command=nuevo, height = 2, width = 20, bg=background, font=botonesFont)
    e.pack()
    for x in range(perfiles):
        e=Button(window, text=result2[x][1], command= lambda x=x: select(x), height = 2, width = 20, bg=background, font=botonesFont)
        e.pack()
    window.mainloop()
    connection.commit()
    connection.close()


 








