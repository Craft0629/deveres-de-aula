import random
import time

lista_teste = []

for i in range(100000):
    lista_teste.append(random.randint(1, 100000))



def heapify(lista, n, i):

    maior = i

    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:

        lista[i], lista[maior] = lista[maior], lista[i]

        heapify(lista, n, maior)


def heap_sort(lista):

    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):

        lista[i], lista[0] = lista[0], lista[i]

        heapify(lista, i, 0)

    return lista

def teste(nome, funcao):

    copia = lista_teste.copy()

    inicio = time.time()

    funcao(copia)

    fim = time.time()

    print(nome)
    print("Tempo:", fim - inicio)
    print()

teste("Heap Sort", heap_sort)

