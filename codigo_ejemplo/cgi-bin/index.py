#!/usr/bin/python3
# import cgi

# print ("Content-type: text/html")
# print

# print ("""
# Hola Mundo
# """)

# form=cgi.FieldStorage()
# print ("<p>user:", form["user"].value)
# print ("<p>pass:", form["pass"].value)

import psycopg2
import bcrypt

# Conectarse a la base de datos
conn = psycopg2.connect(
    database="Usuarios",
    user="admin",
    password="losfifas",
    host="10.0.0.4",
    port="5432"
)

cur = conn.cursor()

def registrar_usuario(username, password):
    # Generar un hash de la contraseña
    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insertar el usuario en la base de datos
    cur.execute("INSERT INTO Usuarios (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()

def verificar_credenciales(username, password):
    cur.execute("SELECT password FROM Usuarios WHERE username = %s", (username,))
    password = cur.fetchone()

    if password and bcrypt.checkpw(password.encode('utf-8'), password[0].encode('utf-8')):
        return True
    else:
        return False

# Ejemplo de registro de usuario
registrar_usuario('usuario_prueba', 'contraseña_secreta')

# Ejemplo de verificación de credenciales
if verificar_credenciales('usuario_prueba', 'contraseña_secreta'):
    print("Inicio de sesión exitoso")
else:
    print("Credenciales incorrectas")


