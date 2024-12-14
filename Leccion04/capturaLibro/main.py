'''
    Ejercicio de captura de datos de un libro
    16 de noviembre del 2024
    Curso Python
'''
print('Proporcione los siguientes datos del libro:')
nombreLibro = input('Nombre: ')
id = int(input('ID: '))
costo = float(input('Costo:'))
envio =  input('Envío gratuito (True/False): ')

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto, debe escribir True/False...'

# Desplegamos la informacion capturada
print(f'''
    Datos capturados:
    Nombre: {nombreLibro}
    ID:     {id}
    Precio: {costo}
    Envío:  {envio}
''')