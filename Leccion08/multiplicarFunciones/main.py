'''
    EJERCICIO: Crear una función para multiplicar los valores recibidos de tipo númerico,
    utilizando argumentos variables *args como parametro de la función
    y regresar como resultado la multiplicación de todos los valores
'''

def multiplica_Valores(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

print(multiplica_Valores(2,5,8,10))

