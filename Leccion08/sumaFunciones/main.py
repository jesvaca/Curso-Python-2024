'''
    PRACTICA: crear una función para sumar los valores recibidos de tipo númerico
    utilizando argumentos variables *args como parámetro de la función
    y regresar como resultado la suma de los valores pasados como argumentos
'''

def sumatoria(*arg):
    # la palabra reservada pass permite dejar si desarrollar la función
    resultado = 0
    for valor in arg:
        resultado += valor
    return resultado

sum = sumatoria(1,2,3,4,5)
print(f'Sumatoria: {sum}')

sum = sumatoria(10, 40, 100, 150)
print(f'Sumatoria: {sum}')