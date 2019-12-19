from collections import deque

# Tuplas
tupla = (100, 'hola', [1,2,3,4], -50)
# Tuplas accept index and slicing
print( tupla )
print( tupla[0] )
print( tupla[-1] )
print( tupla[2:] )
print( tupla[2][-2] )
print( len(tupla) )

# index method that returns the index of the indicated value
print( tupla.index(-50) )
# count method that count how many time an element is in the tupla
print( tupla.count(100) )


# Conjuntos
conjunto = set()
conjunto = {1,2,3}
conjunto.add(4)
conjunto.add(0)
conjunto.add('H')
conjunto.add('Z')
conjunto.add('A')
print( conjunto )
print( 'H' in conjunto )
print( 'B' in conjunto )

l = [1,1,2,2,3,3]
print( l ) # Lista con elementos duplicados
c = set(l) # Convertimos la lista a conjunto, elimina las duplicidades
print( c )
l = list( c )
print( l )

# Diccionarios
colores = {'amarillo':'yellow', 'azul':'blue','rojo':'red','rosa':'white'}
print( colores )
print( colores['rojo'] )
print( colores['amarillo'] )
colores['rosa'] = 'pink'
print( colores )
del( colores['amarillo'] )
print( colores )

numeros = {10:'diez', 20:'veinte'}
print( numeros[10] )
print( numeros[20] )

for clave, valor in colores.items():
    print( clave, valor )


# Pilas
pila = [1,2,3,4]
pila.append(5) # Last in
pila.append(6) # append() adds at the end

print( pila )

pila.pop() # First out
pila.pop() # pop() removes last element and returns it
pila.pop()

print( pila )

# Colas
cola = deque(['Eduardo', 'Alejandro','Marisela'])
print( cola )

cola.append('Maria') # First in
cola.append('Miguel') # append() adds at the end

print( cola )

cola.popleft() # First out
cola.popleft() # popleft() removes first element and returns it

print( cola )