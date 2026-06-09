import random
import time

lista_teste = []

for i in range(100000):
    lista_teste.append(random.randint(1, 100000))



def counting_radix(lista, exp):

    n = len(lista)

    saida = [0] * n

    contagem = [0] * 10

    for i in lista:
        indice = (i // exp) % 10
        contagem[indice] += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    for i in range(n - 1, -1, -1):

        indice = (lista[i] // exp) % 10

        saida[contagem[indice] - 1] = lista[i]

        contagem[indice] -= 1

    for i in range(n):
        lista[i] = saida[i]


def radix_sort(lista):

    maior = max(lista)

    exp = 1

    while maior // exp > 0:

        counting_radix(lista, exp)

        exp *= 10

    return lista


def teste(nome, funcao):

    copia = lista_teste.copy()

    inicio = time.time()

    funcao(copia)

    fim = time.time()

    print(nome)
    print("Tempo:", fim - inicio)
    print()



teste("Radix Sort", radix_sort)