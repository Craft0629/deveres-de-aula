matriculas = [100, 200, 300, 400, 500, 600, 700]

def busca_binaria(lista, valor):

    if len(lista) == 0:
        return False

    meio = len(lista) // 2

    if lista[meio] == valor:
        return True

    if valor < lista[meio]:
        return busca_binaria(lista[:meio], valor)

    return busca_binaria(lista[meio + 1:], valor)


matricula = int(input("Digite a matrícula: "))

if busca_binaria(matriculas, matricula):
    print("Aluno encontrado!")
else:
    print("Aluno não encontrado!")