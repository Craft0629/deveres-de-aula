def indice_menor(lista):
    if not lista:
        return -1

    menor_indice = 0

    for i in range(1, len(lista)):
        if lista[i] < lista[menor_indice]:
            menor_indice = i

    return menor_indice

lista = [9,4,7,1,3]

print(indice_menor(lista))