cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo')
numLetras = 0
for letra in 'prueba letras':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        numLetras += 1
print(f'Número de letras encontradas {numLetras}')

# Ciclo for con rango...
continua = input('...pulsa tecla para continuar...')

print('Imprime lista de números en rango:')
for i in range(6):
    print(f'Valor {i}')

continua = input('...pulsa tecla para continuar...')

print('Imprime lista de números pares en rango:')
for i in range(6):
    if i % 2 == 0:
        print(f'Valor {i}')

# Lo mismo pero con continue
print('Usando continue')
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor {i}')