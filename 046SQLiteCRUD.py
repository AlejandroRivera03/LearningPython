import sqlite3

conexion = sqlite3.connect( 'usuarios.db' )
cursor = conexion.cursor()

cursor.execute( 'SELECT * FROM otherusuarios WHERE edad=25' )
usuario = cursor.fetchone()
print( '\nUsuarios donde edad=25 => {}'.format( usuario ) )

cursor.execute( 'UPDATE otherusuarios SET edad=25 WHERE id=4' )
cursor.execute( 'UPDATE otherusuarios SET nombre="Alejandro" WHERE id=1' )

print( '\nSet edad=25 where id=4' )
print( 'Set nombre="Alejandro" where id=1 =>' )
cursor.execute( 'SELECT * FROM otherusuarios' )
usuarios = cursor.fetchall()
for user in usuarios:
    print( user )

cursor.execute( 'SELECT * FROM otherusuarios WHERE edad=25' )
usuarios = cursor.fetchall()
print( '\nUsuarios donde edad=25 => {}'.format( usuarios ) )

print( '\nDELETE FROM otherusuarios WHERE id=3' )
# cursor.execute( 'DELETE FROM otherusuarios WHERE id=3' )
cursor.execute( 'SELECT * FROM otherusuarios' )
usuarios = cursor.fetchall()
for user in usuarios:
    print( user )

conexion.commit()
conexion.close()