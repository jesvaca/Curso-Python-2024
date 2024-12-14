'''
    FUNCIONES CON DICCIONARIOS. Para recibir diccionarios con terminos, usamos doble asterisco
    en los argumentos recibidos en la función:
    def nom_fun(**args):
        ...

'''

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')

listarTerminos(IDE='Integated Developement Enviroment', PK='Primary Key')
listarTerminos(DBMS='Data Base Maganament System')