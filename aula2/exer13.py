numeros =[10,5,20,7,15]


def maior_menor(numeros):

    maior = numeros[0]
    menor = numeros[0]
    
    
    
    for numero in numeros:

        if numero > maior:
            maior=numero

        if numero < menor:
            menor=numero

    return maior, menor

print (maior_menor(numeros))