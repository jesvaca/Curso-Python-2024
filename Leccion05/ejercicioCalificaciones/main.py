'''
    Ejercicio para sentencias if-eleif-else
    Captura de calificaciones y emisión de la boleta
    Se captura un valor entre 0-10
    Si está entre 9 y 10: imprimir
'''

calificacion = int(input('Proporciona tu calificación (valor entre 0-10): '))
boleta = None

if 9 <= calificacion <= 10:
    boleta = 'A'
elif 8 <= calificacion < 9:
    boleta = 'B'
elif 7 <= calificacion < 8:
    boleta = 'C'
elif 6 <= calificacion < 7:
    boleta = 'D'
elif 0 <= calificacion < 6:
    boleta = 'C'
else:
    boleta = 'Incorrecta'

print(f'La calificación capturada fue {calificacion} y tu boleta es {boleta}')