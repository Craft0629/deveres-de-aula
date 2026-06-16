def fibonacci(n):

    if n == 1:
        return 1

    if n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


meses = int(input("Digite o número de meses: "))

print("Quantidade de usuários:", fibonacci(meses))

