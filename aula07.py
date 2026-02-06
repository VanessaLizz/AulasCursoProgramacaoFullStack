# AULA 07 - PYTHON: MÓDULOS E BIBLIOTECAS

# 1) FAÇA UMA FUNÇÃO QUE RECEBE NO PARÂMETRO UMA IDADE E RETORNA SE É MAIOR OU MENOR DE IDADE.
# 2) FAÇA UMA FUNÇÃO QUE RECEBE UM NÚMERO QUALQUER E RETORNE SE ELE É POSITIVO, NEGATIVO, NEUTRO.
# 3) FAÇA UMA FUNÇÃO QUE RECEBE UMA LISTA DE NUMEROS E RETORNA A MÉDIA DESSES NÚMEROS.
# 4) FAÇA UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMERO E RETORNA QUAL É O MAIOR DELES.
# 5) FAÇA UMA FUNÇÃO QUE RECEBE UMA LISTA DE IDADES E RETORNE QUANTOS DESSA LISTA TEM QUE VOTAR OBRIGATÓRIAMENTE.
# (18 E 70)

def checarIdade(idade):
  if idade >= 18:
    return "Maior de idade"
  else:
    return "Menor de idade"

def checarNumero(numero):
  if numero > 0:
    return "Positivo"
  elif numero < 0:
    return "Negativo"
  else:
    return "Neutro"

def calcularMedia(lista):(
  soma = 0
  for element in lista:
    soma += element
  media = soma / len(lista)
  return media

def encontrarMaior(lista):
  maior = lista[0]
  for element in lista:
    if element > maior:
      maior = element
  return maior

def checarVoto(lista):
  qtde_obrigatorios = 0
  for element in lista:
    if element >= 18 and element <= 70:
      qtde_obrigatorios += 1
  return qtde_obrigatorios


# MÓDULO
import numericas
idade = int(input("Digite uma idade: "))
print(numericas.checarIdade(idade=idade))

# APELIDO
import numericas as n
idade = int(input("Digite uma idade: "))
print(n.checarIdade(idade=idade))

# IMPORTANDO FUNÇÕES SELECIONADAS
from numericas import checarIdade, checarNumero
idade = int(input("Digite uma idade: "))
print(checarIdade(idade=idade))
print(checarNumero(numero=idade))

# IMPORTANDO TUDO
from numericas import *
idade = int(input("Digite uma idade: "))
print(checarIdade(idade=idade))
print(checarNumero(numero=idade))

# BIBLIOTECAS

# MATH
import math
print(math.sqrt(81))
print(math.ceil(8.7))
print(math.floor(8.7))


# RANDOM
import random
print(random.randint(a=10, b=100))
lista_de_alunos = ["Job", "Felipe", "Gabriel"]
aluno_corno = random.choice(lista_de_alunos)
print(aluno_corno)



# ATIVIDADE 1
# FAÇA UM PROGRAMA QUE FAZ O COMPUTADOR ESCOLHER UM NÚMERO ALEATÓRIO ENTRE 1 E 100
# E PEDE PARA O USUÁRIO DIGITAR UM NÚMERO EM UM LOOP INFINITO QUE SÓ ACABA SE ELE ACERTAR O NÚMERO SECRETO QUE O COMPUTADOR ESCOLHEU.
# O PROGRAMA DEVE DIZER SE O NÚMERO SECRETO É MAIOR OU MENOR DO QUE O CHUTE DO USUÁRIO.
# ADICIONE UM LIMITE DE  7 TENTATIVAS.
# 7 - Por pouco ein?
# 5/6 - É, bomzin
# 3/4 - Bom pacarai
# 2 - Monstrão ein?
# 1 - Tu é deus né?