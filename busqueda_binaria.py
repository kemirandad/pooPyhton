import random

contador = 0
contador2 = 0

def busqueda_binaria(lista, comienzo, final, objetivo):
    
    contar()
    
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2
    
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

def busqueda_lineal(lista, objetivo):
    
    match = False

    for elemento in lista:  # O(n)
        contar2()
        if elemento == objetivo:
            
            match = True
            break

    return match


def contar():
    global contador 
    contador += 1
    return contador

def contar2():
    global contador2 
    contador2 += 1
    return contador2

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))
    
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    
    encontrado1 = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    
    print(f'Se han hecho {contar() - 1} busquedas de tipo binario')
    
    print()
    print(f'Se han hecho {contar2() - 1} busquedas de tipo lineal')