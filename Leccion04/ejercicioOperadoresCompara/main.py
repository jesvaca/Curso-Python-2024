# Ejercicio para determinar un número es par/impar

a = int(input('Introduce un número: '))

# El operador % MOD/Residuo para comparar con cero si es par/impar
if a % 2 == 0:
    print(f'El número {a} es par...')
else:
    print(f'El número {a} es impar...')