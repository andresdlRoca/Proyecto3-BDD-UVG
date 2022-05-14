import psycopg2
import bcrypt


user = "RVC1"
password = "123456789"
passwd = bytes(password, 'utf-8')

hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())

 

print(passwd)
print(hashed)
hashed = hashed.decode("utf-8")




connection = psycopg2.connect(database="proyecto2", user="postgres", password="videogamesfan10", host="localhost", port=5432)

cursor = connection.cursor()
cursor.execute(f'''UPDATE usuario SET contraseña = '{hashed}' WHERE nombre_usuario = '{user}';''')
connection.commit()
connection.close()


