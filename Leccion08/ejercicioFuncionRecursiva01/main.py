'''
    EJERCICIO: imprimir números de 5 a 1 de manera descendente usando funciones recursivas.
    Puede ser cualquier valor positivo, ejm, si pasamos 5, debe imprimir:
    5,4,3,2,1
    En caso de pasar el valor de 3, debe imprimir:
    3,2,1
    Si se pasan valores negativos, ni imprime nada
'''

def numeros_Descendentes(numero):
    if numero >= 1:
        print(numero)
        return numeros_Descendentes(numero - 1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Número menor de 1...')



numeros_Descendentes(-1)