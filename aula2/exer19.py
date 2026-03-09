lista=[-9,-8,-6,-4,-2,1,4,5,7,8,9,12]

for i in range(len(lista)-1, -1, -1):
    if lista[i] < 5:
        lista.pop(i)

print(lista)