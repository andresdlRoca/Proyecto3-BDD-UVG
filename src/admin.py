import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from tkcalendar import *
from reportes import main_screen
from bitacora import *
import psycopg2
conn = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
cur = conn.cursor()

background = '#ffe4e1'
foreground = '#79a1e0'

def renderContenido():
    botonlogin.place_forget()
    botonsignup.place_forget()
    botonsalir.place_forget()
    botonbitacora.place_forget()
    botonagregarC.place(relx=0.5, rely=0.2, anchor="center")
    botonmodificarC.place(relx=0.5, rely=0.4, anchor="center")
    botoneliminarC.place(relx=0.5, rely=0.6, anchor="center")
    botonrelacionarC.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=350, height=300)

def renderMultimedia():
    botonagregarC.place_forget()
    botonmodificarC.place_forget()
    botoneliminarC.place_forget()
    botonrelacionarC.place_forget()
    botonMultimedia.place(relx=0.5, rely=0.2, anchor="center")
    botonGenero.place(relx=0.5, rely=0.35, anchor="center")
    botonActor.place(relx=0.5, rely=0.5, anchor="center")
    botonDirector.place(relx=0.5, rely=0.65, anchor="center")
    botonPremio.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=350, height=300)

def renderMultimedia2():
    botonagregarC.place_forget()
    botonmodificarC.place_forget()
    botoneliminarC.place_forget()
    botonrelacionarC.place_forget()
    botonMultimediaM.place(relx=0.5, rely=0.2, anchor="center")
    botonGeneroM.place(relx=0.5, rely=0.35, anchor="center")
    botonActorM.place(relx=0.5, rely=0.5, anchor="center")
    botonDirectorM.place(relx=0.5, rely=0.65, anchor="center")
    botonPremioM.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=350, height=300)

def renderMultimedia1A():
    botonMultimedia.place_forget()
    botonGenero.place_forget()
    botonDirector.place_forget()
    botonPremio.place_forget()
    botonActor.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputtitulo.delete(0, tk.END)
    inputtitulo.insert(0, "Titulo")
    inputtitulo.place(relx=0.5, rely=0.2, anchor="center")
    inputlink.delete(0, tk.END)
    inputlink.insert(0, "Links")
    inputlink.place(relx=0.5, rely=0.3, anchor="center")
    inputtipo.delete(0, tk.END)
    inputtipo.insert(0, "Tipo")
    inputtipo.place(relx=0.5, rely=0.4, anchor="center")
    inputduracion.delete(0, tk.END)
    inputduracion.insert(0, "Duracion")
    inputduracion.place(relx=0.5, rely=0.5, anchor="center")
    cal.place(relx=0.5, rely=0.6, anchor = "center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    agregarC.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)


def renderUsuarios():
    botonlogin.place_forget()
    botonsignup.place_forget()
    botonsalir.place_forget()
    botonbitacora.place_forget()
    botonadministrar.place(relx=0.5, rely=0.2, anchor="center")
    botonmodificarU.place(relx=0.5, rely=0.5, anchor="center")
    botoneliminarU.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=350, height=300)

def renderAnuncios():
    botonlogin.place_forget()
    botonsignup.place_forget()
    botonsalir.place_forget()
    botonbitacora.place_forget()
    botonagregarA.place(relx=0.5, rely=0.2, anchor="center")
    botonmodificarA.place(relx=0.5, rely=0.4, anchor="center")
    botonrelacionarA.place(relx=0.5, rely=0.6, anchor="center")
    botoneliminarA.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=350, height=300)

def renderStart():
    for widget in entryarea.winfo_children():
        widget.place_forget()
    botonlogin.place(relx=0.5, rely=0.2, anchor="center")
    botonsignup.place(relx=0.5, rely=0.4, anchor="center")
    botonsalir.place(relx=0.5, rely=0.6, anchor="center")
    botonbitacora.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=350, height=300)

def clear_entradas(event, entry):
    entry.delete(0, tk.END)


def logueandose(usuario, contraseña):
    nombreuser = usuario.get()
    cur.execute(f"SELECT * FROM multimedia WHERE id_contenido = '{nombreuser}'")
    x = cur.fetchall()
    print(x)
    mensajelogin= f"Bienvenido {nombreuser}!"
    tk.messagebox.showinfo("Login", mensajelogin)
    

def renderAgregarC():
    botonagregarC.place_forget()
    botonmodificarC.place_forget()
    botoneliminarC.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputtitulo.delete(0, tk.END)
    inputtitulo.insert(0, "Titulo")
    inputtitulo.place(relx=0.5, rely=0.2, anchor="center")
    inputgenero.delete(0, tk.END)
    inputgenero.insert(0, "Genero")
    inputgenero.place(relx=0.5, rely=0.3, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    loguearse.place(relx=0.92, rely=0.7, anchor="e")

    entryarea.configure(width=300, height=300)

def AgregarC(id_con,titulo, links, tipo, duracion, fecha):
    cur.execute(f"INSERT INTO multimedia(id_contenido, nombre, fecha_estreno, tipo_contenido, links, duracion) VALUES('{id_con}', '{titulo}', '{fecha}', '{tipo}', '{links}', {duracion})")
    conn.commit()


def renderActor():
    botonMultimedia.place_forget()
    botonGenero.place_forget()
    botonDirector.place_forget()
    botonPremio.place_forget()
    botonActor.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "Nombre")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    agregarCA.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)

def AgregarCA(id_con,nombre):
    cur.execute(f"INSERT INTO actor(id, nombre_completo) VALUES('{id_con}', '{nombre}')")
    conn.commit()

def renderDirector():
    botonMultimedia.place_forget()
    botonGenero.place_forget()
    botonDirector.place_forget()
    botonPremio.place_forget()
    botonActor.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "Nombre")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    agregarCD.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)
    
def AgregarCD(id_con,nombre):
    cur.execute(f"INSERT INTO director(id, nombre_completo) VALUES('{id_con}', '{nombre}')")
    conn.commit()

def renderGenero():
    botonMultimedia.place_forget()
    botonGenero.place_forget()
    botonDirector.place_forget()
    botonPremio.place_forget()
    botonActor.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "Nombre")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    agregarCG.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)

def AgregarCG(id_con,nombre):
    cur.execute(f"INSERT INTO generos(id_genero, nombre) VALUES('{id_con}', '{nombre}')")
    conn.commit()

def renderPremios():
    botonMultimedia.place_forget()
    botonGenero.place_forget()
    botonDirector.place_forget()
    botonPremio.place_forget()
    botonActor.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "Nombre")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    inputtitulo.delete(0, tk.END)
    inputtitulo.insert(0, "Categoria")
    inputtitulo.place(relx=0.5, rely=0.3, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    agregarCP.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)

def AgregarCP(id_con,premio, categoria):
    cur.execute(f"INSERT INTO premios(premio, categoria, id_premio) VALUES('{premio}', '{categoria}', '{id_con}')")
    conn.commit()

#g
def renderMultimedia1C():
    botonMultimediaM.place_forget()
    botonGeneroM.place_forget()
    botonDirectorM.place_forget()
    botonPremioM.place_forget()
    botonActorM.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputtitulo.delete(0, tk.END)
    inputtitulo.insert(0, "Titulo")
    inputtitulo.place(relx=0.5, rely=0.2, anchor="center")
    inputlink.delete(0, tk.END)
    inputlink.insert(0, "Links")
    inputlink.place(relx=0.5, rely=0.3, anchor="center")
    inputtipo.delete(0, tk.END)
    inputtipo.insert(0, "Tipo")
    inputtipo.place(relx=0.5, rely=0.4, anchor="center")
    inputduracion.delete(0, tk.END)
    inputduracion.insert(0, "Duracion")
    inputduracion.place(relx=0.5, rely=0.5, anchor="center")
    cal.place(relx=0.5, rely=0.6, anchor = "center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    modificarC.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)

def ModificarC(id_con,titulo, links, tipo, duracion, fecha):
    cur.execute(f"UPDATE multimedia SET nombre = '{titulo}', fecha_estreno = '{fecha}', tipo_contenido = '{tipo}', links ='{links}', duracion = {duracion}  WHERE id = '{id_con}';")
    conn.commit()


def renderActorM():
    botonMultimediaM.place_forget()
    botonGeneroM.place_forget()
    botonDirectorM.place_forget()
    botonPremioM.place_forget()
    botonActorM.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "Nombre")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    modificarCA.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)

def ModificarCA(id_con,nombre):
    cur.excute(f"UPDATE actor SET nombre_completo = '{nombre}' WHERE id = '{id_con}'")
    conn.commit()

def renderDirectorM():
    botonMultimediaM.place_forget()
    botonGeneroM.place_forget()
    botonDirectorM.place_forget()
    botonPremioM.place_forget()
    botonActorM.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "Nombre")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    modificarCD.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)
    
def ModificarCD(id_con,nombre):
    cur.excute(f"UPDATE director SET nombre_completo = '{nombre}' WHERE id = '{id_con}'")
    conn.commit()

def renderGeneroM():
    botonMultimediaM.place_forget()
    botonGeneroM.place_forget()
    botonDirectorM.place_forget()
    botonPremioM.place_forget()
    botonActorM.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "Nombre")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    modificarCG.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)

def ModificarCG(id_con,nombre):
    cur.excute(f"UPDATE generos SET nombre = '{nombre}' WHERE id_genero = '{id_con}'")
    conn.commit()

def renderPremiosM():
    botonMultimediaM.place_forget()
    botonGeneroM.place_forget()
    botonDirectorM.place_forget()
    botonPremioM.place_forget()
    botonActorM.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "Nombre")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    inputtitulo.delete(0, tk.END)
    inputtitulo.insert(0, "Categoria")
    inputtitulo.place(relx=0.5, rely=0.3, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    modificarCP.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=350, height=300)

def ModificarP(id_con,premio, categoria):
    cur.execute(f"INSERT INTO premios(premio, categoria, id_premio) VALUES('{premio}', '{categoria}', '{id_con}')")
    cur.execute(f"UPDATE premios SET premio = '{premio}', categoria = '{categoria}' WHERE id_premio = {id_con}")
    conn.commit()
    
def renderAgregarA():
    botonagregarA.place_forget()
    botonmodificarA.place_forget()
    botoneliminarA.place_forget()
    botonrelacionarA.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Anuncio")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputtitulo.delete(0, tk.END)
    inputtitulo.insert(0, "Anunciante")
    inputtitulo.place(relx=0.5, rely=0.2, anchor="center")
    inputlink.delete(0, tk.END)
    inputlink.insert(0, "Links")
    inputlink.place(relx=0.5, rely=0.3, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    agregarA.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def AgregarA(id_ad, anunciante, links):
    cur.execute(f"INSERT INTO anuncios(id_anuncio, nombre_anunciante, links) VALUES('{id_ad}', '{anunciante}', '{links}')")
    conn.commit()

def renderModificarA():
    botonagregarA.place_forget()
    botonmodificarA.place_forget()
    botoneliminarA.place_forget()
    botonrelacionarA.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Anuncio")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputtitulo.delete(0, tk.END)
    inputtitulo.insert(0, "Anunciante")
    inputtitulo.place(relx=0.5, rely=0.2, anchor="center")
    inputlink.delete(0, tk.END)
    inputlink.insert(0, "Links")
    inputlink.place(relx=0.5, rely=0.3, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    modificarA.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def ModificarA(id_ad, anunciante, links):
    cur.execute(f"UPDATE anuncios SET anunciante = '{anunciante}', links = '{links}' WHERE id_anuncio = '{id_ad}'")
    conn.commit()

def renderModificarU():
    botonmodificarU.place_forget()
    botoneliminarU.place_forget()
    print(":)")
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "Usuario")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "Subscripcion")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    modificarU.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def ModificarU(name, correo):
    cur.execute(f"UPDATE subscripcion SET tipo = '{correo}' WHERE usuario = '{name}'")
    conn.commit()

def renderEliminarC():
    botonagregarC.place_forget()
    botonmodificarC.place_forget()
    botoneliminarC.place_forget()
    botonrelacionarC.place_forget()
    print(":)")
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    eliminarU.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def EliminarC(name):
    cur.execute(f"UPDATE multimedia SET estado = 'inactivo' WHERE id = '{name}'")
    conn.commit()

def renderEliminarU():
    botonmodificarU.place_forget()
    botoneliminarU.place_forget()
    print(":)")
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Usuario")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    eliminarU.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def EliminarU(name):
    cur.execute(f"UPDATE usuario SET estado = 'inactivo' WHERE nombre_usuario = '{name}'")
    conn.commit()

def renderEliminarA():
    botonagregarA.place_forget()
    botonmodificarA.place_forget()
    botoneliminarA.place_forget()
    botonrelacionarA.place_forget()
    print(":)")
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Contenido")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    eliminarA.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def EliminarA(name):
    cur.execute(f"UPDATE anuncios SET estado = 'inactivo' WHERE id_anuncio = '{name}'")
    conn.commit()

def renderRelacionarA():
    botonagregarA.place_forget()
    botonmodificarA.place_forget()
    botoneliminarA.place_forget()
    botonrelacionarA.place_forget()
    print(":)")
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Anuncio")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "ID Contenido")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    relacionarA.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def RelacionarA(anuncio, contenido):
    cur.execute(f"INSERT INTO anuncio_contenido(id_anuncio, id_contenido) VALUES('{anuncio}', '{contenido}')")
    conn.commit()

def renderRelacionarR():
    botonagregarC.place_forget()
    botonmodificarC.place_forget()
    botoneliminarC.place_forget()
    botonrelacionarC.place_forget()
    print(":)")
    botonGeneroR.place(relx=0.5, rely=0.2, anchor="center")
    botonActorR.place(relx=0.5, rely=0.4, anchor="center")
    botonDirectorR.place(relx=0.5, rely=0.6, anchor="center")
    botonPremioR.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=300, height=300)

def RelacionarA(anuncio, contenido):
    cur.execute(f"INSERT INTO anuncio_contenido(id_anuncio, id_contenido) VALUES('{anuncio}', '{contenido}')")
    conn.commit()

def renderRelacionarRG():
    botonGeneroR.place_forget()
    botonDirectorR.place_forget()
    botonPremioR.place_forget()
    botonActorR.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Multimedia")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "ID Genero")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    relacionarRG.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def RelacionarRG(contenido, genero):
    cur.execute(f"INSERT INTO genero_contenido(id_contenido, id_genero) VALUES('{contenido}', '{genero}')")
    conn.commit()

def renderRelacionarRA():
    botonGeneroR.place_forget()
    botonDirectorR.place_forget()
    botonPremioR.place_forget()
    botonActorR.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Multimedia")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "ID Actor")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    relacionarRA.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def RelacionarRA(contenido, actor):
    cur.execute(f"INSERT INTO actor_contenido(multimedia_id, actor_id) VALUES('{contenido}', '{actor}')")
    conn.commit()

def renderRelacionarRD():
    botonGeneroR.place_forget()
    botonDirectorR.place_forget()
    botonPremioR.place_forget()
    botonActorR.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Multimedia")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "ID Director")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    relacionarRD.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def RelacionarRD(contenido, director):
    cur.execute(f"INSERT INTO director_contenido(multimedia_id, id) VALUES('{contenido}', '{director}')")
    conn.commit()

def renderRelacionarRP():
    botonGeneroR.place_forget()
    botonDirectorR.place_forget()
    botonPremioR.place_forget()
    botonActorR.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "ID Multimedia")
    inputUsuario.place(relx=0.5, rely=0.1, anchor="center")
    inputUsuario2.delete(0, tk.END)
    inputUsuario2.insert(0, "ID Premios")
    inputUsuario2.place(relx=0.5, rely=0.2, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    relacionarRD.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)

def RelacionarRP(contenido, director):
    cur.execute(f"INSERT INTO premios_contenido(multimedia_id, id) VALUES('{contenido}', '{director}')")
    conn.commit()
        
def administrar():
    botonadministrar.place_forget()
    botonmodificarU.place_forget()
    botoneliminarU.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario3.insert(0, "ID del usuario a hacer administrador")
    inputUsuario3.place(relx=0.5, rely=0.1, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    administracion.place(relx=0.92, rely=0.7, anchor="e")
    entryarea.configure(width=300, height=300)
    typeMenu.place(relx=0.5, rely=0.3, anchor="center")

def administrador(user, clicker):
    cur.execute(f"UPDATE usuario SET isadmin = '{clicker}' WHERE nombre_usuario = '{user}'")
    conn.commit()
    
    

window = tk.Tk(className="Streameo (Working title)")

botonesFont = tkFont.Font(family="@MS UI Gothic", size=16, weight="bold" )
loginFont = tkFont.Font(family="@MS UI Gothic", size=8, weight="bold" )


#Render del logo de la aplicacion


def renderReportes(window):
    window.destroy()
    main_screen()

def inicializacionAdmin():
    window.deiconify()
    entryarea.place(relx=0.5, rely=0.62, anchor="center")
    botonlogin.place(relx=0.5, rely=0.1, anchor="center")
    botonsignup.place(relx=0.5, rely=0.3, anchor="center")
    botonReportes.place(relx=0.5, rely=0.5, anchor="center")
    botonbitacora.place(relx=0.5, rely=0.7, anchor="center")
    botonsalir.place(relx=0.5, rely=0.9, anchor="center")
    #Configuraciones extra de ventana
    window.configure(bg=background)
    window.geometry("900x500")
    window.resizable(False,False)
    window.mainloop()

#Area de inicio, con botones para ir a login, sign up y salir de la aplicacion
entryarea = tk.Canvas(window, width=350, height=400, bg=foreground)
#entryarea.place(relx=0.5, rely=0.62, anchor="center")

botonlogin = tk.Button(entryarea, bg=background, width=20, height=3, text="Contenido", font=botonesFont, command=lambda: renderContenido())
#botonlogin.place(relx=0.5, rely=0.2, anchor="center")

botonsignup = tk.Button(entryarea, bg=background, width=20, height=3, text="Usuarios", font=botonesFont, command=lambda: renderUsuarios())
#botonsignup.place(relx=0.5, rely=0.5, anchor="center")

botonReportes = tk.Button(entryarea, bg=background, width=20, height=3, text="Reportes", font=botonesFont, command=lambda: renderReportes(window))

botonsalir = tk.Button(entryarea, bg=background, width=20, height=3, text="Anuncios", font=botonesFont, command=lambda: renderAnuncios())
#botonsalir.place(relx=0.5, rely=0.8, anchor="center")

botonbitacora = tk.Button(entryarea, bg=background, width=20, height=2, text="Bitacora", font=botonesFont, command=lambda: UI_bitacora())
#botonbitacora.place(relx=0.5, rely=0.8, anchor="center")

botonagregarC = tk.Button(entryarea, bg=background, width=20, height=2, text="Agregar", font=botonesFont, command=lambda: renderMultimedia())

botonmodificarC = tk.Button(entryarea, bg=background, width=20, height=2, text="Modificar", font=botonesFont, command=lambda: renderMultimedia2())

botoneliminarC = tk.Button(entryarea, bg=background, width=20, height=2, text="Eliminar", font=botonesFont, command=lambda: renderEliminarC())

botonrelacionarC = tk.Button(entryarea, bg=background, width=20, height=2, text="Relacionar", font=botonesFont, command=lambda: renderRelacionarR())

botonmodificarU = tk.Button(entryarea, bg=background, width=20, height=3, text="Modificar", font=botonesFont, command=lambda: renderModificarU())

botoneliminarU = tk.Button(entryarea, bg=background, width=20, height=3, text="Eliminar", font=botonesFont, command=lambda: renderEliminarU())

botonagregarA = tk.Button(entryarea, bg=background, width=20, height=2, text="Agregar", font=botonesFont, command=lambda: renderAgregarA())

botonmodificarA = tk.Button(entryarea, bg=background, width=20, height=2, text="Modificar", font=botonesFont, command=lambda: renderModificarA())

botoneliminarA = tk.Button(entryarea, bg=background, width=20, height=2, text="Eliminar", font=botonesFont, command=lambda: renderEliminarA())

botonrelacionarA = tk.Button(entryarea, bg=background, width=20, height=2, text="Relacionar", font=botonesFont, command=lambda: renderRelacionarA())

botonMultimedia = tk.Button(entryarea, bg=background, width=20, height=1, text="Multimedia", font=botonesFont, command=lambda: renderMultimedia1A())

botonGenero = tk.Button(entryarea, bg=background, width=20, height=1, text="Genero", font=botonesFont, command=lambda: renderGenero())

botonActor = tk.Button(entryarea, bg=background, width=20, height=1, text="Actor", font=botonesFont, command=lambda: renderActor())

botonDirector = tk.Button(entryarea, bg=background, width=20, height=1, text="Director", font=botonesFont, command=lambda: renderDirector())

botonPremio = tk.Button(entryarea, bg=background, width=20, height=1, text="Premios", font=botonesFont, command=lambda: renderPremios())

botonMultimediaM = tk.Button(entryarea, bg=background, width=20, height=1, text="Multimedia", font=botonesFont, command=lambda: renderMultimedia1C())

botonGeneroM = tk.Button(entryarea, bg=background, width=20, height=1, text="Genero", font=botonesFont, command=lambda: renderGeneroM())

botonActorM = tk.Button(entryarea, bg=background, width=20, height=1, text="Actor", font=botonesFont, command=lambda: renderActorM())

botonDirectorM = tk.Button(entryarea, bg=background, width=20, height=1, text="Director", font=botonesFont, command=lambda: renderDirectorM())

botonPremioM = tk.Button(entryarea, bg=background, width=20, height=1, text="Premios", font=botonesFont, command=lambda: renderPremiosM())

botonGeneroR = tk.Button(entryarea, bg=background, width=20, height=1, text="Genero", font=botonesFont, command=lambda: renderRelacionarRG())

botonActorR = tk.Button(entryarea, bg=background, width=20, height=1, text="Actor", font=botonesFont, command=lambda: renderRelacionarRA())

botonDirectorR = tk.Button(entryarea, bg=background, width=20, height=1, text="Director", font=botonesFont, command=lambda: renderRelacionarRD())

botonPremioR = tk.Button(entryarea, bg=background, width=20, height=1, text="Premios", font=botonesFont, command=lambda: renderRelacionarRP())

botonadministrar = tk.Button(entryarea, bg=background, width=20, height=3, text="Administrar", font=botonesFont, command=lambda: administrar())

clicked = StringVar()
clicked.set("true")
typeMenu = OptionMenu(entryarea, clicked, "true", "false")

#Area de login
inputUsuario = tk.Entry(entryarea, width=30)
inputUsuario.bind("<Button-1>", lambda event: clear_entradas(event, inputUsuario))
inputUsuario2 = tk.Entry(entryarea, width=30)
inputUsuario2.bind("<Button-1>", lambda event: clear_entradas(event, inputUsuario2))
inputUsuario3 = tk.Entry(entryarea, width=40)
inputUsuario3.bind("<Button-1>", lambda event: clear_entradas(event, inputUsuario3))
inputtitulo = tk.Entry(entryarea, width=30)
inputtitulo.bind("<Button-1>", lambda event: clear_entradas(event, inputtitulo))
inputgenero = tk.Entry(entryarea, width=30)
inputgenero.bind("<Button-1>", lambda event: clear_entradas(event, inputgenero))
inputlink = tk.Entry(entryarea, width=30)
inputlink.bind("<Button-1>", lambda event: clear_entradas(event, inputlink))
inputtipo = tk.Entry(entryarea, width=30)
inputtipo.bind("<Button-1>", lambda event: clear_entradas(event, inputtipo))
inputduracion = tk.Entry(entryarea, width=30)
inputduracion.bind("<Button-1>", lambda event: clear_entradas(event, inputduracion))
cal = DateEntry(entryarea,selectmode='day')
inputcal = ''
volverMenu = tk.Button(entryarea, bg=background, width=10, height=2, text="Volver", font=loginFont, command=lambda: renderStart())
loguearse = tk.Button(entryarea, bg=background, width=10, height=2, text="Login", font=loginFont, command=lambda: logueandose(inputUsuario, inputContra))
agregarC = tk.Button(entryarea, bg=background, width=10, height=2, text="Agregar", font=loginFont, command=lambda: AgregarC(inputUsuario.get(), inputtitulo.get(), inputlink.get(), inputtipo.get(), inputduracion.get(), cal.get_date()))
agregarCA = tk.Button(entryarea, bg=background, width=10, height=2, text="Agregar", font=loginFont, command=lambda: AgregarCA(inputUsuario.get(), inputUsuario2.get()))
agregarCD = tk.Button(entryarea, bg=background, width=10, height=2, text="Agregar", font=loginFont, command=lambda: AgregarCD(inputUsuario.get(), inputUsuario2.get()))
agregarCG = tk.Button(entryarea, bg=background, width=10, height=2, text="Agregar", font=loginFont, command=lambda: AgregarCG(inputUsuario.get(), inputUsuario2.get()))
agregarCP = tk.Button(entryarea, bg=background, width=10, height=2, text="Agregar", font=loginFont, command=lambda: AgregarCAP(inputUsuario.get(), inputUsuario2.get(), inputtitulo.get()))
modificarC = tk.Button(entryarea, bg=background, width=10, height=2, text="Modificar", font=loginFont, command=lambda: ModificarC(inputUsuario.get(), inputtitulo.get(), inputlink.get(), inputtipo.get(), inputduracion.get(), cal.get_date()))
modificarCA = tk.Button(entryarea, bg=background, width=10, height=2, text="Modificar", font=loginFont, command=lambda: ModificarCA(inputUsuario.get(), inputUsuario2.get()))
modificarCD = tk.Button(entryarea, bg=background, width=10, height=2, text="Modificar", font=loginFont, command=lambda: ModificarCD(inputUsuario.get(), inputUsuario2.get()))
modificarCG = tk.Button(entryarea, bg=background, width=10, height=2, text="Modificar", font=loginFont, command=lambda: ModificarCG(inputUsuario.get(), inputUsuario2.get()))
modificarCP = tk.Button(entryarea, bg=background, width=10, height=2, text="Modificar", font=loginFont, command=lambda: ModificarCAP(inputUsuario.get(), inputUsuario2.get(), inputtitulo.get()))
eliminarC = tk.Button(entryarea, bg=background, width=10, height=2, text="Eliminar", font=loginFont, command=lambda: EliminarC(inputUsuario.get()))
modificarU = tk.Button(entryarea, bg=background, width=10, height=2, text="Modificar", font=loginFont, command=lambda: ModificarU(inputUsuario.get(), inputUsuario2.get()))
eliminarU = tk.Button(entryarea, bg=background, width=10, height=2, text="Eliminar", font=loginFont, command=lambda: EliminarU(inputUsuario.get()))
agregarA = tk.Button(entryarea, bg=background, width=10, height=2, text="Agregar", font=loginFont, command=lambda: AgregarA(inputUsuario.get(), inputtitulo.get(), inputlink.get()))
modificarA = tk.Button(entryarea, bg=background, width=10, height=2, text="Agregar", font=loginFont, command=lambda: ModificarA(inputUsuario.get(), inputtitulo.get(), inputlink.get()))
eliminarA = tk.Button(entryarea, bg=background, width=10, height=2, text="Eliminar", font=loginFont, command=lambda: EliminarA(inputUsuario.get()))
relacionarA = tk.Button(entryarea, bg=background, width=10, height=2, text="Eliminar", font=loginFont, command=lambda: RelacionarA(inputUsuario.get(), inputUsuario2.get()))
relacionarRG = tk.Button(entryarea, bg=background, width=10, height=2, text="Eliminar", font=loginFont, command=lambda: RelacionarRG(inputUsuario.get(), inputUsuario2.get()))
relacionarRA = tk.Button(entryarea, bg=background, width=10, height=2, text="Eliminar", font=loginFont, command=lambda: RelacionarRA(inputUsuario.get(), inputUsuario2.get()))
relacionarRD = tk.Button(entryarea, bg=background, width=10, height=2, text="Eliminar", font=loginFont, command=lambda: RelacionarRD(inputUsuario.get(), inputUsuario2.get()))
relacionarRP = tk.Button(entryarea, bg=background, width=10, height=2, text="Eliminar", font=loginFont, command=lambda: RelacionarRP(inputUsuario.get(), inputUsuario2.get()))
administracion = tk.Button(entryarea, bg=background, width=10, height=2, text="Administrar", font=loginFont, command=lambda: administrador(inputUsuario3.get(), clicked.get()))

#inicializacionAdmin()



