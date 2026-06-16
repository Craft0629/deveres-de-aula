faq = {
    "python": "Python é uma linguagem de programação.",
    "ia": "IA significa Inteligência Artificial.",
    "recursao": "Recursão é quando uma função chama ela mesma."
}


def chatbot():

    pergunta = input("Digite sua pergunta: ")

    if pergunta in faq:

        print(faq[pergunta])

    else:

        print("Pergunta não encontrada.")


chatbot()