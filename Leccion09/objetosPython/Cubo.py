class Cubo:
    '''
        Coercion POO. VOLUMEN DE UN CUBO.
        Calcular el VOLUMEN de un cub0 usando POO.
        Volumen = Ancho x Profundidad x Altura
    '''
    def __init__(self, ancho, profundidad, altura):
        self.ancho = ancho
        self.profundida = profundidad
        self.altura = altura

    def calcula_volumen(self):
        return self.ancho * self.profundida * self.altura

# Inicio de progrmama

ancho = int(input('Proporciona el ancho del cubo: '))
profundidad = int(input('Proporciona la profundida: '))
altura = int(input('Proporciona la altura: '))
cubo1 = Cubo(ancho, profundidad, altura)

print(f'El volúmen del cubo: {cubo1.calcula_volumen()}')