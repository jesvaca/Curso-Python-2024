'''
EJERCICIO DE TUPLA
Dada la lista de tupla, crear una lista que incluya los número menores a cinco
tupla = (13, 1, 8, 3, 2, 5, 8)
'''

numMenores5 = (13, 1, 8, 3, 2, 5, 8)
listaNumeros = []

for num in numMenores5:
    if num <= 5:
        listaNumeros.append(num)

print(listaNumeros)
        


