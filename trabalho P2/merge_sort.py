import random
import time


lista_teste = []

for i in range(100000):
    lista_teste.append(random.randint(1, 100000))


def merge_sort(lista):

    if len(lista) > 1:

        meio = len(lista) // 2

        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):

            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1

            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    return lista


def teste(nome, funcao):

    copia = lista_teste.copy()

    inicio = time.time()

    funcao(copia)

    fim = time.time()

    print(nome)
    print("Tempo:", fim - inicio)
    print()


teste("Merge Sort", merge_sort)