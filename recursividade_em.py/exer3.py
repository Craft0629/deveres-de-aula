def inverter(texto):

    if len(texto) <= 1:
        return texto

    return inverter(texto[1:]) + texto[0]


print(inverter("recursao"))
