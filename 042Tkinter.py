from tkinter import Tk, Frame, Label, StringVar, PhotoImage

root = Tk()

root.title( 'Ventanita' )
root.resizable( 1, 1 ) # first for x axis, second for y axis
root.iconbitmap( 'icono.ico' )

frame = Frame( root, width=480, height=320 )
frame.config( cursor='pirate' )
frame.config( bg='lightblue' )
frame.config( bd=5 )
frame.config( relief='sunken' )
# frame.pack( side='bottom', anchor='w' )
# frame.pack( fill='both', expand=1 )
frame.pack()

texto = StringVar()
texto.set( 'Tercer etiqueta!' )

Label( frame, text='Primer etiqueta' ).place(x=0, y=0)

label = Label( frame, text='Segunda etiqueta' )
label.place(x=0, y=25)
label.config( bg='green', fg='white', font=('Verdana', 24) )

label2 = Label( frame, text='algo' )
label2.place(x=100, y=0)
label2.config( textvariable=texto )

imagen = PhotoImage( file='oso.gif' )
Label( frame, image=imagen, bd=0 ).place(x=0, y=80)

root.mainloop() # Always put it at the end