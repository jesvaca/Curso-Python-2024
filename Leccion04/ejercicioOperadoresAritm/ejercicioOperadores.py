""""
Ejercicio de calculo de area y el perimetro de un Rectangulo:

Area: alto * ancho
Perimetro: (alto+ancho)*2
"""
alto = int(input("Proporciona el alto del rectangulo:"))
ancho = int(input('Proporciona el ancho del rectangulo:'))
area = alto * ancho
perimetro = (alto+ancho)*2
print(f'Area: {area} ')
print(f'Perimetro: {perimetro}')


print('REASIGNACION DE VARIABLES')

miVariable = 10
miVariable = miVariable + 1
print(miVariable)
# esto es igual a la asignación anterior
miVariable += 1
print(miVariable)

miVariable *= 3
print(miVariable)
