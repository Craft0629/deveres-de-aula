def buscar_titulo():

    try:

        titulo = input("Digite o título: ")

        if titulo == "":
            raise ValueError

        arquivo = open("livros.txt", "r")

        encontrado = False

        for linha in arquivo:

            dados = linha.strip().split(";")

            if dados[0].lower() == titulo.lower():

                print("Livro encontrado!")
                print("Autor:", dados[1])
                print("Quantidade:", dados[2])

                encontrado = True

        arquivo.close()

        if encontrado == False:
            print("Livro não encontrado.")

    except FileNotFoundError:

        print("Arquivo não encontrado.")

    except ValueError:

        print("Título inválido.")

buscar_titulo()