class Rectangulo: #Clase padres no hereda
    
    def __init__(self, base, altura): #se define el constructor con dos atributos
        # los atributos son de caracter publico
        self.base = base
        self.altura = altura

    def area(self): #metodo para calcular area de un rectangulo vinculado a la clase padre
        return self.base * self.altura

class Cuadrado(Rectangulo): # clase cuadrado hereda de rectangulo

    def __init__(self, lado): #se define el constructor con un atributo
        super().__init__(lado, lado)


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())