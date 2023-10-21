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
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iniciar Sesión</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="login-info">
    <h1>Resultados del Login: </h1>
    """)
form=cgi.FieldStorage()
user = form["user"].value
passw = form["pass"].value
# print ("<p>user:", user)
#print ("<p>pass:", passw)

try:
    #print("<p> Los datos fueron Usuario: "+user+" y Contrasena: "+passw)
    connection = psycopg2.connect(user = "admin",
                                  password = "losfifas",
                                  host = "10.0.0.4",
                                  port = "5432",
                                  database = "usuarios")
    cursor = connection.cursor()

    # def registrar_usuario(username, passw):
    #     password_hash = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    #     cursor.execute("INSERT INTO Usuarios (username, password) VALUES (%s, %s)", (username, password_hash))
    #     connection.commit()

    # cursor.execute("SELECT password FROM Usuarios WHERE username = %s", (user,))
    # Consulta parametrizada
    query = "SELECT password FROM Usuarios WHERE username = %s"
    cursor.execute(query, (user,))
    # password_hash = cursor.fetchone()[0].encode('utf8')
    password = cursor.fetchone()[0].encode('utf8')
    if password is not None:
        # password = password.decode('utf-8')
        # password = password.strip()
        # if password == passw:
        if bcrypt.checkpw(passw.encode('utf8'), password):
            print(f"""
                <div class="login-container login-success">
                    <h2> Bienvenido {user}!!</h2>

                    <div class="login-datos">
                        <h3>Tus datos son:</h3>
                        <p>Usuario: {user}</p>
                        <p>Contraseña: {passw}</p>
                    </div>
                </div>
                """)
            # registrar_usuario('usuario1', 'contr1')
            # registrar_usuario('usuario2', 'contr2')
            # registrar_usuario('usuario3', 'contr3')
        else:
            print(f"""
                <div class="login-container login-fail">
                    <h2>Contraseña incorrecta</h2>
                    <p>Contraseña1: {passw.encode('utf8')}</p>
                    <p>Contraseña2: {password}</p>
                </div>
                """)
            # registrar_usuario('usuario4', 'contr4')
            # registrar_usuario('usuario5', 'contr5')
            # registrar_usuario('usuario6', 'contr6')
    else:
        print("""
            <div class="login-container login-fail">
                <h2>Usuario no encontrado</h2>
            </div>
            """)
        # registrar_usuario('usuario7', 'contr7')
        # registrar_usuario('usuario8', 'contr8')
        # registrar_usuario('usuario9', 'contr9')
#     if bcrypt.checkpw(passw.encode('utf8'), password_hash):
#         print("<h2> Bienvenido :D " + user + " </h2>")
#     else:
#         print("<h2> Ese nombre no me suena D: </h2>")
# except (Exception, psycopg2.Error) as error :
    # print("Error while connectiong to PostgreSQL", error)
except psycopg2.OperationalError as e:
    #print("<p> Linea despues del SELECT - EXCEPT")
    print(f"<p>Error al conectar a la base de datos: {e}</p>")
finally:
    if(connection):
        cursor.close()
        connection.close()

print("""
    </div>
</body>
</html>
""")

