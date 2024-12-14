'''
    Ejercicio de sentencias de control con IF-ELSIF-ELSE
    Captura por el usuario su edad, desplegar mensaje por condicionales:
    0-10:   La infancia es increible
    10-20:  Muchos cambios y mucho estudio
    20-30:  Amor y comienza trabajo
    Cualquier otro valor: etapa de vida no reconocida
'''
edad = int(input('Propociona tu edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increible'
elif edad >= 10 and edad < 20:
    mensaje = 'Muchos cambios y mucho estudio'
elif 20 <= edad <= 30:
    mensaje = 'Amor y comienza trabajo'
else:
    mensaje = 'Etapa de vida no reconocida'

print(mensaje)