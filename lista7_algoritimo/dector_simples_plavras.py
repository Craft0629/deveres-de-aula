def salvar_texto():

    texto = input("Digite uma resposta: ")

    arquivo = open("resposta.txt", "w")

    arquivo.write(texto)

    arquivo.close()


def contar_palavras():

    arquivo = open("resposta.txt", "r")

    texto = arquivo.read()

    arquivo.close()

    palavras = texto.split()

    print("Quantidade de palavras:", len(palavras))


salvar_texto()
contar_palavras()