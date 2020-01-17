from tkinter import Tk, Frame, Label, StringVar, PhotoImage, Entry, Text, Button, Radiobutton, IntVar, Checkbutton, Menu, messagebox as Messagebox

def sumar():
    r.set( float( n1.get() ) + float( n2.get() ) )

def restar():
    r.set( float( n1.get() ) - float( n2.get() ) )

def producto():
    r.set( float( n1.get() ) * float( n2.get() ) )

def seleccionar():
    monitor.config( text='valor {}'.format( opcion.get() ) )

def reset():
    opcion.set( None )
    monitor.config( text='' )

def coffee():
    cadena = ''
    if( leche.get() ):
        cadena += 'Con leche, '
    else:
        cadena += 'Sin leche, '
    if( azucar.get() ):
        cadena += 'Con azucar'
    else:
        cadena += 'Sin azucar'
    customcoffe.config( text='{}'.format( cadena ) )

def infoPopup():
    Messagebox.showinfo( 'Informacion', 'Este es un popup informativo')

def warningPopup():
    Messagebox.showwarning( 'Alerta', 'Este es un popup de alerta')   

def errorPopup():
    Messagebox.showerror( 'Error', 'Este es un popup de error') 

def askQuestionPopup():
    resultado = Messagebox.askquestion( 'Pregunta', 'Este es un popup de pregunta si-no, devuelve "yes" o "no" (str)') 
    print( resultado )

def askOkCalcelPopup():
    resultado = Messagebox.askokcancel( 'Pregunta', 'Este es un popup de pregunta ok-cancelar, devuelve True o False') 
    print( resultado )

def askYesNoPopup():
    resultado = Messagebox.askyesno( 'Pregunta', 'Este es un popup de pregunta si-no, devuelve True o False') 
    print( resultado )

def askRetryCalcelPopup():
    resultado = Messagebox.askretrycancel( 'Reintentar', 'Este es un popup de re-intento, devuelve True o False') 
    print( resultado )

root = Tk()

root.title( 'Ventanita' )
root.resizable( 1, 1 ) # first for x axis, second for y axis
root.iconbitmap( 'icono.ico' )
root.config(width=1200, height=250)

menubar = Menu( root )
root.config( menu=menubar )

filemenu = Menu( menubar, tearoff=0 )
filemenu.add_command( label='Nuevo' )
filemenu.add_command( label='Abrir' )
filemenu.add_command( label='Guardar' )
filemenu.add_command( label='Cerrar' )
filemenu.add_separator()
filemenu.add_command( label='Salir', command=root.quit )

editmenu = Menu( menubar, tearoff=0 )
editmenu.add_command( label='Cortar' )
editmenu.add_command( label='Copiar' )
editmenu.add_command( label='Pegar' )

helpmenu = Menu( menubar, tearoff=0 )
helpmenu.add_command( label='Ayuda' )
filemenu.add_separator()
helpmenu.add_command( label='Acerca de...' )


menubar.add_cascade( label='Archivo', menu=filemenu )
menubar.add_cascade( label='Editar', menu=editmenu )
menubar.add_cascade( label='Ayuda', menu=helpmenu )

frame = Frame( root, width=300, height=250 )
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

entriesSection = Frame( root, width=260, height=250 )
# entriesSection.config( bg='green' )
entriesSection.place(x=300, y=0)

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


n1 = StringVar()
n2 = StringVar()
r = StringVar()

buttonSection = Frame( root, width=230, height=250 )
buttonSection.place(x=560, y=0)

Label( buttonSection, text='Primer numero' ).grid( row=0, column=0, sticky='e' )
Entry( buttonSection, justify='center', textvariable=n1 ).grid( row=0, column=1 )
Label( buttonSection, text='Segundo numero' ).grid( row=1, column=0, sticky='e' )
Entry( buttonSection, justify='center', textvariable=n2 ).grid( row=1, column=1 )
Label( buttonSection, text='Resultado' ).grid( row=2, column=0, sticky='e' )
Entry( buttonSection, justify='center', textvariable=r, state='disabled' ).grid( row=2, column=1 )
Button( buttonSection, text='Suma', command=sumar ).grid( row=3, column=0, sticky='we' )
Button( buttonSection, text='Resta', command=restar ).grid( row=4, column=0, sticky='we' )
Button( buttonSection, text='Producto', command=producto ).grid( row=5, column=0, sticky='we' )

radioSection = Frame( root, width=80, height=250 )
radioSection.place( x=790, y=0 )

opcion = IntVar()
Radiobutton( radioSection, text='Opcion 1', variable=opcion, value=1, command=seleccionar ).pack()
Radiobutton( radioSection, text='Opcion 2', variable=opcion, value=2, command=seleccionar ).pack()
Radiobutton( radioSection, text='Opcion 3', variable=opcion, value=3, command=seleccionar ).pack()
monitor = Label( radioSection )
monitor.pack()
Button( radioSection, text='Reiniciar', command=reset ).pack()


checkSection = Frame( root, width=130, height=250 )
checkSection.place( x=870, y=0 )

leche = IntVar()
azucar = IntVar()

Label( checkSection, text='Personaliza tu cafe' ).pack( anchor='w' )
Checkbutton(checkSection, text='Con leche', variable=leche, onvalue=1, offvalue=0, command=coffee ).pack( anchor='w' )
Checkbutton(checkSection, text='Con azucar', variable=azucar, onvalue=1, offvalue=0, command=coffee ).pack( anchor='w' )
customcoffe = Label( checkSection )
customcoffe.config( text='Sin leche, Sin azucar' )
customcoffe.pack()

popupsSection = Frame( root, width=200, height=250 )
popupsSection.place( x=1000, y=0 )
Button( popupsSection, text='Info Popup', command=infoPopup ).pack( anchor="w" )
Button( popupsSection, text='Alert Popup', command=warningPopup ).pack( anchor="w" )
Button( popupsSection, text='Error Popup', command=errorPopup ).pack( anchor="w" )
Button( popupsSection, text='Ask Question Popup', command=askQuestionPopup ).pack( anchor="w" )
Button( popupsSection, text='Ask Ok Cancel Popup', command=askOkCalcelPopup ).pack( anchor="w" )
Button( popupsSection, text='Ask Yes No Popup', command=askYesNoPopup ).pack( anchor="w" )
Button( popupsSection, text='Ask Retry Cancel Popup', command=askRetryCalcelPopup ).pack( anchor="w" )

root.mainloop() # Always put it at the end