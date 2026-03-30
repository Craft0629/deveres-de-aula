try:
    saldo=int(input("qual o saldo atual que vc possui?:"))
    valor_transfe=int(input("qual o valor da transferencia:"))
    if saldo>valor_transfe:
       print("valor transferido")
 
    if saldo< valor_transfe:
        raise ValueError


except ValueError:
    print("saldo insuficiente para a transferencia")