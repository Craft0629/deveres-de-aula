def aluno_aprovado(lista):
    for nome, nota in lista:
        if nota >= 7 and nome.startswith("A"):
            return nome

    return "Não encontrado"

alunos = [
("Ana",8),
("Bruno",9),
("Amanda",6),
("Alice",7)
]

print(aluno_aprovado(alunos))