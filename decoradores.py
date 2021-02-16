def presentarse(nombre):
    return f"Me llamo {nombre}"


def estudiemos_juntos(nombre):
    return f"¡Hey {nombre}, aprendamos Python!"


def consume_funciones(funcion_entrante):
    return funcion_entrante("Kenny")

# Otro codigo distinto


def decorador(func):  # A, #B

    def nueva_funcion():
        print("Ejecutando la funcion")
        # Aqui es donde se agrega la logica que va a ser añadida a la funcion
    func()
    print("Se ejecuto la funcion")

    return nueva_funcion  # C

@decorador  # Aqui es donde se le agrega la decoracion, la funcion que queramos
def saluda():  # C
    print("Hola mundo")

if __name__ == '__main__':
    #Primera parte de codigo
    """
    print(consume_funciones(presentarse))
    print(consume_funciones(estudiemos_juntos))
    """
    #Segunda parte de codigo
    saluda()
