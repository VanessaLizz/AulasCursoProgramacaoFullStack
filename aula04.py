# AULA 04: PYTHON: FUNÇÕES

# ATIVIDADE REVISÃO
# FAÇA UM PROGRAMA DE CONTROLE DE ESTOQUE.
# 1 - ADICIONAR PRODUTO
#       NOME, MARCA, UNIDADE, PREÇO, QTDE_ESTOQUE
# 2 - VER TODOS OS PRODUTOS 
# 3 - REMOVER UM PRODUTO
# 0 - SAIR

lista_de_produtos = []

while True:
    menu = input("""
    Escolha uma opção:
    1 - Adicionar produto
    2 - Ver todos produtos
    3 - Remover um produto
    0 - Sair  
    """)
    if menu == "1":
        nome = input("Digite o nome do produto: ")
        marca = input("Digite a marca do produto: ")
        unidade = input("Digite a unidade do produto (Ex: 1L, 1KG): ")
        preco = float(input("Digite o preco do produto: "))
        qtde = int(input("Digite a quantidade em estoque do produto: "))
        
        novo_produto = {
            "Nome": nome,
            "Marca": marca,
            "Unidade": unidade,
            "Preço": preco,
            "Quantidade em Estoque": qtde
        }
        lista_de_produtos.append(novo_produto)
    elif menu == "2":
        for element in lista_de_produtos:
            print(f"{element['Nome']} {element['Marca']} - {element['Unidade']} | R${element['Preço']} ")
    elif menu == "3":
        nome_excluir = input("Digite o nome do produto que você quer excluir: ")
        qtde_produtos_encontrados = 0
        for element in lista_de_produtos:
            if element["Nome"] == nome_excluir:
                lista_de_produtos.remove(element)
                qtde_produtos_encontrados += 1
                print("Item removido com sucesso")
        if qtde_produtos_encontrados == 0:
            print("Produto não encontrado")
    elif menu == "0":
        break
    else:
        print("Opção inválida")


# FUNÇÕES
def cumprimentar():
    return "Olá, seja bem vindo"

cumprimentar()
print(cumprimentar())
print(cumprimentar())
print(cumprimentar())

# PARÂMETRO
def cumprimentar(aluno):
    return f"Olá {aluno}, seja bem vindo"

print(cumprimentar(aluno="João"))
print(cumprimentar(aluno="Maria"))
print(cumprimentar(aluno="Gabriel"))
nome = input("Digite o nome do aluno: ")
print(cumprimentar(aluno=nome))

# ARGUMENTOS
def dividir(x1, x2):
    resultado = x1 / x2
    return resultado

print(dividir(x1=10, x2=30))
print(dividir(x1=20, x2=50))
print(dividir(x2=50, x1=20))

# TIPAGEM
def cumprimentar(nome:str, hora:int):
    if hora >= 5 and hora <= 12:
        return f"Bom dia {nome}"
    elif hora >= 13 and hora <= 18:
        return f"Boa tarde {nome}"
    else:
        return f"Boa noite {nome}"

print(cumprimentar(hora=20, nome="Abel"))
print(cumprimentar(nome="João", hora=9))
print(cumprimentar(nome="Maria", hora=14))