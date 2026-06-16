frequencias = []

quantidade = int(input("Quantas aulas? "))

for i in range(quantidade):
    presenca = input("P para presença ou F para falta: ")
    frequencias.append(presenca.upper())

presencas = frequencias.count("P")

percentual = (presencas / quantidade) * 100

print("Frequências:", frequencias)
print("Percentual:", percentual, "%")