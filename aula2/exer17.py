lista1=[10,5,20,7,15] 
lista2=[10,15,25,8,12]

def comparar_listas(lista1, lista2):

    if sorted(lista1) == sorted(lista2):
        return True
    else:
        return False
   
print(comparar_listas(lista1,lista2))
    
