'''
    Las funciones son bloques de código que pueden llamarse indefinidamente
    Deben declararse y desarrollarse en la parte superior, antes de ser llamadas
'''

def mi_funcion():
    print('Saludos desde mi función...')

def mi_funcion_arg(nombre, apellido):
    print(f'Saludos {nombre} {apellido} ...')

def sumar(a,b):
    return a+b

def suma2(a:int = 0, b:int = 0)->int:        # Los parametros iniciados ayudan a evitar error cuando no se mandan de llamada
    return a+b                               # formas de tipear los datos que ingresan y se retornan

# Funcion dinamica: con varios parametros con tipo de tupla
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
'''
************************************************************************************
'''
# Inicio del programa convencional
# Llamamos a la función

mi_funcion()
mi_funcion_arg('Jesús', 'Vaca')
resultado = sumar(5,4)
print(f'Resultado sumar:{resultado}')
print(f'Resultado sumar:{sumar(1,2)}')
print(f'Resultado sumar:{suma2()}') # Se inicializa los parametros en la función para evitar error

# Funcion con argumentos dinamicos
def listarNombres(*nombres):    # Se una el * para recibir varios argumentos en la función
    for nombre in nombres:
        print(nombre)

# Argumentos variables en funciones
listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')
listarNombres('Alex', 'Elsa')
