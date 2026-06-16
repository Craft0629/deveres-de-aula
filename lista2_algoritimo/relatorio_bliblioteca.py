def total_livros():

    arquivo = open("livros.txt", "r")

    total = 0

    for linha in arquivo:
        total += 1

    arquivo.close()

    print("Total de livros:", total)


def autor_mais_frequente():

    arquivo = open("livros.txt", "r")

    autores = {}

    for linha in arquivo:

        dados = linha.strip().split(";")

        autor = dados[1]

        if autor in autores:
            autores[autor] += 1
        else:
            autores[autor] = 1

    arquivo.close()

    mais_frequente = max(autores, key=autores.get)

    print("Autor mais frequente:", mais_frequente)


def livro_maior_quantidade():

    arquivo = open("livros.txt", "r")

    maior = 0
    nome_livro = ""

    for linha in arquivo:

        dados = linha.strip().split(";")

        titulo = dados[0]
        quantidade = int(dados[2])

        if quantidade > maior:

            maior = quantidade
            nome_livro = titulo

    arquivo.close()

    print("Livro com maior quantidade:", nome_livro)
    print("Quantidade:", maior)


total_livros()
autor_mais_frequente()
livro_maior_quantidade()
