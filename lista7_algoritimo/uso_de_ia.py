usuarios = {}


def cadastrar_usuario():

    aluno = input("Nome do aluno: ")

    ferramenta = input("Ferramenta utilizada: ")

    frequencia = int(input("Frequência de uso: "))

    usuarios[aluno] = {
        "ferramenta": ferramenta,
        "frequencia": frequencia
    }


def mostrar_estatisticas():

    print("\nESTATÍSTICAS\n")

    for aluno, dados in usuarios.items():

        print("Aluno:", aluno)
        print("Ferramenta:", dados["ferramenta"])
        print("Frequência:", dados["frequencia"])
        print("-" * 20)


cadastrar_usuario()
cadastrar_usuario()

mostrar_estatisticas()