'''
    Ejercicio listas con rangos
    Sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)

    # Ejercicio 1. Iterar un rango de o a 10 e imprimir números divibles entre 3
    # Ejercicio 2. Crear rango de números de 2 a 6, e imprimirlos
    # Ejercicio 3. Crear rango de 3 a 10 pero con incremento de 2 en 2
'''

# Ejercicio 1.
print('Rango de 9 a 10 imprime Números divisibles entre 3: ')
for i in  range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2.
numeros = range(2,7)
print(f'La lista de números {numeros}')
print('Números 2 a 6: ')
for i in  numeros:
    print(i)

# Ejercicio 3.
numeros = range(3,11,2)
print('Rango con valores de inicio = 3, fin = 10, incremento =2')
for i in numeros:
    print(i)

