# Exercícios de Revisão - Corrija os Bugs
 
# =============================================
# Exercício 1 - Estoque de Produtos
# =============================================
# Enunciado: Corrija o código para adicionar um produto na lista apenas se ele ainda não existir.
# O programa deve mostrar o estoque atualizado após cada tentativa.
 
estoque = ["Notebook", "Mouse", "Teclado"]
 
def adicionar_produto(estoque,produto):
    if produto not in estoque:
        estoque.append(produto)
    print("Estoque atual:", estoque)
 
adicionar_produto(estoque, "Monitor")
adicionar_produto(estoque, "Mouse")
adicionar_produto(estoque, "computador")
adicionar_produto(estoque, "fio")



 
