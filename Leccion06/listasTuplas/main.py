# Definir una tupla

frutas = ('Naranaja','Platano','Guayaba')
# Cuando es un solo elemento en la tupla, se debe agregar una coma al final:
# frutas = ('Naranja',)

# Funciones
# Saber la longitud
print(frutas)
print(len(frutas))

# Acceder a un elemento
print(frutas[0])

# Navegacion inversa
print(frutas[-1])

# Acceder a un rango
print(frutas[0:1]) # sin incluir el último

# Recorrer los elementos con for
for fruta in frutas:
    print(fruta)

# Para evitar el salto de línea
for fruta in frutas:
    print(fruta, end=' ** ')

# Cambiar una tupla: se copia la tupla a una lista, se modifica esa lista y con la función list() se
# regresa a la tupla. No es buena practica

frutasLista = list(frutas)
frutasLista[0] = 'Mandarina'
frutas = tuple(frutasLista)
print('\n',frutas)

# Eliminar una tupla...la variable completa
del frutas

