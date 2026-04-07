numero = int(input("Coloque um numero para ver seu fatorial: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é {fatorial}")