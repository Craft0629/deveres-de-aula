alunos=[]


def adicionar_aluno():
   nome=(input("qual o nome do aluno: "))
   
   notas = []
   while True:
        try:
            qtd = int(input("Quantas notas (2 a 5): "))
            if 2 <= qtd <= 5:
                break
            else:
                print("Digite entre 2 e 5.")
        except:
            print("Digite um número válido.")

   for i in range(qtd):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve ser entre 0 e 10.")
            except:
                print("Digite um número válido.")
   
   media=sum(notas)/len(notas)
      
   aluno = {
        "nome": nome,
        "notas": notas,
        "media": media
      }
   alunos.append(aluno)

      
def ordenar_alunos():
   alunos.sort(key=lambda aluno: aluno["media"], reverse=True)

def salvar_em_arquivo():   
   import os

   if os.path.exists("alunos.txt"):
        escolha = input("Arquivo já existe. Deseja sobrescrever? (s/n): ")
        if escolha.lower() != "s":
            print("Operação cancelada.")
            return

   try:
        with open("alunos.txt", "w") as arquivo:
            for aluno in alunos:
                linha = f"{aluno['nome']},{aluno['media']:.2f}\n"
                arquivo.write(linha)
        print("Os dados foram salvos no arquivo 'alunos.txt'.")
    
   except Exception as erro:
        print("Erro ao salvar arquivo:", erro)


while True:
      adicionar_aluno()
      
      continuar = input("Deseja adicionar outro aluno? (s/n): ")
      if continuar.lower() != "s":
        break

      ordenar_alunos()

print(alunos)

salvar_em_arquivo()





