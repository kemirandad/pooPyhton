class Auto():
    def __init__(self, modelo, anio):
        self.__modelo = modelo
        self.__anio = anio
        self.__precio = 0
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def anio(self):
        return self.__anio
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        if precio > 2000:
            self.__precio = precio
        else:
            raise ValueError(f'No tenemos ningún auto de {precio} dolares')
        

auto1 = Auto('Toyota', 2000)
print(auto1.precio)
auto1.precio = 2015
print(auto1.precio)
print(f'{auto1.modelo}, {auto1.anio}')
print('')
auto2 = Auto('Nissan', 2020)
print(auto2.precio)
auto2.precio = 2000
print(auto2.precio)