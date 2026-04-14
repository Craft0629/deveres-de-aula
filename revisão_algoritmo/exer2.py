import os

livros = []

def adicionar_livro():
    titulo = input("Qual o nome do livro: ")
    autor = input("Qual o nome do autor do livro: ")


    while True:
        try:
            ano = int(input("Qual o ano de publicação do livro: "))
            if ano > 0:
                break
            else:
                print("Digite um ano válido.")
        except:
            print("Digite um número inteiro.")

   
    while True:
        try:
            paginas = int(input("Quantas páginas tem o livro: "))
            if paginas > 0:
                break
            else:
                print("Digite um número válido.")
        except:
            print("Digite um número inteiro.")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "paginas": paginas
    }

    livros.append(livro)
    print("Livro adicionado com sucesso!")



def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']}) - {livro['paginas']} páginas")



def ordenar_livros():
    escolha = input("Ordenar por 'ano' ou 'paginas': ").lower()
    ordem = input("Ordem 'crescente' ou 'decrescente': ").lower()

    reverse = True if ordem == "decrescente" else False

    if escolha == "ano":
        livros.sort(key=lambda livro: livro["ano"], reverse=reverse)

    elif escolha == "paginas":
        livros.sort(key=lambda livro: livro["paginas"], reverse=reverse)

    else:
        print("Opção inválida.")



def salvar_livros():
    try:
        with open("biblioteca.txt", "w") as arquivo:
            for livro in livros:
                linha = f"{livro['titulo']},{livro['autor']},{livro['ano']},{livro['paginas']}\n"
                arquivo.write(linha)
        print("Os dados foram salvos no arquivo 'biblioteca.txt'.")
    
    except Exception as erro:
        print("Erro ao salvar:", erro)



def carregar_livros():
    if not os.path.exists("biblioteca.txt"):
        print("Arquivo não encontrado.")
        return

    try:
        with open("biblioteca.txt", "r") as arquivo:
            for linha in arquivo:
                titulo, autor, ano, paginas = linha.strip().split(",")

                livro = {
                    "titulo": titulo,
                    "autor": autor,
                    "ano": int(ano),
                    "paginas": int(paginas)
                }

                livros.append(livro)

        print("Dados carregados com sucesso!")

    except Exception as erro:
        print("Erro ao carregar:", erro)



while True:
    print("\nBem-vindo à Biblioteca Digital!")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Ordenar livros")
    print("4. Salvar dados")
    print("5. Carregar dados")
    print("6. Sair")

    opcao = input("> ")

    if opcao == "1":
        adicionar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        ordenar_livros()

    elif opcao == "4":
        salvar_livros()

    elif opcao == "5":
        carregar_livros()

    elif opcao == "6":
        sair = input("Deseja salvar antes de sair? (s/n): ")
        if sair.lower() == "s":
            salvar_livros()
        print("Saindo...")
        break

    else:
        print("Opção inválida.")