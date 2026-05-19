import random

mapa = []

tentativas = 0


for i in range(5):
    linha = []
    for j in range(5):
        linha.append("-")
    mapa.append(linha)


tesouro_linha = random.randint(0, 4)
tesouro_coluna = random.randint(0, 4)

print("=== CAÇA AO TESOURO ===")
print("encontre o tesouro na matriz 5x5")

while True:

    
    for linha in mapa:
        print(linha)

    try:
        linha = int(input("digite a linha (0 a 4): "))
        coluna = int(input("digite a coluna (0 a 4): "))

        if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
            print("posição inválida")
            continue

        tentativas += 1

        
        if linha == tesouro_linha and coluna == tesouro_coluna:
            mapa[linha][coluna] = "X"

            print("\nVOCÊ ENCONTROU O TESOURO!")
            print(f"tentativas: {tentativas}")

            for linha_mapa in mapa:
                print(linha_mapa)

            break

        
        distancia = abs(linha - tesouro_linha) + abs(coluna - tesouro_coluna)

        if distancia == 1:
            print("Muito perto")

        elif distancia == 2 or distancia == 3:
            print("Perto")

        else:
            print("Longe")

        mapa[linha][coluna] = "*"

    except:
        print("digite números válidos")