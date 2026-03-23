def somadig(numero):
    if numero <10:
        return numero
    else:
        return (numero % 10) + somadig(numero // 10)


resultado=somadig(123)
print(resultado)
