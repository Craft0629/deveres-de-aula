def contar_vogais(texto):
    return sum(1 for c in texto.lower() if c in "aeiou")

print(contar_vogais("python"))