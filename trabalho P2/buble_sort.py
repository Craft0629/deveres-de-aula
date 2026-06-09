import random
import time

lista_teste = []

for i in range(100000):
    lista_teste.append(random.randint(1, 100000))


def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def teste(nome, funcao):

    copia = lista_teste.copy()

    inicio = time.time()

    funcao(copia)

    fim = time.time()

    print(nome)
    print("Tempo:", fim - inicio)
    print()

teste("Bubble Sort", bubble_sort)