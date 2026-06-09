import random
import time


lista_teste = []

for i in range(100000):
    lista_teste.append(random.randint(1, 100000))

def bucket_sort(lista):

    quantidade = 10

    buckets = []

    for i in range(quantidade):
        buckets.append([])

    maior = max(lista)

    for numero in lista:

        indice = numero * quantidade // (maior + 1)

        buckets[indice].append(numero)

    resultado = []

    for bucket in buckets:

        bucket.sort()

        resultado.extend(bucket)

    return resultado

def teste(nome, funcao):

    copia = lista_teste.copy()

    inicio = time.time()

    funcao(copia)

    fim = time.time()

    print(nome)
    print("Tempo:", fim - inicio)
    print()


teste("Bucket Sort", bucket_sort)