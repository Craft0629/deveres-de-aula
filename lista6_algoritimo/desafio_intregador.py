alunos = {}

sala = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


def cadastrar_aluno():

    matricula = input("Matrícula: ")

    nome = input("Nome: ")

    alunos[matricula] = {
        "nome": nome,
        "notas": []
    }


def lancar_nota():

    try:

        matricula = input("Matrícula: ")

        nota = float(input("Nota: "))

        alunos[matricula]["notas"].append(nota)

    except ValueError:

        print("Digite apenas números.")

    except KeyError:

        print("Matrícula não encontrada.")


def calcular_media():

    matricula = input("Matrícula: ")

    notas = alunos[matricula]["notas"]

    if len(notas) == 0:

        print("Sem notas.")

        return

    media = sum(notas) / len(notas)

    print("Média:", media)


def historico():

    matricula = input("Matrícula: ")

    notas = alunos[matricula]["notas"]

    print("Nome:", alunos[matricula]["nome"])

    print("Notas:", notas)

    if len(notas) > 0:

        print(
            "Média:",
            sum(notas) / len(notas)
        )


def buscar_matricula(lista, matricula):

    if lista == []:
        return False

    if lista[0] == matricula:
        return True

    return buscar_matricula(
        lista[1:],
        matricula
    )


def pesquisar():

    matricula = input("Matrícula: ")

    lista = list(alunos.keys())

    if buscar_matricula(lista, matricula):

        print("Aluno encontrado.")

    else:

        print("Aluno não encontrado.")


def salvar_arquivo():

    arquivo = open("alunos.txt", "w")

    for matricula, dados in alunos.items():

        arquivo.write(
            f"{matricula};{dados['nome']};{dados['notas']}\n"
        )

    arquivo.close()

    print("Arquivo salvo.")


def mostrar_sala():

    for linha in sala:

        print(linha)


def reservar_lugar():

    linha = int(input("Linha: "))

    coluna = int(input("Coluna: "))

    sala[linha][coluna] = 1


while True:

    print("\n1-Cadastrar Aluno")
    print("2-Lançar Nota")
    print("3-Calcular Média")
    print("4-Histórico")
    print("5-Buscar Matrícula")
    print("6-Salvar Arquivo")
    print("7-Mapa da Sala")
    print("8-Reservar Lugar")
    print("0-Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        lancar_nota()

    elif opcao == "3":
        calcular_media()

    elif opcao == "4":
        historico()

    elif opcao == "5":
        pesquisar()

    elif opcao == "6":
        salvar_arquivo()

    elif opcao == "7":
        mostrar_sala()

    elif opcao == "8":
        reservar_lugar()

    elif opcao == "0":
        break