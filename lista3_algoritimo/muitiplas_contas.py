clientes = {
    "123": {
        "nome": "Ana",
        "saldo": 500,
        "extrato": []
    },

    "456": {
        "nome": "Eduardo",
        "saldo": 1000,
        "extrato": []
    }
}
def busca_de_conta_para_depositar():

    conta = input("Conta: ")

    valor = float(input("Valor: "))

    clientes[conta]["saldo"] += valor
    
    clientes[conta]["extrato"].append(
    ("deposito", valor)
)


def saque():

   
  

    try:

        conta = input("Conta: ")
        valor = float(input("Valor do saque: "))

        if valor <= 0:
            raise ValueError

        if valor > clientes[conta]["saldo"]:
            raise Exception("Saldo insuficiente")

        clientes[conta]["saldo"] -= valor

        clientes[conta]["extrato"].append(
    ("saque", valor)
)

    except ValueError:

        print("Valor inválido.")

    except Exception as erro:

        print(erro)

    

def consultar_saldo():

   conta = input("Conta: ")

   print("Saldo:", clientes[conta]["saldo"])


def mostrar_extrato():

    conta = input("Conta: ")

    for item in clientes[conta]["extrato"]:
        print(item)


def total_depositado():

    total_depositado = 0

    conta = input("Conta: ")

    if conta not in clientes:
        print("Conta não encontrada")
        return

    for operacao, valor in clientes[conta]["extrato"]:

        if operacao == "deposito":

            total_depositado += valor

    print("Total depositado:", total_depositado)


def total_sacado():

    total_sacado = 0

    conta = input("Conta: ")

    if conta not in clientes:
        print("Conta não encontrada")
        return

    for operacao, valor in clientes[conta]["extrato"]:

        if operacao == "saque":

            total_sacado += valor

    print(total_sacado)



busca_de_conta_para_depositar()
saque()
consultar_saldo()
mostrar_extrato()
total_depositado()
total_sacado()