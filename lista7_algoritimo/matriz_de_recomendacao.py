preferencias = [
    [5, 4, 3],
    [3, 5, 4],
    [4, 2, 5]
]


def mostrar_matriz():

    print("\nPREFERÊNCIAS DOS ALUNOS\n")

    for linha in preferencias:

        print(linha)


def consultar_preferencia():

    aluno = int(input("Digite a linha do aluno (0 a 2): "))

    ferramenta = int(input("Digite a coluna da ferramenta (0 a 2): "))

    print(
        "Nota:",
        preferencias[aluno][ferramenta]
    )


mostrar_matriz()

consultar_preferencia()