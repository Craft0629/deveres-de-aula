pares = [x for x in range(1,51)]

contador = 0

for x in pares:
    if x % 2 == 0:
        contador += 1
print(f"os pares aparece {contador} vezes")

print (pares)