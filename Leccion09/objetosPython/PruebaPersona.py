from Encapsulamiento3 import Persona

print('Creación de objetos'.title() .center(50,'-'))
persona1 = Persona('Elsa','Chávez', 52)
persona1.mostrar_detalle()
print(__name__)

print('Destrucción de objetos'.title() .center(50,'-'))
del persona1