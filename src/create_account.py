import psycopg2
import bcrypt
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
import re
from datetime import date

disallowedchars="!#$%&/()='-|;"
background = '#ffe4e1'
foreground = '#79a1e0'


def UI_signup(clicked):
    username = userInput.get()
    email = mailInput.get()
    password = passInput.get()
    accountType = clicked.get()
    state = "activo"
    fecha = date.today()
    today_date = fecha.strftime("%Y-%m-%d")
    
    #Hashing del password
    pass_byte = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(pass_byte, bcrypt.gensalt(10))
    hashed = hashed.decode("utf-8")
    

    
    if(len(username) == 0 or len(email)== 0 or len(password) == 0 or set(username) & set(disallowedchars) or set(email) & set(disallowedchars) or set(password) & set(disallowedchars)):
        tk.messagebox.showinfo("Error de datos", "Datos ingresados invalidos")
    else:
        try:
            conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=12345")
            cur = conn.cursor()
            cur.execute("INSERT INTO usuario (nombre_usuario, contraseña, correo, estado) values (%s, %s, %s, %s)",
                    (username, hashed, email, state))
            
            cur.execute("INSERT INTO subscripcion (usuario, estado, tipo,fecha_inicio) values (%s, %s, %s, %s)",
                            (username, state, accountType, today_date))
            cur.execute(f"INSERT INTO registros(usuario_id) VALUES('{username}')")
        
            tk.messagebox.showinfo("Cuenta creada", "Cuenta Creada")
        
        except Exception:
            tk.messagebox.showinfo("Error", "El usuario ya se encuentra registrado, intente de nuevo")
        
        conn.commit() #Commit de las tablas a base de datos SQL
        conn.close()  #Cerrar la conexion


window = tk.Tk(className="Streameo (Working title)")


SignupFont = tkFont.Font(family="@MS UI Gothic", size=12, weight="bold" )


#Render del logo de la aplicacion
logoCanvas = tk.Canvas(window, width = 150, height = 150, highlightthickness=0, bg=background)
logo = tk.PhotoImage(file="streameologo.png")
logoCanvas.create_image(130,10, anchor="ne", image=logo)
logoCanvas.place(relx=0.49, rely=0.15, anchor="center")

#Area de inicio, con botones para ir a login, sign up y salir de la aplicacion
entryarea = tk.Canvas(window, width=350, height=300, bg=foreground)
entryarea.place(relx=0.5, rely=0.62, anchor="center")

#Area de input de informacion
userText = Label(entryarea, text = "Usuario", bg = foreground, font = SignupFont)
userText.place(relx=0.1, rely=0.1, anchor="w")
userInput = tk.Entry(entryarea, width=30)
userInput.place(relx=0.4, rely=0.1, anchor="w")

mailText = Label(entryarea, text = "Correo", bg = foreground, font = SignupFont)
mailText.place(relx=0.1, rely=0.3, anchor="w")
mailInput = tk.Entry(entryarea, width=30)
mailInput.place(relx=0.4, rely=0.3, anchor="w")

passText = Label(entryarea, text = "Contrasena", bg = foreground, font = SignupFont)
passText.place(relx=0.1, rely=0.5, anchor="w")
passInput = tk.Entry(entryarea, width=30)
passInput.place(relx=0.4, rely=0.5, anchor="w")

typeText = Label(entryarea, text = "Tipo de cuenta", bg = foreground, font = SignupFont)
typeText.place(relx=0.1, rely=0.7, anchor="w")
clicked = StringVar()
clicked.set("Basica")
typeMenu = OptionMenu(entryarea, clicked, "Basica", "Estandar", "Avanzada")
typeMenu.place(relx=0.45, rely=0.7, anchor="w")

buttonSignup = tk.Button(entryarea, bg=background, width=10, height=2, text="Crear cuenta", font=SignupFont, command=lambda: UI_signup(clicked))
buttonSignup.place(relx=0.1, rely=0.9, anchor="w")

buttonReturn = tk.Button(entryarea, bg=background, width=10, height=2, text="Volver", font=SignupFont, command=lambda: UI_signup(clicked))
buttonReturn.place(relx=0.9, rely=0.9, anchor="e")


#Configuraciones extra de ventana
window.configure(bg=background)
window.geometry("900x500")
window.resizable(False,False)
window.mainloop()
