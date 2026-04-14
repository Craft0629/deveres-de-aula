import os

produtos = []


def adicionar_produto():
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")

    while True:
        try:
            preco = float(input("Preço: "))
            if preco > 0:
                break
            else:
                print("Preço deve ser positivo.")
        except:
            print("Digite um número válido.")

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade >= 0:
                break
            else:
                print("Quantidade não pode ser negativa.")
        except:
            print("Digite um número inteiro.")

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print("Produto adicionado com sucesso!")


def atualizar_quantidade():
    nome = input("Qual produto deseja atualizar? ")

    for p in produtos:
        if p["nome"].lower() == nome.lower():
            try:
                valor = int(input("Digite quanto deseja adicionar/remover: "))
                p["quantidade"] += valor

                if p["quantidade"] < 0:
                    p["quantidade"] = 0

                print("Quantidade atualizada!")
            except:
                print("Valor inválido.")
            return

    print("Produto não encontrado.")


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for p in produtos:
        print(f"{p['nome']} | {p['categoria']} | R${p['preco']:.2f} | Qtd: {p['quantidade']}")


def ordenar_produtos():
    escolha = input("Ordenar por 'preco' ou 'quantidade': ").lower()
    ordem = input("Ordem 'crescente' ou 'decrescente': ").lower()

    reverse = True if ordem == "decrescente" else False

    if escolha == "preco":
        produtos.sort(key=lambda p: p["preco"], reverse=reverse)

    elif escolha == "quantidade":
        produtos.sort(key=lambda p: p["quantidade"], reverse=reverse)

    else:
        print("Opção inválida.")

def salvar_estoque():
    try:
        with open("estoque.txt", "w") as arquivo:
            for p in produtos:
                linha = f"{p['nome']},{p['categoria']},{p['preco']},{p['quantidade']}\n"
                arquivo.write(linha)

        print("Os dados foram salvos no arquivo 'estoque.txt'.")

    except Exception as erro:
        print("Erro ao salvar:", erro)



def carregar_estoque():
    if not os.path.exists("estoque.txt"):
        print("Arquivo não encontrado.")
        return

    try:
        with open("estoque.txt", "r") as arquivo:
            for linha in arquivo:
                nome, categoria, preco, quantidade = linha.strip().split(",")

                produto = {
                    "nome": nome,
                    "categoria": categoria,
                    "preco": float(preco),
                    "quantidade": int(quantidade)
                }

                produtos.append(produto)

        print("Dados carregados com sucesso!")

    except Exception as erro:
        print("Erro ao carregar:", erro)


while True:
    print("\nBem-vindo ao Sistema de Gestão de Estoque!")
    print("1. Adicionar produto")
    print("2. Atualizar quantidade")
    print("3. Listar produtos")
    print("4. Ordenar produtos")
    print("5. Salvar dados")
    print("6. Carregar dados")
    print("7. Sair")

    opcao = input("> ")

    if opcao == "1":
        adicionar_produto()

    elif opcao == "2":
        atualizar_quantidade()

    elif opcao == "3":
        listar_produtos()

    elif opcao == "4":
        ordenar_produtos()

    elif opcao == "5":
        salvar_estoque()

    elif opcao == "6":
        carregar_estoque()

    elif opcao == "7":
        sair = input("Deseja salvar antes de sair? (s/n): ")
        if sair.lower() == "s":
            salvar_estoque()
        print("Saindo...")
        break

    else:
        print("Opção inválida.")