def mdc(numero1,numero2):
    if numero2==0:
      return numero1
    
    return mdc(numero2,numero1%numero2)


numero1=4
numero2=8
print(mdc(numero1,numero2))