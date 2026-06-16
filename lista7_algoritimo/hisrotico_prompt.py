prompts = []


def adicionar_prompt():

    prompt = input("Digite o prompt: ")

    prompts.append(prompt)

    print("Prompt salvo!")


def mostrar_historico():

    print("\nHISTÓRICO DE PROMPTS\n")

    for prompt in prompts:

        print(prompt)


adicionar_prompt()
adicionar_prompt()
mostrar_historico()