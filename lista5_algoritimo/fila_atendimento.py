pacientes = [
    "Ana",
    "Carlos",
    "Pedro",
    "Maria"
]

def contar_pacientes(lista):

    if lista == []:
        return 0

    return 1 + contar_pacientes(lista[1:])

print(contar_pacientes(pacientes))