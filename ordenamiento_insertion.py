import random

def ordenamiento_de_insercion(lista):
    n = len(lista)
    
    for i in range(0, n - 1):
        contador = i
        while contador < n:
            if  lista[i] > lista [contador]:
                lista[i], lista[contador] = lista[contador], lista[i]
                contador = i
            contador += 1
    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_insercion(lista)
    print(lista_ordenada)