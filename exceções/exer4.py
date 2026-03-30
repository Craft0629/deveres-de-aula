def valida_senha(senha):
    if len(senha) < 8:
        raise ValueError("a senha tem que ter mais que 8 caracteres")

    if not any(c.isdigit() for c in senha):
        raise ValueError("a senha precisa ter pelo menos um número")
try:
    senha = input("coloque a senha: ")
    valida_senha(senha)
    print("senha válida")


except Exception as e:
    print("talvez vc tenha colocado menos numeros", e)
