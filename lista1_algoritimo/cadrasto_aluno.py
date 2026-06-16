
alunos = []

def cadastro():
    nome = input("Qual o nome do aluno? ")
    matricula = input("Qual a matrícula? ")
    curso = input("Qual o curso? ")

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "curso": curso
    }

    alunos.append(aluno)
    print("aluno cadrastrado")

def listar_alunos():
    print("aqui esta a lista de alunos")
    print(alunos)
    

def buscar_aluno():#aqui foi mais um teste pq eu queria ver se dava pra buscar pelo nome ou matricula ou curso foi algo que eu realmente quis ver se daria pra fazer e deu realmente pra fazer :D
    busca=input("buscar por nome matricula ou curso?")

    if busca not in ["nome","matricula","curso"]:
        print("opção invalida")
        return
    valor = input(f"digite {busca}: ")
  

    for aluno in alunos:
        if aluno[busca]==valor:
            print("nome:", aluno["nome"])
            print("matricula:", aluno["matricula"])
            print("curso:", aluno["curso"])
            print()
           

      
while True:
    print("opções do sistema:")
    print("para cadrastrar digite 1: ")
    print("para listar alunos digite 2: ")
    print("para buscar algum aluno digite 3: ")
    print("para sair do sistema digite 4")

    opcoes=input("")

    if opcoes=="1":
        cadastro()
    elif opcoes=="2":
        listar_alunos()
    elif opcoes=="3":
        buscar_aluno()
    elif opcoes=="4":
        break

