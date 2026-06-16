estoque_A=[
    [2,5],
    [10,8]
]

estoque_B=[
    [4,2],
    [2,10]
]


juncao=[
    [0,0],
    [0,0]
]

def muitiplicacao():
    for linha in range(2):
        for coluna in range(2):
            
            juncao[linha][coluna]=(estoque_A[linha][coluna]*estoque_B[linha][coluna])


muitiplicacao()
print(juncao)