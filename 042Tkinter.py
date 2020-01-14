from tkinter import Tk, Frame, Label, StringVar, PhotoImage, Entry, Text

root = Tk()

root.title( 'Ventanita' )
root.resizable( 1, 1 ) # first for x axis, second for y axis
root.iconbitmap( 'icono.ico' )
root.config(width=480, height=501)

frame = Frame( root, width=480, height=250 )
frame.config( cursor='pirate' )
frame.config( bg='lightblue' )
frame.config( bd=5 )
frame.config( relief='sunken' )
# frame.pack( side='bottom', anchor='w' )
# frame.pack( fill='both', expand=1 )
frame.place(x=0, y=0)

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

entriesSection = Frame( root, width=480, height=250 )
# entriesSection.config( bg='green' )
entriesSection.place(x=0, y=251)

labelentry1 = Label( entriesSection, text='Nombre (s)' )
labelentry1.grid( row=0, column=0, padx=3, pady=3, sticky='e' )

entry1 = Entry( entriesSection )
entry1.grid( row=0, column=1, padx=3, pady=3 )
entry1.config( justify='right' )

labelentry2 = Label( entriesSection, text='Apellidos' )
labelentry2.grid( row=1, column=0, padx=3, pady=3, sticky='e' )

entry2 = Entry( entriesSection )
entry2.grid( row=1, column=1, padx=3, pady=3 )
entry2.config( justify='center' )

labelentry3 = Label( entriesSection, text='Telefono' )
labelentry3.grid( row=2, column=0, padx=3, pady=3, sticky='e' )

entry3 = Entry( entriesSection )
entry3.grid( row=2, column=1, padx=3, pady=3 )

labelentry4 = Label( entriesSection, text='Campo deshabilitado' )
labelentry4.grid( row=3, column=0, padx=3, pady=3, sticky='e' )

entry4 = Entry( entriesSection )
entry4.grid( row=3, column=1, padx=3, pady=3 )
entry4.config( state='disabled' )

labelentry5 = Label( entriesSection, text='Contraseña' )
labelentry5.grid( row=4, column=0, padx=3, pady=3, sticky='e' )

entry5 = Entry( entriesSection )
entry5.grid( row=4, column=1, padx=3, pady=3 )
entry5.config( show='*' )

labelentry6 = Label( entriesSection, text='Box' )
labelentry6.grid( row=5, column=0, padx=3, pady=3, sticky='ne' )

entry6 = Text( entriesSection )
entry6.grid( row=5, column=1, padx=3, pady=3 )
entry6.config( width=16, height=5, font=('Console', 10), selectbackground='red', padx=5 )

root.mainloop() # Always put it at the end