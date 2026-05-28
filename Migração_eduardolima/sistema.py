def menu():
    print("=== SISTEMA DE CADASTRO DE ALUNOS ===")

    num_alunos = 5

    nomes = []
    notas = []

    total_notas = 0

    for i in range(num_alunos):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        nota = float(input(f"Digite a nota de {nome}: "))

        nomes.append(nome)
        notas.append(nota)

        total_notas += nota

    media_alunos = media(total_notas, num_alunos)

    lista_alunos(nomes, notas)

    print(f"Média da turma: {media_alunos:.2f}")


def media(total_notas, num_alunos):
    return total_notas / num_alunos


def lista_alunos(nomes, notas):
    print("\n=== LISTA DE ALUNOS ===")

    for i in range(len(nomes)):
        print(f"{nomes[i]} | Nota: {notas[i]}")


menu()