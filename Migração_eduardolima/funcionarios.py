funcionarios = []


def adicionar_funcionario():
    funcionario = {}

    funcionario["nome"] = input("Nome: ")
    funcionario["cargo"] = input("Cargo: ")
    funcionario["salario"] = float(input("Salário: "))

    funcionarios.append(funcionario)

    print("Funcionário cadastrado!")


def listar_funcionarios():
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    print("\n=== LISTA DE FUNCIONÁRIOS ===")

    for i in range(len(funcionarios)):
        print(
            f"{i + 1}) "
            f"{funcionarios[i]['nome']} - "
            f"{funcionarios[i]['cargo']} - "
            f"R$ {funcionarios[i]['salario']:.2f}"
        )


def buscar_funcionario():
    nome_busca = input("Nome do funcionário: ")

    for funcionario in funcionarios:
        if funcionario["nome"] == nome_busca:
            print(
                f"Cargo: {funcionario['cargo']} | "
                f"Salário: R$ {funcionario['salario']:.2f}"
            )
            return

    print("Funcionário não encontrado.")


def menu():
    opcao = -1

    while opcao != 0:
        print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
        print("1 - Adicionar funcionário")
        print("2 - Listar funcionários")
        print("3 - Buscar funcionário")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_funcionario()

        elif opcao == 2:
            listar_funcionarios()

        elif opcao == 3:
            buscar_funcionario()

        elif opcao == 0:
            print("Encerrando...")

        else:
            print("Opção inválida!")


menu()