def busca_sequencial_ordenada(lista, alvo):
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1

lista = [1,2,3,4,5,6]

print(busca_sequencial_ordenada(lista,4))