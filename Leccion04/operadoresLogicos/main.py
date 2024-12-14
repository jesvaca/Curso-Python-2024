"""
Operadores Lógicos
and  Devuelve True si ambos operadores son True
or   Devuelve True si alguno de los operadores es True
not  Devuelve True si alguno de los operadores es False
"""

a = True
b = True
resultado = a and b
print(f'Variables a: {a} AND b: {b} ')
print(f'Resultado: {resultado}')

a = True
b = False
resultado = a and b
print(f'Variables a: {a} AND b: {b} ')
print(f'Resultado: {resultado}')

a = True
b = False
resultado = a or b
print(f'Variables a: {a} OR b: {b} ')
print(f'Resultado: {resultado}')


b = False
resultado = not b
print(f'Variables NOT b: {b} ')
print(f'Resultado: {resultado}')

b = True
resultado = not b
print(f'Variables NOT b: {b} ')
print(f'Resultado: {resultado}')