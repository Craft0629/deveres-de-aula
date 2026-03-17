def busca_rotacionada(lista, alvo):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        if lista[inicio] <= lista[meio]:
            if lista[inicio] <= alvo < lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
        else:
            if lista[meio] < alvo <= lista[fim]:
                inicio = meio + 1
            else:
                fim = meio - 1

    return -1

lista = [4,5,6,7,0,1,2]

print(busca_rotacionada(lista,0))