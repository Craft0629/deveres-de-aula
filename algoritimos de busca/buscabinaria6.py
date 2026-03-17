def valor_mais_proximo(lista, alvo):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    if inicio >= len(lista):
        return fim
    if fim < 0:
        return inicio

    if abs(lista[inicio] - alvo) < abs(lista[fim] - alvo):
        return inicio
    else:
        return fim
    
lista = [10,20,30,40]

print(valor_mais_proximo(lista,26))