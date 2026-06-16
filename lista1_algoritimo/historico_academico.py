historico = {}

while True:

    print("\n1 - Adicionar disciplina")
    print("2 - Consultar histórico")
    print("3 - Calcular CRA")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        disciplina = input("Disciplina: ")
        nota = float(input("Nota: "))

        historico[disciplina] = nota

    elif opcao == "2":

        for disciplina, nota in historico.items():
            print(disciplina, "-", nota)

    elif opcao == "3":

        if len(historico) > 0:

            cra = sum(historico.values()) / len(historico)

            print("CRA:", cra)

        else:
            print("Nenhuma disciplina cadastrada.")

    elif opcao == "0":
        break