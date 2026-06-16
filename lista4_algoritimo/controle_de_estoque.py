estoque=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]


def cadrastar_quantidades():
    for linha in range(4):
        for coluna in range(4):

            estoque[linha][coluna]= int(input(f"quantidade[{linha}[{coluna}]:" ))

def atualizar_estoque():
    linha=int(input("linha: "))
    coluna=int(input("coluna: "))
    nova_quantidade=int(input("qual a nova quantidade?:"))
    estoque[linha][coluna] = nova_quantidade


def consultar_item():          
    linha=int(input("linha: "))
    coluna=int(input("coluna: "))
    print(estoque[linha][coluna])



cadrastar_quantidades()
atualizar_estoque()
consultar_item()