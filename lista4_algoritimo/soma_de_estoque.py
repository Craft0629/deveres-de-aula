estoque_A=[
    [2,4],
    [5,9]
]

estoque_B=[
    [4,6],
    [5,1]
]

estoques_juntos=[
    [0,0],
    [0,0]
]

def soma_do_estoque():
    for linha in range(2):
        for coluna in range (2):
            estoques_juntos[linha][coluna]=(estoque_A[linha][coluna]+estoque_B[linha][coluna])


soma_do_estoque()

print(estoques_juntos)