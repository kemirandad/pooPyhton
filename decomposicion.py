class Automovil():
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = color
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros = 4)
        
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyectar_gasolina(10)
        else:
            self._motor.inyectar_gasolina(3)
            
        self._estado = 'en movimiento'
        
        
class Motor():
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._tempertatura = 0
    
    def inyectar_gasolina(self, cantidad):
        pass
    
class Asientos():
    def __init__(self, cantidad, material, tipo='estandar'):
        self.cantidad = cantidad
        self.material = material
        self.tipo = tipo
        self._grabados = False
    
    def es_familiar(self, tipo_vehiculo):
        if tipo_vehiculo == 'familiar':
            self._grabados = False
        else:
            self._grabados = True
        