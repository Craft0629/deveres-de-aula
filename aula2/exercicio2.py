aluno={
    "nome": "joao", 
    "idade": 18,
    "nota": 9.5,
    "cidade":"São Paulo"
}
print(aluno["idade"])
print(aluno.keys())

for chave, valor in aluno.items():
    print(chave, valor)