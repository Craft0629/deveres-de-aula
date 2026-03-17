def contar_menores(lista, alvo):
    inicio, fim = 0, len(lista)

    while inicio < fim:
        meio = (inicio + fim) // 2

        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio

    return inicio

lista = [1,3,5,7,9]

print(contar_menores(lista,6))