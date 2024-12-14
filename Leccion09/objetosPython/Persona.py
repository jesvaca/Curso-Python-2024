class Persona1:
    # Se inicializa la instancia de clase
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = '28'

class Persona2:
    # Se inicializa la instancia de clase
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Objeto Persona2 {self.nombre} {self.apellido} {self.edad}')

print(type(Persona1))

persona1 = Persona1()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona2('Jesús', 'Vaca', 56)    # Se crea el objeto con la instancia
                                                                 # de clase Persona2
print(f'Objeto Persona2 {persona2.nombre} {persona2.apellido} {persona2.edad}')

persona2.mostrar_detalle()      # Mostramos los datos usando el método de la clase Persona2

# Se crea otro objeto con la instancia de la clase Persona2
persona2a = Persona2('Elsa', 'Chávez', 53)
# Desplegamos con el método de la clase pero usando otra notación
Persona2.mostrar_detalle(persona2a)

# AGREGAR ATRIBUTOS/CAMPOS AL VUELO A UN OBJETO EN PARTICULAR
persona2a.telefono ='1234567890'
print(persona2a.telefono)
persona2a.mostrar_detalle()

