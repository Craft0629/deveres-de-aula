def buscar_matriz_ordenada(matriz, alvo):
    linha = 0
    coluna = len(matriz[0]) - 1

    while linha < len(matriz) and coluna >= 0:
        valor = matriz[linha][coluna]

        if valor == alvo:
            return linha, coluna
        elif valor > alvo:
            coluna -= 1
        else:
            linha += 1

    return -1, -1

matriz = [
[1,4,7,11],
[2,5,8,12],
[3,6,9,16],
[10,13,14,17]
]

print(buscar_matriz_ordenada(matriz,9))