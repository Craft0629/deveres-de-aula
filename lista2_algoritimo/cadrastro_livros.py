

def cadastro_de_autor():
    nome=input("qual o nome do autor: ")
    quantidade=int(input("qual a quantidade de livros? "))
    
    

    autor={
        "nome": nome,
        "quantidade_livros": quantidade,
        "titulos": []
    }

    for i in range (quantidade):
            titulo=input("quais os titulos do livro? ")
            autor["titulos"].append(titulo)




def salvar_em_arquivo(autor):
  with open("autores.txt", "a") as arquivo:

        arquivo.write(
            f"{autor['nome']};"
            f"{autor['quantidade_livros']};"
            f"{autor['titulos']}\n"
        )

cadastro_de_autor()
salvar_em_arquivo()