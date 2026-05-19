tabuleiro=[]
for i in range(8):
    linha=[]
    for j in range(8):
        linha.append(".")
    tabuleiro.append(linha)
colunas=["a","b","c","d","e","f","g","h"]
posicao=input("Digite a posição inicial do cavalo, exemplo e4: ").lower()
if len(posicao)!=2:
    print("Posição inválida! Digite no formato correto, exemplo: e4")
else:
    coluna_letra=posicao[0]
    linha_numero=posicao[1]
    if coluna_letra not in colunas or linha_numero not in "12345678":
        print("Posição inválida! Use colunas de a até h e linhas de 1 até 8.")
    else:
        coluna_cavalo=colunas.index(coluna_letra)
        linha_cavalo=8-int(linha_numero)
        tabuleiro[linha_cavalo][coluna_cavalo]="C"
        movimentos=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
        for movimento in movimentos:
            nova_linha=linha_cavalo+movimento[0]
            nova_coluna=coluna_cavalo+movimento[1]
            if nova_linha>=0 and nova_linha<=7 and nova_coluna>=0 and nova_coluna<=7:
                tabuleiro[nova_linha][nova_coluna]="*"
        print("\nTabuleiro final:\n")
        print("   a b c d e f g h")
        numero_linha=8
        for linha in tabuleiro:
            print(numero_linha,end="  ")
            for casa in linha:
                print(casa,end=" ")
            print(" ",numero_linha)
            numero_linha-=1
        print("   a b c d e f g h")