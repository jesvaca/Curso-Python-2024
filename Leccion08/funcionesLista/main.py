'''
    FUNCIONES CON ARGUMENTOS LISTAS.
'''

def desplegar_Nombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Karla','Juan', 'Guillermo']
desplegar_Nombres(nombres)

# Puede enviar una lista
desplegar_Nombres([10,20,30])  # En el caso de lista numerica, encerrar entre corchetes los valores LISTA
desplegar_Nombres((5,15)) # En el caso de TUPLAS númericas, encerrar entre parentisis los valores LISTA