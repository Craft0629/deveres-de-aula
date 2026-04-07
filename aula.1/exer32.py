n = int(input("coloque um numero para ver se é primo ou nao: "))

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if primo(n):
    print("É primo")
else:
    print("Não é primo")