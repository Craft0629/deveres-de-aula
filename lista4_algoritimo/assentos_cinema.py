Assentos=[
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]



def reservar_cadeira():
            
            linha=int(input("qual a linha? "))
            coluna=int(input("qual a coluna? "))
            Assentos[linha][coluna]=1


def cancelar_reserva_de_cadeira():
            linha=int(input("qual a linha da cadeira quer cancelar? "))       
            coluna=int(input("qual a coluna da cadeira que quer cancelar? "))
            Assentos[linha][coluna]=0



def mapa():
        print("\n=== Assentos disponiveis===\n")

        for linha in Assentos:
                for assento in linha:
                        print(assento,end=" ")
                    
                print()


mapa()

reservar_cadeira()

mapa()

cancelar_reserva_de_cadeira()

mapa()


