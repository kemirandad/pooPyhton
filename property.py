# Esto generará error
"""
class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

mi_clase = Clase("valor_atributo")
print(mi_clase.__Clase.__mi_atributo)
"""
# mi_clase.__mi_atributo # Error!

class CasillaDeVotacion:

    def __init__(self, identificador, pais): #constructor
        self._identificador = identificador # atributos necesarios para crear una instancia
        self._pais = pais # atributos necesarios para crear una instancia
        self._region = None # atributo que el usuario no debe conocer o manejar

    @property
    def region(self): # Funcion getter que captura e imprime el atributo región
        return self._region

    @region.setter
    def region(self, region): # función setter que modificar la región del objeto
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')


casilla = CasillaDeVotacion(123, ['Mexico', 'Morelos'])
print(casilla.region)
casilla.region = 'Cali'
print(casilla.region)
