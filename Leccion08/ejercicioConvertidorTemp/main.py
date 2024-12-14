'''
    Ejercicio: Convertidor de Temperatura
    Realizar dos funciones para convertir de grados Celsius a Faherenheit
'''

# Función que convierte grados Celsius a Faherenheit
def celsius_fahren(grados):
    conversion = ((grados * 9)/5)+32
    print(f'{grados}c grados Celsius => equivalen {conversion: 0.2f}f grados Fahrenheit')
    return
# Función que convierte grados Faherenheit a Celsius
def fahren_celsius(grados):
    conversion = ((grados - 32)*5)/9
    print(f'{grados}f grados Fahrenheit => equivalen {conversion: 0.2f}c en Celsius')
    return
# Función para preguntar a usuario si desea continuar
def continuar_conversiones():
    continua = input('¿Desea otra conversión? [S/N]: ')
    if continuar == 'S' or continuar == 's':
        os.system('cls')
        return continua
    else:
        exit()

# Importamos libreria sistema operativo
import os

# *********** Inicia cuerpo principal del programa **************
continuar = 'S'
tipoConversion = ''
os.system('cls')
while continuar == 'S' or continuar == 's':
    grados = int(input('Introduzca los grados que desea convertir: '))
    print('____________________ Qué conversión desea?:')
    print('Escriba C para Celsius')
    print('Escriba F para Fahrenheit')
    tipoConversion = input('Capture su elección: ')
    if tipoConversion == 'C' or tipoConversion == 'c':
        fahren_celsius(grados)
        continuar = continuar_conversiones()
    elif tipoConversion == 'F' or tipoConversion == 'f':
        celsius_fahren(grados)
        continuar = continuar_conversiones()
    else:
        continuar = input('Opción incorrecta, ¿desea continuar? [S/N]: ')
        if continuar == 'C' or continuar == 'c':
            os.system('cls')
            continue
        else:
            break

