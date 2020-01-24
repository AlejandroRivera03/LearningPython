import sqlite3
from tkinter import *

root = Tk()
root.title( 'Bar don Rivera - Menú' )
root.resizable(0,0)
root.config( bd=25, relief='sunken' )

Label( root, text='   Bar Don Rivera   ', fg='darkgreen', font=( 'Times New Roman', 28, 'bold italic' ) ).pack()
Label( root, text='Menú del dia', fg='green', font=( 'Times New Roman', 24, 'bold italic' ) ).pack()
Label( root, text='' ).pack()

conexion = sqlite3.connect( 'restaurante.db' )
cursor = conexion.cursor()

categorias = cursor.execute( 'SELECT * FROM categoria' ).fetchall()
for categoria in categorias:
    Label( root, text=categoria[1], fg='black', font=( "Times New Roman", 20, 'bold italic' ) ).pack()

    platos = cursor.execute( 'SELECT * FROM plato WHERE categoria_id={}'.format( categoria[0] ) ).fetchall()
    for plato in platos:
        Label( root, text=plato[1], fg='gray', font=( 'Verdana', 15, 'italic' ) ).pack()
    
    Label( root, text='' ).pack()

conexion.close()

Label( root, text='$40 (IVA Incluido)', fg='darkgreen', font=( 'Times New Roman', 16, 'bold italic' ) ).pack( side='right' )

root.mainloop()