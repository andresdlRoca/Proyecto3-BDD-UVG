from login import *
from perfiles import *
from admin import *
import tkinter as tk
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
import tkinter.font as tkFont


background = '#ffe4e1'
foreground = '#79a1e0'
disallowedchars="!#$%&/()='-|;"

def UI_signup(botonlogin, botonsignup, botonsalir, entryarea, ):
    botonlogin.place_forget()
    botonsignup.place_forget()
    botonsalir.place_forget()
    SignupFont = tkFont.Font(family="@MS UI Gothic", size=12, weight="bold" )
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
    
    buttonSignup = tk.Button(entryarea, bg=background, width=10, height=2, text="Crear cuenta", font=SignupFont, command=lambda: signup(userInput.get(), passInput.get(), mailInput.get(), clicked.get()))
    buttonSignup.place(relx=0.1, rely=0.9, anchor="w")

    buttonReturn = tk.Button(entryarea, bg=background, width=10, height=2, text="Volver", font=SignupFont, command=lambda: renderStartFromSignup(entryarea, botonlogin, botonsignup, botonsalir))
    buttonReturn.place(relx=0.9, rely=0.9, anchor="e")



def signup(username, password, email, accountType):
    #Hashing del password
    state="Activo"
    pass_byte = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(pass_byte, bcrypt.gensalt(10))
    hashed = hashed.decode("utf-8")
    fecha = date.today()
    today_date = fecha.strftime("%Y-%m-%d")

    if accountType=="Basica":
        accountType="1"
    elif accountType=="Estandar":
        accountType="2"
    elif accountType=="Avanzada":
        accountType="3"
    
    
    if(len(username) == 0 or len(email)== 0 or len(password) == 0 or set(username) & set(disallowedchars) or set(email) & set(disallowedchars) or set(password) & set(disallowedchars)):
        tk.messagebox.showinfo("Error de datos", "Datos ingresados invalidos")
    else:
        try:
            conn = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
            cur = conn.cursor()
            cur.execute("INSERT INTO usuario (nombre_usuario, contraseña, correo, estado, isadmin) values (%s, %s, %s, %s, %s)",
                    (username, hashed, email, state, False))
            
            cur.execute("INSERT INTO subscripcion (usuario, estado, tipo,fecha_inicio) values (%s, %s, %s, %s)",
                            (username, state, accountType, today_date))

            conn.commit()
            tk.messagebox.showinfo("Cuenta creada", "Cuenta Creada")
        
        except Exception as E:
            tk.messagebox.showinfo("Error", "El usuario ya se encuentra registrado, intente de nuevo")
            print(E)
        
        conn.commit() #Commit de las tablas a base de datos SQL
        conn.close()  #Cerrar la conexion

def renderLogin(botonlogin, botonsignup, botonsalir, inputUsuario, inputContra, volverMenu, loguearse, entryarea, ):
    botonlogin.place_forget()
    botonsignup.place_forget()
    botonsalir.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "Usuario")
    inputUsuario.place(relx=0.5, rely=0.2, anchor="center")
    inputContra.delete(0, tk.END)
    inputContra.insert(0, "Contraseña")
    inputContra.place(relx=0.5, rely=0.4, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    loguearse.place(relx=0.92, rely=0.7, anchor="e")

    entryarea.configure(width=200, height=150)

def renderStart(inputUsuario, inputContra, volverMenu, loguearse, botonlogin, botonsignup, botonsalir, entryarea):
    inputUsuario.place_forget()
    inputContra.place_forget()
    volverMenu.place_forget()
    loguearse.place_forget()
    botonlogin.place(relx=0.5, rely=0.2, anchor="center")
    botonsignup.place(relx=0.5, rely=0.5, anchor="center")
    botonsalir.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=350, height=250)

def renderStartFromSignup(entryarea, botonlogin, botonsignup, botonsalir):
    for widget in entryarea.winfo_children():
        widget.place_forget()
    
    botonlogin.place(relx=0.5, rely=0.2, anchor="center")
    botonsignup.place(relx=0.5, rely=0.5, anchor="center")
    botonsalir.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=350, height=250)


def clear_entradas(inputContra, entry):
    entry.delete(0, tk.END)
    if entry == inputContra:
        entry.configure(show="*")

def logueandose(usuario, contraseña, window):
    nombreuser = usuario.get()
    contra = contraseña.get()
    if loginInfo(nombreuser, contra):
        #cur.execute(f'''SELECT * FROM usuario INNER JOIN subscripcion ON usuario.nombre_usuario = subscripcion.usuario WHERE nombre_usuario = '{nombreuser}';''')
        #result = cur.fetchall()
        #print(result)
        if checkAdmin(nombreuser):
            mensajelogin = f"Bienvenido admin {nombreuser}"
            tk.messagebox.showinfo("Login", mensajelogin)
            window.destroy()
            inicializacionAdmin()
        else:
            mensajelogin= f"Bienvenido {nombreuser}!"
            tk.messagebox.showinfo("Login", mensajelogin)
            window.destroy()
            setUsuario(nombreuser)
            perfiles()
        

    else:
        tk.messagebox.showwarning("Login", "No te has logrado loguear")

def RenderAdmin(window):
    window.destroy()
    inicializacionAdmin()

def mainScreen():
    window = tk.Tk(className="Streameo (Working title)")

    botonesFont = tkFont.Font(family="@MS UI Gothic", size=16, weight="bold" )
    loginFont = tkFont.Font(family="@MS UI Gothic", size=8, weight="bold" )

    #Render del logo de la aplicacion
    logoCanvas = tk.Canvas(window, width = 150, height = 150, highlightthickness=0, bg=background)
    logo = tk.PhotoImage(master=window, file="src/assets/streameologo.png")
    logoCanvas.create_image(130,10, anchor="ne", image=logo)
    logoCanvas.place(relx=0.49, rely=0.15, anchor="center")

    #Area de inicio, con botones para ir a login, sign up y salir de la aplicacion
    entryarea = tk.Canvas(window, width=350, height=250, bg=foreground)
    entryarea.place(relx=0.5, rely=0.62, anchor="center")

    botonlogin = tk.Button(master=entryarea, bg=background, width=20, height=1, text="Login", font=botonesFont, command=lambda: renderLogin(botonlogin, botonsignup, botonsalir, inputUsuario, inputContra, volverMenu, loguearse, entryarea))
    botonlogin.place(relx=0.5, rely=0.2, anchor="center")

    botonsignup = tk.Button(master=entryarea, bg=background, width=20, height=1, text="Sign Up", font=botonesFont, command=lambda: UI_signup(botonlogin, botonsignup, botonsalir, entryarea))
    botonsignup.place(relx=0.5, rely=0.5, anchor="center")

    botonsalir = tk.Button(entryarea, bg=background, width=20, height=1, text="Salir", font=botonesFont, command=window.destroy)
    botonsalir.place(relx=0.5, rely=0.8, anchor="center")


    #Area de login
    inputUsuario = tk.Entry(entryarea, width=30)
    inputUsuario.bind("<Button-1>", lambda event: clear_entradas(event, inputUsuario))
    inputContra = tk.Entry(entryarea, width=30)
    inputContra.bind("<Button-1>", lambda event: clear_entradas(event, inputContra))
    volverMenu = tk.Button(entryarea, bg=background, width=3, height=1, text="Volver", font=loginFont, command=lambda: renderStart(inputUsuario, inputContra, volverMenu, loguearse, botonlogin, botonsignup, botonsalir, entryarea, ), padx=8, pady=1)
    loguearse = tk.Button(entryarea, bg=background, width=3, height=1, text="Login", font=loginFont, command=lambda: logueandose(inputUsuario, inputContra, window), padx=5, pady=1)

    #Configuraciones extra de ventana
    window.configure(bg=background)
    window.geometry("900x500")
    window.resizable(False,False)
    window.mainloop()

mainScreen()
