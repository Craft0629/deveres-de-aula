def primo(n, divisor):
     if n % divisor == 0:
       return False
     
     if divisor * divisor >n:
       return True
     return primo(n, divisor + 1)




n=7
divisor=2

print(primo(n,divisor))