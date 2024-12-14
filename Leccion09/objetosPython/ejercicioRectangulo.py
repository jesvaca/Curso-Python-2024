class Rectangulo:
    '''
        Coercion POO. TRIANGULO.
        Calcular el AREA de rectangulo usando POO.
        Area = Base x Altura
    '''
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Inicio de progrmama

base = int(input('Proporciona la base: '))
altura = int(input('Proporcina la altura: '))
rectangulo1 = Rectangulo(base, altura)

print(f'El área del rectangulo: {rectangulo1.calcular_area()}')

