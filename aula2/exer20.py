lista=[1,2,3]

def soma_acumulada(lista):

    resultado = []
    soma = 0

    for numero in lista:
        soma = soma + numero
        resultado.append(soma)

    return resultado

print(soma_acumulada(lista))