class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self.__edad = edad    # Atributo privado

    def mostrar_nombre(self):
        return self._nombre

    def _mostrar_edad(self): # MÉTODO PROTEGIDO, inicia con guion bajo en el nombre
      return self.__edad

    def mostrar_informacion(self):
      print(f"Nombre: {self._nombre}")
      print(f"Edad: {self._mostrar_edad()}")  # Está dentro de la clase y puede acceder siendo privado

persona = Persona("Juan", 30)
print(persona.mostrar_nombre()) # Acceso al atributo protegido mediante un metodo publico
persona.mostrar_informacion()
print(f'Acceso directo al atributo protegido (posible, pero no recomendado: {persona._nombre}')  # Acceso directo al atributo protegido (posible, pero no recomendado)
#print(persona.__edad) # Error: AttributeError: 'Persona' object has no attribute '__edad'
print({f'Acceso al atributo privado usando name mangling: {persona._Persona__edad}') # Acceso al atributo privado usando name mangling (no recomendado)