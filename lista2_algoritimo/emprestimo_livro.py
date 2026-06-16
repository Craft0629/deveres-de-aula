livros={
    "livro a":20,
    "livro b":10,
    "livro c":0,
    "livro d":1,
}

def consultar_estoque():
    for livro, quantidade in livros.items():
        print(f"Livro: {livro}")
        print(f"Quantidade: {quantidade}")
        print("-" * 25)


def editar_estoque():
    livro_escolhido=input("qual livro voce deseja pegar?")
    if livro_escolhido in livros:
         print("livro encontrado")
    else:
        print("livro nao encontrado")
    quantidade=int(input("qual a quantidade deseja retirar?"))

    if quantidade <= livros[livro_escolhido]:
        livros[livro_escolhido] -= quantidade
        print("Empréstimo realizado!")
    else:
        print("Quantidade indisponível.")



consultar_estoque()
editar_estoque()
consultar_estoque()