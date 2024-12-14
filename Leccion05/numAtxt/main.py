num = int(input('Proporciona un valor entre 1-3: '))
numTxt = ''
if num == 1:
    numTxt = 'Número uno'
elif num == 2:
    numTxt = 'Número dos'
elif num == 3:
    numTxt = 'Número tres'
else:
    numTxt = 'Valor fuera de rango'

print(f'Número proporcionado: {num} - {numTxt}')