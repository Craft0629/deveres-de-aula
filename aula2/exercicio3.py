tarefas = []

while True:

    print("\n--- MENU ---")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Listar tarefas")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Nome da tarefa: ")
        tarefas.append({"nome": nome, "feito": False})

    elif escolha == "2":
        numero = int(input("Número da tarefa para remover: "))
        tarefas.pop(numero - 1)

    elif escolha == "3":
        numero = int(input("Número da tarefa concluída: "))
        tarefas[numero - 1]["feito"] = True

    elif escolha == "4":

        for i, tarefa in enumerate(tarefas):

            status = "FEITO" if tarefa["feito"] else "ESPERA"

            print(i+1, "-", tarefa["nome"], "[", status, "]")

    elif escolha == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida")