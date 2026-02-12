# Dracula Theme Official
# Material Icon Theme
# Bracket Pair Color DLW
# indent-rainbow
# Incredibly In Your Face
# vscode-pets



# # Aula 02 - Lógica de Programação: Condicionais

# # Finalizando aula 01:
# # Extensões:
# # - Dracula Theme Official
# # - Material Icon Theme
# # - Bracket Pair Color DLW
# # - indent-rainbow
# # - Incredibly In Your Face
# # - vscode-pets

# # Exibindo informação
# print("Qualquer coisa")


# # CRIANDO VARIÁVEIS
# nome = "Abel"
# idade = 29
# altura = 1.79

# # PADRÃO DE VARIÁVEL
# nomedomeucachorro = "Spike" # PROCURAR AJUDA. CAPS CASE
# nome_do_meu_cachorro = "Spike" # SNAKE CASE
# nomeDoMeuCachorro = "Spike" # CAMEL CASE

# TIPOS DE VARIÁVEIS
# str
# # Significa String, que representa todo tipo de texto em python, ou seja qualquer coisa que esteja entre aspas.
# "Abel"
# "Olá, seja vem vindo"
# "x"
# "066086536954"
# "85985630694"
# "61658070"


# int
# # Significa INTERGER ou Inteiro, são NÚMEROS que não são "quebrados"
# 5
# 1000
# -2
# 0
# 7
# 90
# -10

# float
# # Siginifica flutuante ou seja "quebrado" é o número com a virgula que não programação é o ponto "."
# 1.79
# 9.99
# 1550.40
# -7.7

# bool
# # Significa Boolean, é o verdeiro ou falso, sim ou não, é ou não é, 0 ou 1, ligado ou desligado
# True
# False



# ATIVIDADE 1
# CRIE VARIÁVEIS COM:
# - SOBRENOME
# - SAPATO
# - HABILITADO
# - CASADO
# - TELEFONE
# - NOME
# - IDADE
# - ALTURA
# RESPOSTA:
# sobrenome = "Teixeira"
# sapato = 42
# habilitado = True
# casado = False
# telefone = "085985300694"
# nome = "Abel"
# idade = 29
# altura = 1.79

# CONCATENAÇÃO (JEITO MAIS ANTIGO)
# nome = "Abel"
# idade = 29
# peso = 113.5

# print("Olá",nome,"você tem",idade,"anos e pesa",peso,"kg")

# F-STRING
# nome = "Abel"
# idade = 29
# peso = 113.5

# print(f"Olá {nome} você tem {idade} anos e pesa {peso}kg")

# INPUT
# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# peso = float(input("Digite seu peso: "))

# print(f"Olá {nome} você tem {idade} anos e pesa {peso}kg")

# OPERADORES MATEMÁTICOS BÁSICOS
# n1 = 5
# n2 = 8
# soma = n1 + n2
# subtracao = n1 - n2
# multiplicacao = n1 * n2
# divisao = n1 / n2

# OPERADORES MATEMÁTICOS COMPLEXOS
# n1 = 5
# modulo = n1 % 3
# divisa_inteira = n1 // 2
# potenciacao = n1 ** 2


# ATIVIDADE 2
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR DUAS NOTAS, CALCULA A MÉDIA DESSAS 2 NOTAS E MOSTRA NA TELA O RESULTADO.

# RESULTADO:
 n1 = float(input("Digite a primeira nota: "))
 n2 = float(input("Digite a segunda nota: "))

 m = (n1 + n2) / 2

 print(f'Sua média é: {m}')

# ATIVIDADE 3
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR SEU PESO E SUA ALTURA E CALCULA O IMC.
# FÓRMULA: 
# IMC = peso / (altura x altura)
# MOSTRA O RESULTADO NA TELA.
 peso = float(input("Digite seu peso: "))
 altura = float(input("Digite sua altura: "))

 imc = peso / (altura * altura)

 print(f"Seu IMC é: {imc:.2f}")

# DESAFIO FINAL
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR QUANTO ELE GANHA POR HORA E QUANTAS HORAS ELE TRABALHA NO MÊS:
# SALÁRIO BRUTO - QTDE * VALOR
# DESCONTO DO IMPOSTO DE RENDA - 7.5%
# DESCONTO DO INSS - 8% 
# SALÁRIO LIQUIDO - BRUTO - INSS - IR


# https://notepad.ink/515aula04logica