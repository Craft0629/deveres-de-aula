import random
import time

lista_teste = []

for i in range(100000):
    lista_teste.append(random.randint(1, 100000))


def insertion_sort(lista):

    for i in range(1, len(lista)):

        chave = lista[i]
        j = i - 1

        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

def teste(nome, funcao):

    copia = lista_teste.copy()

    inicio = time.time()

    funcao(copia)

    fim = time.time()

    print(nome)
    print("Tempo:", fim - inicio)
    print()


teste("Insertion Sort", insertion_sort)