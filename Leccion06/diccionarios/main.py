'''
    DICCIONARIOS. Colección de datos de un tipo con una llave de id y su contenido
    dict(key, value)
'''
from typing import Dict

miDiccionario = {
    'IDE': 'Integrated Develpment Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(miDiccionario)

# Recupera un elemento escribiendo la key
print(miDiccionario['IDE'])
# Otra forma de recuperar valores
print(f'Valor recuperado con método get: {miDiccionario.get('OOP')}')

# Longitud de un diccionario
print(f'El número de elementos del diccionario es {len(miDiccionario)}')

# Modificar elemento del diccionario
miDiccionario['OOP'] = 'Programación Orientada a Objetos'
print(miDiccionario['OOP'])

# Recorrer el diccionario con for para las llaves
for valorDiccionario in miDiccionario:
    print(valorDiccionario)

# Recorrer el diccionario con for para las llaves
print('Recorriendo el diccionario con for para las llaves - valores:')
for keyDiccionario, valorDiccionario in miDiccionario.items():
    print(keyDiccionario, '***', valorDiccionario)

# Recorrer el diccionario con for para las llaves con metodo keys()
print('Recorriendo el diccionario con for para las llaves con método keys():')
for keysDiccionario in miDiccionario.keys():
    print(keysDiccionario)

# Recorrer el diccionario con for para las valores con metodo values()
print('Recorriendo el diccionario con for para los valores con método values():')
for valuesDiccionario in miDiccionario.values():
    print(valuesDiccionario)

# Comprobar si existe un valor en el diccionario
print('OOP' in miDiccionario)

# Agregar un elemento al diccionario
miDiccionario['PST'] = 'Programación Estructurada'
print('Agragamos elemento: ', miDiccionario)

# Eliminar elemento
miDiccionario.pop('OOP')
print('Eliminamos elemento con pop(): ', miDiccionario)

# Eliminar el contenido del diccionario
miDiccionario.clear()
print('Eliminamos todo el contenido del diccionario: ', miDiccionario)

# Eliminar la variable del diccionario
del miDiccionario
print(miDiccionario)