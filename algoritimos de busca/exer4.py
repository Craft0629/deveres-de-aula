def buscar_nome(lista, alvo):
    alvo = alvo.lower()

    for i, nome in enumerate(lista):
        if nome.lower() == alvo:
            return i

    return -1

nomes = ["Ana","Carlos","Bruno","Maria"]

print(buscar_nome(nomes,"maria"))
print(buscar_nome(nomes,"ANA"))