"""
     ENCAPSULAMIENTO se refiere a la práctica de ocultar los detalles internos
     de un objeto y exponer solo una interfaz pública para interactuar con él

     Objetivos del encapsulamiento:
        * Ocultamiento de la información: Protege los datos internos del objeto de modificaciones externas no deseadas.
        * Control de acceso: Define cómo se pueden acceder y modificar los datos del objeto.
        * Modularidad: Facilita la organización del código en unidades lógicas independientes.
        * Mantenibilidad: Simplifica la modificación y el mantenimiento del código al aislar los efectos de los cambios.

    Convención de nombres para indicar el nivel de acceso a los atributos y métodos de una clase:
        * Atributos/métodos públicos: Se nombran de forma normal (ej., nombre, calcular_edad).
          Se puede acceder a ellos desde cualquier parte.
        * Atributos/métodos protegidos: Se preceden con un guión bajo (ej., _nombre, _calcular_edad).
          Por convención, se indica que no deben ser accedidos directamente desde fuera de la clase o sus subclases, aunque Python no lo impide.
        * Atributos/métodos privados: Se preceden con dos guiones bajos (ej., __nombre, __calcular_edad).
          Python aplica un "name mangling" (cambio de nombre) que dificulta el acceso directo desde fuera de la clase.
"""
class Persona:
    # Se inicializa la instancia de clase
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre       # Atributo protegido
        self.__apellido = apellido  # Atributo privado
        self.edad = edad

    def _muestra_apellido(self):    # Método protegido que regresa el valor de un objeto privado
        return self.__apellido

    def mostrar_detalle(self):
        print(f'Objeto Persona2 {self._nombre} {self._muestra_apellido()} {self.edad}')     # Se realiza el llamado al método _muestra_apellido para el atributo PRIVADO


persona1 = Persona('Jesús', 'Vaca', 56)    # Se crea el objeto con la instancia
# print(f'Objeto Persona2 {persona1._nombre} {persona1.apellido} {persona1.edad})

persona1.mostrar_detalle()      # Mostramos los datos usando el método de la clase Persona2

