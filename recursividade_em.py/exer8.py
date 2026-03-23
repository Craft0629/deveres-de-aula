lista=[2,6,2,5,2,8,2]
def contador(lista, numero):

    if len(lista) == 0:
        return 0

    if lista[0] == numero:
        soma = 1
    else:
        soma = 0

    return soma + contador(lista[1:], numero)

numero=2
print(contador(lista,numero))
    