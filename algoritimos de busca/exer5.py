def aluno_maior_18(lista):
    for aluno in lista:
        if aluno["idade"] >= 18:
            return aluno["nome"]

    return None

alunos = [
{"nome":"João","idade":17},
{"nome":"Maria","idade":19},
{"nome":"Carlos","idade":16}
]

print(aluno_maior_18(alunos))