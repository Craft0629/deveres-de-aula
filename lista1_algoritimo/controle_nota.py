def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

nome = input("Nome do aluno: ")

notas = []

for i in range(3):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

media = calcular_media(notas)

print("Aluno:", nome)
print("Notas:", notas)
print("Média:", media)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")