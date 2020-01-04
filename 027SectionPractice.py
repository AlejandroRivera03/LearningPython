texto = "un dia que el viento soplaba con fuerza#mira como se mueve aquela banderola -dijo un monje#lo que se mueve es el viento -respondio otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
lineas = texto.split( '#' )
for i, linea in enumerate( lineas ):
    lineas[i] = linea.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + '...'
    else:
        lineas[i] = '- ' + lineas[i] + '.'

for linea in lineas:
    print( linea )

print( '\n' )
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(l):
    l = list( set( l ) ) # lista a conjunto elimina elementos duplicados
    l.sort( reverse=True ) # ordenando de mayor a menor
    for i,n in enumerate(l):
        if n%2 != 0: # si es impar se elimina elemento
            del( l[i] )
    suma = sum( l )
    l.insert(0, suma) # la sumatoria de los elementos lo añadimos al primer elemento
    return l

nueva_lista = modificar( lista )
print( nueva_lista[0] == sum( nueva_lista[1:] ) ) # comprobando que el primer elemento es igual a la sumatoria del resto de elementos
print( lista )
print( nueva_lista )