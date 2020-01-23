import sqlite3

conexion = sqlite3.connect( 'usuarios.db' )
cursor = conexion.cursor()

########## DNI PRIMARY KEY ##########

# cursor.execute('''
#     CREATE TABLE usuarios (
#         dni VARCHAR(9) PRIMARY KEY,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')

# usuarios = [
#     ( '11111111A', 'alejandro', 25, 'alejandro@ejemplo.com' ),
#     ( '22222222B', 'Miguel', 44, 'miguel@ejemplo.com' ),
#     ( '33333333D', 'Jose', 62, 'jose@ejemplo.com' ),
#     ( '44444444D', 'Manuel', 36, 'manuel@ejemplo.com' ),
# ]

# cursor.executemany( 'INSERT INTO usuarios VALUES ( ?, ?, ?, ? )', usuarios )
cursor.execute( 'SELECT * FROM usuarios' )
usuarios = cursor.fetchall()
for usuario in usuarios:
    print( usuario )

########## INTEGER PRIMARY KEY AUTOINCREMENT ##########

# cursor.execute('''
#     CREATE TABLE productos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCAR(100) NOT NULL,
#         marca VARCHAR(100) NOT NULL,
#         precio FLOAT NOT NULL
#     )
# ''')

# productos = [
#     ( 'Teclado', 'Logitech', 299.00 ),
#     ( 'Pantalla 19"', 'LG', 2999.00 )
# ]

# cursor.executemany( 'INSERT INTO productos VALUES (null, ?, ?, ?)', productos )
cursor.execute( 'SELECT * FROM productos' )
productos = cursor.fetchall()
for producto in productos:
    print( producto )

########## DNI AND PRIMARY KEY AUTOINCREMENT ##########

# cursor.execute('''
#     CREATE TABLE otherusuarios (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dni VARCHAR(9) UNIQUE,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')

# usuarios = [
#     ( '11111111A', 'alejandro', 25, 'alejandro@ejemplo.com' ),
#     ( '22222222B', 'Miguel', 44, 'miguel@ejemplo.com' ),
#     ( '33333333C', 'Jose', 62, 'jose@ejemplo.com' ),
#     ( '44444444D', 'Manuel', 36, 'manuel@ejemplo.com' ),
# ]

# cursor.executemany( 'INSERT INTO otherusuarios VALUES ( null, ?, ?, ?, ? )', usuarios )

# Line with error about the repeated unique key
# cursor.execute( 'INSERT INTO otherusuarios VALUES ( null, "44444444D", "fulanito", "30", "fulano@ejemplo.com" )' )

cursor.execute( 'SELECT * FROM otherusuarios' )
otherusuarios = cursor.fetchall()
for otherusers in otherusuarios:
    print( otherusers )

conexion.commit()
conexion.close()