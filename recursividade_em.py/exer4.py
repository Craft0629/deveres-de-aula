def palindro(texto):

    if len(texto) <= 1:
        return True

    if texto[0] != texto[-1]:
        return False

    return palindro(texto[1:-1])
    

print(palindro("arara"))