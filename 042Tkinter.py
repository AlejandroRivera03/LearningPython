from tkinter import Tk, Frame

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

root.mainloop() # Always put it at the end