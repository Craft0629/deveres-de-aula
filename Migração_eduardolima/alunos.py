alunos = []
def main_Menu(): #Esse bloco abre o menu principal
    while True:
        try:
            menu = int(input('Main Menu \n1 -> Add Studant \n2 -> List Studants \n3 -> Get Grade \n4 -> Log Out\n'))
            match menu:
                case 1:
                    adicionar_Alunos()
                case 2:
                    listar_Alunos()
                case 3:
                    buscar_Notas()
                case 4:
                    print('Leaving APP...')
                    break
                case _:
                    print('Error! Plase enter a valid number')
        except ValueError:
            print('Please type only numbers')

def adicionar_Alunos():
    aluno = {}
    aluno['nome'] = input('Enter studants name: ').capitalize
    while True:
        try:
            aluno['nota'] = float(input('Enter studants grade: '))
            break
        except ValueError:
            print('Please type only numbers')
    alunos.append(aluno)

def listar_Alunos():
    for aluno in alunos:
        print(f'Name: {aluno['nome']} | Grade: {aluno['nota']:.2f}')

def buscar_Notas():
    quem = input('Type studants name: ')
    if quem in alunos:
        print(f'{quem['nota']} ')

        # h2