lista=[1,2,3]

def maior(lista):

    if len(lista) == 1:
        return lista[0]

    resto = maior(lista[1:])

    return max(lista[0], resto)

print(maior(lista))


