def fazer_backup():

    origem = open("livros.txt", "r")

    dados = origem.read()

    backup = open("backup.txt", "w")

    backup.write(dados)

    origem.close()
    backup.close()

    print("Backup realizado com sucesso!")



fazer_backup()