def primeiro_maior_50(lista):
    for i, num in enumerate(lista):
        if num > 50:
            return i, num

    return -1, None

lista = [10,20,40,60,70]

print(primeiro_maior_50(lista))