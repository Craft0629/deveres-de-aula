saldo = 0
extrato = []



def deposito():

   global saldo

try:

        valor = float(input("Valor: "))

        if valor <= 0:
            raise ValueError

        saldo += valor

        extrato.append(("deposito", valor))

except ValueError:

        print("Valor inválido.")
def saque():

   
    global saldo

    try:

        valor = float(input("Valor do saque: "))

        if valor <= 0:
            raise ValueError

        if valor > saldo:
            raise Exception("Saldo insuficiente")

        saldo -= valor

        extrato.append(("saque", valor))

    except ValueError:

        print("Valor inválido.")

    except Exception as erro:

        print(erro)

    

def consultar_saldo():

    print("Saldo:", saldo)

def mostrar_extrato():

    for item in extrato:
        print(item)


def total_depositado():

    total = 0

    for operacao, valor in extrato:

        if operacao == "deposito":

            total += valor

    print(total)

def total_sacado():

    total = 0

    for operacao, valor in extrato:

        if operacao == "saque":

            total += valor

    print(total)



deposito()
saque()
consultar_saldo()
mostrar_extrato()
total_depositado()
total_sacado()