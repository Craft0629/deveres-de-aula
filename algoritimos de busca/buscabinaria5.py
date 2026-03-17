def busca_binaria_strings(lista, alvo):
    alvo = alvo.lower()
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor = lista[meio].lower()

        if valor == alvo:
            return meio
        elif valor < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

nomes = ["Ana","Bruno","Carlos","Maria"]

print(busca_binaria_strings(nomes,"carlos"))