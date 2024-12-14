# Determinar si un valor esta en un rango de numeros

valor = int(input('Escribe un valor: '))
valorMinimo = 0
valorMaximo = 5

dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)

if dentroRango:
    print(f'El valor {valor} esta en el rango de 0 a 5...')
else:
    print(f'El valor {valor} esta FUERA de rango de 0 a 5...')