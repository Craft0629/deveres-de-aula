import random
import time

lista_teste = []

for i in range(100000):
    lista_teste.append(random.randint(1, 100000))


def counting_sort(lista):

    maior = max(lista)

    contagem = [0] * (maior + 1)

    for numero in lista:
        contagem[numero] += 1

    resultado = []

    for i in range(len(contagem)):
        resultado.extend([i] * contagem[i])

    return resultado

def teste(nome, funcao):

    copia = lista_teste.copy()

    inicio = time.time()

    funcao(copia)

    fim = time.time()

    print(nome)
    print("Tempo:", fim - inicio)
    print()


teste("Counting Sort", counting_sort)