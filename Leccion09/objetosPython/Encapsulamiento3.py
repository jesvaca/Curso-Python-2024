'''
    Los métodos "getter" (obtener) y "setter" (establecer) son una forma común
    de implementar este encapsulamiento, especialmente cuando se necesita un mayor
    control sobre el acceso y la modificación de los atributos de un objeto.

    ¿Qué son los métodos getter y setter?

    Getter: Un método getter se utiliza para obtener el valor de un atributo privado.
            Permite acceder al valor del atributo desde fuera de la clase, pero sin
            permitir la modificación directa.

    Setter: Un método setter se utiliza para establecer o modificar el valor de
            un atributo privado. Permite controlar cómo se modifica el atributo,
            incluyendo validaciones o transformaciones del valor.

    ¿Por qué usar getters y setters?

    Control del acceso: Permiten controlar el acceso a los atributos de una clase,
                        previniendo modificaciones no deseadas o inconsistencias.
    Validación de datos: Permiten validar los datos antes de ser asignados a un
                        atributo, asegurando la integridad de los datos del objeto.
    Abstracción: Ocultan la implementación interna de la clase, permitiendo modificarla
                 sin afectar el código que la utiliza.
    Encapsulamiento: Son una parte fundamental del encapsulamiento, proporcionando una
                interfaz controlada para interactuar con los atributos de un objeto.

'''
class Persona:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre       # Encapsulamiento del atributo tipo PROTEGIDO
        self._apellido = apellido
        self._edad = edad

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    @property           # Método GET para obtener el atributo PROTEGIDO
    def nombre(self):
        return self._nombre

    @nombre.setter      # Método SET para asignar el valor el atributo PROTEGIDO
    def nombre(self, nombre):
        self._nombre = nombre

    @property           # Método GET para obtener el atributo PROTEGIDO
    def apellido(self):
        return self._apellido

    @nombre.setter      # Método SET para asignar el valor el atributo PROTEGIDO
    def apellido(self, apellido):
        self._apellido = apellido

    @property           # Método GET para obtener el atributo PROTEGIDO
    def edad(self):
         return self._edad

    @nombre.setter      # Método SET para asignar el valor el atributo PROTEGIDO
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    persona1.mostrar_detalle()
    persona1.nombre = 'Jesus'
    persona1.apellido = 'Vaca'
    persona1.edad = 56
    persona1.mostrar_detalle()
    print(__name__)

