# AULA 05 - PYTHON: FUNÇÕES 2

# ATIVIDADE DE REVISÃO
# FAÇA UMA FUNÇÃO QUE RECEBE NO PARÂMETRO, O NOME E A IDADE DE ALGUEM
# E RETORNE UMA MENSAGEM TIPO:
# "FULANO VOCÊ É MAIOR DE IDADE"
# OU
# "FULANO VOCÊ É MENOR DE IDAD
def checarMaiorIdade(nome, idade):
  if idade >= 18:
    return f"{nome} você é maior de idade"
  else:
    return f"{nome} você é menor de idade"
  

print(checarMaiorIdade(nome="João", idade=30))

nome = input("Digite um nome: ")
idade = int(input("Digite uma idade: "))
print(checarMaiorIdade(nome=nome, idade=idade))
print(checarMaiorIdade(idade=idade, nome=nome))
print(checarMaiorIdade(nome, idade))
# print(checarMaiorIdade(idade, nome)) ISSO AQUI DA ERRADO.



# TIPANDO E COLOCANDO VALORES DEFAULT
def checarMaiorIdade(nome:str = "Desconhecido", idade:int = 0):
  if idade >= 18:
    return f"{nome} você é maior de idade"
  else:
    return f"{nome} você é menor de idade"
  

print(checarMaiorIdade(nome="João", idade=30))

nome = input("Digite um nome: ")
idade = int(input("Digite uma idade: "))
print(checarMaiorIdade(nome=nome, idade=idade))
print(checarMaiorIdade(idade=idade, nome=nome))
print(checarMaiorIdade(nome, idade))
print(checarMaiorIdade(idade = 50))
print(checarMaiorIdade(nome = "Maria"))
# print(checarMaiorIdade(idade, nome)) ISSO AQUI DA ERRADO.

# ATIVIDADE 1
# FAÇA UMA FUNÇÃO QUE RECEBE UMA LISTA DE IDADES E RETORNE QUANTOS DESSA LISTA SÃO MAIORES DE IDADE.
def checarMaioresIdade(lista_de_idades):
  qtde_maiores = 0
  for element in lista_de_idades:
    if element >= 18:
      qtde_maiores += 1
  return qtde_maiores

print(checarMaioresIdade(lista_de_idades=[10, 15, 30, 40, 50]))
idades = [40, 52, 90, 14, 10, 47, 33]
print(checarMaioresIdade(lista_de_idades=idades))

# ATIVIDADE 2
# FAÇA UMA FUNÇÃO QUE RECEBE A PLACA DE UM VEÍCULO, E A VELOCIDADE QUE ELE PASSOU E RETORNA UMA MULTA SE ELE PASSOU ACIMA DE 50
def fotoSensor(placa, velocidade):
  if velocidade >= 50:
    return f"Veículo de placa {placa} multado."

print(fotoSensor(placa="HJI-8561", velocidade=120))
print(fotoSensor(placa="OPQN-525", velocidade=40))


# ATIVIDADE 3
# FAÇA UMA FUNÇÃO QUE RECEBE UMA LISTA DE DICIONÁRIOS REPRESENTANDO PRODUTOS COM NOME, MARCA, PREÇO, E RETORNE QUAL O NOME DO PRODUTO MAIS CARO.







# ASSUNTO DA AULA 5

# *ARGS
# *ARGS não sabe quantos argumentos vao ser.
# transforma os itens em uma tupla
def calcularMedia(*notas):
  return notas

print(calcularMedia(5, 2, 8, 10))
print(calcularMedia(5, 2))
print(calcularMedia(5, 2, 6))

# **KWARGS
# **KWARGS
# RECEBE UM NÚMERO ILIMITADO DE ITENS E TRANSFORMA ELES NUM DICIONÁRIO.
def dadosPessoais(**informacoes):
    return informacoes

print(dadosPessoais(nome="João", idade=30, telefone="8598632694"))
print(dadosPessoais(nome="João"))


# FUNÇÃO LAMBDA
funcao = lambda nome : f"Olá {nome}"
print(funcao("João"))


# CONDICONAL COM LAMBDA
def checarIdade(idade):
  if idade >= 18:
    return "Maior"
  else:
    return "Menor"

funcao = lambda idade : "Maior" if idade >= 18 else "Menor"


# ELIF NA LAMBDA
def checarNumero(n):
  if n > 0:
    return "Positivo"
  elif n < 0:
    return "Negativo"
  else:
    return "Neutro"

funcao = lambda n : "Positivo" if n > 0 else "Negativo" if n < 0 else "Neutro"

# FILTER
# def filtrarMaiores(lista_de_idades):
#   lista_de_maiores = []
#   for element in lista_de_idades:
#     if element >= 18:
#       lista_de_maiores.append(element)
#   return lista_de_maiores

# idades = [30, 40, 10, 8, 15, 20]
# print(filtrarMaiores(lista_de_idades=idades))


idades = [30, 40, 10, 8, 15, 20]
lista_de_maiores = list(filter(lambda element : element >= 18), idades)

# MAP ()
# def aplicarPromocao(lista_de_precos):
#   lista_promocional = []
#   for element in lista_de_precos:
#     lista_promocional.append(element / 2)
#   return lista_promocional

precos = [20, 9.99, 100, 50, 45.90, 1000]
promocional = list(map(lambda element: element / 2), precos )


# REDUCE (A DESGRAÇA)
# def somatoria(lista_de_numeros):
#   soma = 0
#   for element in lista_de_numeros:
#     soma += element
#   return soma

import functools
numeros = [10,20,30]
somatoria = list(functools.reduce(lambda x, y: x+y), numeros)

# AULA 06 - PYTHON: PROJETO LISTA DE TAREFAS

# MODELO DE TAREFAS:

# NOME: VARRER A CASA
# CATEGORIA: DOMÉSTICA
# PRIORIDADE: BAIXA
# STATUS: PENDENTE

# NOME: ESTUDAR PYTHON
# CATEGORIA: ACADÊMICO
# PRIORIDADE: ALTA
# STATUS: CONCLUÍDO

# NOME: IR PARA ACADEMIA
# CATEGORIA: ESPORTE
# PRIORIDADE: MÉDIA
# STATUS: PENDENTE




# ESCOLHA UMA OPÇÃO:
# 1 - ADICIONAR TAREFA
# 2 - VER TODAS AS TAREFAS
# 3 - MARCAR UMA TAREFA COMO CONCLUÍDA
# 4 - FILTRAR TAREFAS POR PRIORIDADE
# 5 - FILTRAR TAREFAS POR CATEGORIA
# 0 - SAIR