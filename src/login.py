###############################################
#   login.py
###############################################
#   Universidad del Valle de Guatemala
#   Bases de datos 1
#   Proyecto 1
#   Presentado por:
#   Andres de la Roca
#   Jun Woo Lee
#   
#   Ver 1.0
###############################################
import psycopg2
import bcrypt
from datetime import date

conn = psycopg2.connect("host=localhost dbname=proyecto3 user=postgres password=rwby123")
cur = conn.cursor()

def loginInfo(usuario, contraseña):

    #fetchLoginInfo_Query = "SELECT nombre_usuario,contraseña FROM usuario WHERE usuario.nombre_usuario = '{0}'".format(usuario)
    cur.execute("""
        SELECT  nombre_usuario,contraseña
        FROM    usuario
        WHERE   usuario.nombre_usuario = %(usuario)s
    """, {
        'usuario': usuario
    })
    login_records = cur.fetchall()

    if login_records is None:
        print("No existe ese usuario")
        return False

    if not login_records:
        print("No existe ese usuario")
        return False
    contraseñaSQL = login_records[0][1]
    contraseña = bytes(contraseña, 'utf-8') 
    contraseñaSQL = bytes(contraseñaSQL, 'utf-8')
    if bcrypt.hashpw(contraseña, contraseñaSQL) == contraseñaSQL:
        cur.execute(f"INSERT INTO registros(usuario_id) VALUES('{usuario}')")
        conn.commit()
        return True
    else:
        print("Esa contraseña no es la correcta...")
        cur.execute("select id_intento from seguridad")
        tries =  cur.fetchall()
        id_tries = len(tries) + 1
        fecha = date.today()
        cur.execute("INSERT INTO seguridad (id_intento, fecha, usuario) values (%s, %s, %s)",
                    (id_tries, fecha, usuario))
        conn.commit()
        return False

def checkAdmin(usuario):
    cur.execute("""
        SELECT isadmin
        FROM usuario
        WHERE usuario.nombre_usuario = %(usuario)s

    """ , {
        "usuario": usuario
    })

    adminState = cur.fetchall()
    #print(adminState[0][0])
    return adminState[0][0]
