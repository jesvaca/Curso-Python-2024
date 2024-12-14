"""
Comparación de dos números para determinar cual es el mayo
"""
num1 = int(input('Introduce el primer número:'))
num2 = int(input('Introduce el segundo número:'))
if num1 > num2:
    print(f'El primer número {num1} es MAYOR que el número dos {num2}')
else:
    if num1 == num2:
        print(f'El primer número {num1} es IGUAL que el número dos {num2}')
    else:
        print(f'El segundo número {num2} es MAYOR que el primer número {num1}')
