try:
    x=float(input("coloque um numero: "))
    y=float(input("coloque mais um numero: "))
    resultado=x/y
    print(resultado)
except ZeroDivisionError:
    print("é possivel fazer uma divisão por zero")
finally:
    print("Tenha uma boa tarde")