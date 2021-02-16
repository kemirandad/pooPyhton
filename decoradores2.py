def decorar(func):
    print('Hola mundo')
    func()
    
    def nueva_funcion(nombre):
        print(f'Hola ! {nombre} bienvenido a este nuevo curso') 
    
    print('Se terminó de ejecutar la función...')
    return nueva_funcion('Kenny')

@decorar
def despedir():
    print('Hasta luego !')
