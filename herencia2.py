import math

class Circunferencia():
    
    def __init__(self, radio):
        self.__radio = radio
    
    @property
    def get_radio(self):
        return self.__radio
    
    @get_radio.setter
    def set_radio(self, radio):
        if radio >= 0:
            self.__radio = radio
        else:
            print('El radio debe ser un número positivo')
    
    def calcular_area(self):
        return math.pi *  self.get_radio ** 2
    

class Esfera(Circunferencia):
    def __init__(self, radio):
        super().__init__(radio)
    
    def calcular_area(self):
        return 4 * math.pi * self.get_radio ** 2

if __name__ == '__main__':
    fig1 = Circunferencia(radio=5)
    print(fig1.calcular_area())
    fig1.__radio = 20
    print(fig1.get_radio)
    fig1.set_radio = -5 
    print(fig1.get_radio)
    fig1.set_radio = 10
    print(fig1.get_radio)
    
    fig2 = Esfera(radio=5)
    print(fig2.calcular_area())