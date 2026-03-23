lista=[2,4,6,8,10,20]
def soma_lista(lista):

    if len(lista) == 0:
        return 0

    return lista[0] + soma_lista(lista[1:])

print(soma_lista(lista))
