def busca_sequencial(lista, alvo):
    lista = [4, 7, 1, 9, 3]

    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


lista = [4, 7, 1, 9, 3]

print(busca_sequencial(lista, 9))
print(busca_sequencial(lista, 5))