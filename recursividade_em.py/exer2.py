def somadig(numero):
    if numero <10:
        return 1
    else:
        return 1 + somadig(numero // 10)
    



resultado=somadig(9876)
print(resultado)