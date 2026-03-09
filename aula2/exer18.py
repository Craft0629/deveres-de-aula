import random
lista = [random.randint( 1,11) for _ in range(10)]
pares = [x for x in lista if x % 2 == 0]
pares_ordenados = sorted(pares)

print(lista)
print(pares_ordenados)