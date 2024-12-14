'''
    La herencia en Python es un concepto fundamental de la Programación Orientada
    a Objetos (POO) que permite crear nuevas clases basadas en clases existentes.
    La clase original se denomina "clase padre" o "superclase", mientras que la
    nueva clase se llama "clase hija" o "subclase". La herencia posibilita que la
    clase hija herede los atributos (variables) y métodos (funciones) de la clase
    padre, lo que fomenta la reutilización de código y la organización jerárquica
    de las clases.
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

'''
    El método super() en Python es una función incorporada que se utiliza principalmente 
    en el contexto de la herencia de clases, dentro de la programación orientada a objetos (POO). 
    Su principal función es permitirte acceder a métodos de la clase padre (o superclase) desde 
    una clase hija (o subclase). Esto es esencial para reutilizar código, extender la funcionalidad 
    de las clases padre y manejar correctamente la herencia múltiple.
'''
class Empleado(Persona):                        # La clase Empleado hereda todos los atributos de la clase padre PERSONA
    def __init__(self, nombre, edad, sueldo):   # Se inicia la clase Empleado
        super().__init__(nombre, edad)          # super() permite acceder a métodos de la clase padre Persona
        self.sueldo = sueldo

empleado1 = Empleado('Jesus', 56, 19000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)