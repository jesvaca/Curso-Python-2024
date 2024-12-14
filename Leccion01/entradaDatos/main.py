# Función input para procesar la entrada del usuario
from copyreg import pickle

resultado = input("Escribe un dato: ")
print(resultado)
print("Fin del programa...")

print("Suma de dos números capturados")
num1 = input("Introduce el primer número: ")
num2 = input("Introduce el seegundo número: ")
# Uso con int en input
# num1 = int(input(num1))
numerosCadena = num1 + num2
print("Concatenación de números capturados. ", num1 + num2)

print("...convertimos:")
num1 = int(num1)
num2 = int(num2)
print("Números a int: ", num1+num2)