# Ingresar dos numeros, crear menu y mostrar resultados acorde al menu
n1 = float( input('Ingrese el primer numero: ') )
n2 = float( input('Ingrese el segundo numero: ') )

while True:
    option = input("""Ingrese una opcion
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Salir
    """)

    if option == '1':
        print('La suma es:', n1+n2)
    elif option == '2':
        print('La resta es:', n1-n2)
    elif option == '3':
        print('La multiplicacion es:', n1*n2)
    elif option == '4':
        print('Saliendo...')
        break
    else:
        print('Comando no valido')

# Pedirle al usuario un numero impar, repetir el proceso hasta que lo haga

while float( input("""Ingresa un numero impar: """) ) % 2 == 0:
    print('Numero incorrecto')

# Sumar todos los numeros enteros pares entre el 0 y 100
# primer forma
suma = sum( range(0, 101, 2) )
print( "El resultado de la sumatoria 1", suma )
# segunda forma
suma2 = 0
for i in range(0,101,2):
    suma2 += i
print( "El resultado de la sumatoria 2", suma2 )

# Pedir al usuario cuantos numeros quiere introducir, pedirselos y calcular media

amount = int( input('Cuantos numeros deseas introducir? ') )
total = 0
for i in range(0, amount):
    total += int( input('Ingresa el numero: ') )
print( 'La media es: ', total/amount)

# Pedirle al usuario un numero entre 0 y 9, comprobar que sea correcto y de serlo, verificar si el numero esta en la lista o no

lista = [1, 3, 6, 9]

while True:
    num = int( input('Ingresa un numero del 0 al 9: ') )
    if num >= 0 and num <= 9:
        break
if num in lista:
    print( 'El numero', num, 'se encuentra en la lista')
else:
    print( 'El numero', num, 'no se encuentra en la lista' )

# Usando la funcion range

print( list( range( 11 ) ) ) # todos los numeros del 0 al 10
print( list( range( -10, 1 ) ) ) # todos los numeros del -10 al 0
print( list( range( 0, 21, 2) ) ) # todos los numeros pares del 0 al 20
print( list( range( -19, 0, 2) ) ) # todos los numeros impares entre -20 y 0
print( list( range( 0, 51, 5 ) ) ) # todos los numeros multiples de 5 del 0 al 50


lista1 = ['h','o','l','a',' ','m','u','n','d','o']
lista2 = ['h','o','l','a',' ','l','u','n','a']

lista3 = []

for letra in lista1:
    if letra in lista2 and letra not in lista3:
        lista3.append(letra)

print(lista3)