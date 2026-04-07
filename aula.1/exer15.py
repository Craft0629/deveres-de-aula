numero_termos=10
a, b = 0, 1

for i in range(numero_termos):
    print(a, end=' ')
    proximo = a + b
    a = b
    b = proximo