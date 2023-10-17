#!/usr/bin/python3
import cgi
import psycopg2
import bcrypt

# print ("Content-type: text/html")
# # # print

# print ("""
# Hola Mundo
# """)

# form=cgi.FieldStorage()
# print ("<p>user:", form["user"].value)
# print ("<p>pass:", form["pass"].value)

#import psycopg2
# import bcrypt

# ---------------- CAMBIOS ANTERIORES ----------------
# Conectarse a la base de datos
# conn = psycopg2.connect(
#     database="Usuarios",
#     user="admin",
#     password="losfifas",
#     host="10.0.0.4",
#     port="5432"
# )

# cur = conn.cursor()

# def registrar_usuario(username, password):
#     # Generar un hash de la contraseña
#     password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#     # Insertar el usuario en la base de datos
#     cur.execute("INSERT INTO Usuarios (username, password) VALUES (%s, %s)", (username, password))
#     conn.commit()

# def verificar_credenciales(username, password):
#     cur.execute("SELECT password FROM Usuarios WHERE username = %s", (username,))
#     password = cur.fetchone()

#     if password and bcrypt.checkpw(password.encode('utf-8'), password[0].encode('utf-8')):
#         return True
#     else:
#         return False

# # Ejemplo de registro de usuario
# registrar_usuario('usuario_prueba', 'contraseña_secreta')

# # Ejemplo de verificación de credenciales
# if verificar_credenciales('usuario_prueba', 'contraseña_secreta'):
#     print("Inicio de sesión exitoso")
# else:
#     print("Credenciales incorrectas")
# ----------------------------------------------------------------

print ("Content-type: text/html")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta chaset="UTF-8">
    <meta name="viewport" content="widtg=device-width, initial-scale=1.0>
    <title>Iniciar Sesión</title>
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
    <div id="login-container">
    <h1>Resultados del Login: </h1>
    """)
form=cgi.FieldStorage()
user = form["user"].value
passw = form["pass"].value
print ("<p>user:", user)
print ("<p>pass:", passw)

try:
    print("<p> Los datos fueron Usuario: "+user+" y Contrasena: "+passw)
    connection = psycopg2.connect(user = "admin",
                                  password = "losfifas",
                                  host = "10.0.0.4",
                                  port = "5432",
                                  database = "usuarios")
    cursor = connection.cursor()

    cursor.execute("SELECT password FROM Usuarios WHERE username = %s", (user,))
    print("<p> Linea despues del SELECT - TRY")
    # password_hash = cursor.fetchone()[0].encode('utf8')
    password = cursor.fetchone()
    if password is not None:
        print("<p>Si se hizo el SELECT</p>")
        print(f"<p>{password}</p>")
        if password == passw:
            print("<h2> Bienvenido :D " + user + " </h2>")
        else:
            print("<h2> Ese nombre no me suena D: </h2>")
    else:
        print("<p>No se hizo el SELECT</p>")
#     if bcrypt.checkpw(passw.encode('utf8'), password_hash):
#         print("<h2> Bienvenido :D " + user + " </h2>")
#     else:
#         print("<h2> Ese nombre no me suena D: </h2>")
# except (Exception, psycopg2.Error) as error :
    # print("Error while connectiong to PostgreSQL", error)
except psycopg2.OperationalError as e:
    print("<p> Linea despues del SELECT - EXCEPT")
    print(f"Error al conectar a la base de datos: {e}")
finally:
    if(connection):
        cursor.close()
        connection.close()

print("""
    </div>
</body>
</html>
""")