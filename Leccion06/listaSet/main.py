'''
    Listas SET. Permiten crear listas de datos de cualquier tipo que no pueden ser modificadas
    Operaciones: agregar elementos, eliminar la lista, etc.
'''
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)

# Longitud de la lista SET
print(f'Longitud del set {len(planetas)}')

# Revisar si un elemento está presente en set
print('Marte' in planetas)
# Error si no está el elemento en la lista
print('Martes' in planetas)

# Agregar un elemento a la lista
planetas.add('Tierra')
print(planetas)

# Eliminar un elemento de la lista SET (arroja error en caso de no estar en la lista)
planetas.remove('Júpiter')
print(planetas)

# Otro metodo para eliminar un elemento de la lista set (no arroja error en caso de no estar en la lista
planetas.discard('Venus')

# Eliminar (limpiar) la lista set
planetas.clear()
print(planetas)

# Eliminar el set completo
planetas.remove()
print(planetas)