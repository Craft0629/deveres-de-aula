cores={
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255)
    }
cores2=input("selecione uma cor vermelho,verde,azul: ").lower()
if cores2 =="vermelho":
    print(cores.get('vermelho'))

elif cores2=="verde":
    print(cores.get('verde'))

elif cores2 =="azul":
    print(cores.get('azul'))
    
try:
    print(cores[cores2])
except KeyError:
    print("não tem essa cor")