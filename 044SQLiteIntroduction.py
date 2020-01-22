import sqlite3

conexion = sqlite3.connect( 'ejemplo.db' )
cursor = conexion.cursor()

# cursor.execute( 'CREATE TABLE usuarios (name VARCHAR(100), edad INTEGER, email VARCHAR(100) )' )

# cursor.execute( 'INSERT INTO usuarios VALUES ( "alejandro", 25, "alejandro@ejemplo.com" )' )

# cursor.execute( 'SELECT * FROM usuarios' )
# usuario = cursor.fetchone()
# print( usuario )

# usuarios = [
#     ('Miguel', 44, 'miguel@ejemplo.com'),
#     ('Jose', 62, 'jose@ejemplo.com'),
#     ('Manuel', 36, 'manuel@ejemplo.com'),
# ]
# cursor.executemany( 'INSERT INTO usuarios VALUES (?,?,?)', usuarios )

cursor.execute( 'SELECT * FROM usuarios' )
usuarios = cursor.fetchall()
print( usuarios )

conexion.commit()
conexion.close()