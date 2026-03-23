def multi(numero,numero2):
    
    if numero==1:
        return numero2
        
    return numero2 + multi(numero - 1, numero2)
        

numero=3
numero2=4
print(multi(numero,numero2))






    
    