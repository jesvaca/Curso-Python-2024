'''
    Listas de datos (vectores/arreglos en Python

'''

nombres = ['Elsa', 'Alex', 'Maya', 'Rex', 'Jesus']
# Imprimir la lista de nombre
print(nombres)
# Acceder a la lista individualmente
print(nombres[0])
print(nombres[1])
print(nombres[2])

print('Acceder a la lista de manera inversa')
print(nombres[-1])
print(nombres[-2])

print('Acceder a la lista en rango')
print(nombres[0:2])

print('Imprimir la lista del inicio al indice (sin incluirlo')
print(nombres[:3])

print('Imprimir la lista del indice indicado al final')
print(nombres[2:])

# Reemplazar el valor de una celda
nombres[3] = 'Lula'
print(nombres)

# Iterar la lista con for
for nom in nombres:
    print(nom)
else:
    print(f'Es toda la lista, total de elementos {len(nombres)}')

print('Agregar un elemento a la lista')
nombres.append('Jesús')
print(nombres)
print(' ')
print('Agregar un elemento en un indice a la lista')
nombres.insert(2,'Romario')
print(nombres)

print(' ')
print('Eliminar un valor ')
nombres.remove('Lula')
print(nombres)

print(' ')
print('Eliminar el último valor a la lista')
nombres.pop()
print(nombres)

print(' ')
print('Eliminar por indice')
del nombres[0]
print(nombres)

print(' ')
print('Eliminar todo el contenido de la lista')
nombres.clear()
print(nombres)

print(' ')
print('Eliminar la lista')
del nombres
print(nombres)