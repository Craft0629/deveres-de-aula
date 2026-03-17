def indice_insercao(lista, alvo):
    inicio, fim = 0, len(lista)

    while inicio < fim:
        meio = (inicio + fim) // 2

        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio

    return inicio

lista = [1,3,5,7]

print(indice_insercao(lista,4))