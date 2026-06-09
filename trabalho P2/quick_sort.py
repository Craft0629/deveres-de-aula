import random
import time

lista_teste = []

for i in range(100000):
    lista_teste.append(random.randint(1, 100000))

def quick_sort(lista):

    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista)//2]

    menores = []
    iguais = []
    maiores = []

    for numero in lista:

        if numero < pivo:
            menores.append(numero)

        elif numero > pivo:
            maiores.append(numero)

        else:
            iguais.append(numero)

    return quick_sort(menores) + iguais + quick_sort(maiores)



def teste(nome, funcao):

    copia = lista_teste.copy()

    inicio = time.time()

    funcao(copia)

    fim = time.time()

    print(nome)
    print("Tempo:", fim - inicio)
    print()

teste("Quick Sort", quick_sort)