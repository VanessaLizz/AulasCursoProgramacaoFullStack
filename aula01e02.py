# AULA 01 - PYTHON: REVISÃO GERAL

# REVISÃO WHILE
cont = 1
while cont <= 10:
  nota = float(input("Digite uma nota: "))
  cont += 1
print("Fim do loop")

# REVISÃO WHILE TRUE
soma = 0
quantidade_notas = 0

while True:
  menu = input("""
    Escolha uma opção:
    1 - Pedir nota
    2 - Calcular média
    3 - Simbora aviões
  """)
  if menu == "1":
    nota = float(input("Digite uma nota: "))
    soma += nota
    quantidade_notas += 1
  elif menu == "2":
    media = soma / quantidade_notas
    print(f"A média é: {media}")
  elif menu == "3":
    break
  else:
    print("DIGITA DIREITO BAITOLA.")
print("Fim do loop")


# FOR 
for i in range(5):
  nota = float(input(f"Digite uma nota: "))
print("Fim do loop")


# ATIVIDADE 1
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR A IDADE DE 6 PESSOAS, CALCULE E MOSTRE NA TELA A MÉDIA DAS IDADES. (TREINEM O FOR)
soma = 0
for i in range(6):
  idade = int(input("Digite a idade: "))
  soma += idade
media = soma / 6
print(f"A média é: {media}")

# ATIVIDADE 2
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR A NOTA DE 5 ALUNOS E CONTE QUANTOS DESSES FORAM APROVADO (CONSIDERE A MÉDIA 7)
qtde_aprovados = 0
for i in range(5):
  nota = float(input("Digite uma nota: "))
  if nota >= 7:
    qtde_aprovados += 1
print(f"A quantidade de alunos aprovados foi: {qtde_aprovados}")


# FOR IN
nome = "abel"
qtde_de_a = 0
for letra_da_vez in nome.lower():

  if letra_da_vez in "aâãáà":
    qtde_de_a += 1 

# ATIVIDADE 3
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR SEU NOME E CONTE QUANTAS VOGAIS TEM NO SEU NOME.
nome = input("Digite seu nome: ").lower().strip()
qtde_vogais = 0
vogais = "aeiouáàâãéèêíóôõúü"

for element in nome:
  if element in vogais:
    qtde_vogais+=1
print(f"A quantidade de vogais do seu nome é: {qtde_vogais}")

# CONTE TAMBÉM QUANTAS CONSOANTES TEM NESSE NOME
nome = input("Digite seu nome: ").lower().strip()
qtde_vogais = 0
qtde_consoantes = 0
vogais = "aeiouáàâãéèêíóôõúü"
consoantes = "bcdfghjklmnpqrstvwxyzçñ"
for element in nome:
  if element in vogais:
    qtde_vogais+=1
  elif element in consoantes:
    qtde_consoantes += 1
print(f"A quantidade de vogais so seu nome é: {qtde_vogais}")
print(f"A quantidade de vogais: {quantidade_de_consoantes}")


# DESAFIO FINAL
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR SUA SENHA E CONTE:
# QUANTAS LETRAS MINUSCULAS
# QUANTAS LETRAS MAIUSCULAS
# QUANTOS NÚMEROS
# QUANTOS CARACTERES ESPECIAIS
# QUANTOS CARACTERES TOTAIS
senha = input("Digite sua senha: ")
qtde_maiusculas = 0
qtde_minusculas = 0
qtde_numeros = 0
qtde_especiais = 0
qtde_total = len(senha)

todas_minusculas = "abcdedfgihjklmnopqrsvtuxywzçáàâãéèêíóôõú"
todas_maiusculas = todas_minusculas.upper()
todos_numeros = "0123456789"


for element in senha:
  if element in todas_minusculas:
    qtde_minusculas += 1
  elif element in todas_maiusculas:
    qtde_maiusculas += 1
  elif element in todos_numeros:
    qtde_numeros += 1
  else:
    qtde_especiais += 1

print(f"""
      Relatório da senha:
      Quantidade de letras maiúsculas: {qtde_maiusculas}
      Quantidade de letras minúsculas: {qtde_minusculas}
      Quantidade de números: {qtde_numeros}
      Quantidade de caracteres especiais: {qtde_especiais}
      Quantidade de caracteres gerais: {qtde_total}
""")


# AULA 02 

# '''FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR A IDADE DE MAIS 5 PESSOAS E ADICIONE NESSA LISTA.
# PERCORRA A LISTA E :
# - MÉDIA DAS IDADES
# - MAIS VELHA
# - MAIS NOVA
# - QUANTAS SÃO MAIORES DE IDADES
# - QUANTOS SÃO MENORES DE IDADES'''

idades = [30, 43, 59, 14, 10]
for i in range(5):
    idade = int(input(f'Digite a {i + 1}ª idade:'))
    idades.append(idade)
media = sum(idades)/len(idades)
mais_velha = max(idades)
mais_nova = min(idades)
qtd_maiores = 0
qtd_menores = 0
for i in idades:
    if i >= 18:
        qtd_maiores += 1
    else:
        qtd_menores += 1

print(f'A media das idades é {media} anos.')
print(f'A pessoa mais nova tem {mais_nova} anos.')
print(f'A pessoa mais velha tem {mais_velha} anos.')
print(f'Temos {qtd_maiores} maiores de idade.')
print(f'Temos {qtd_menores} menores de idade.')

#exercicio resolvido pelo professor
idades = [30, 43, 59, 14, 10]

for i in range(5):
  nova_idade = int(input("Digite uma nova idade: "))
  idades.append(nova_idade)

soma = 0
mais_velho = idades[0]
mais_novo = idades[0]
qtde_maiores_idade = 0
qtde_menores_idade = 0
for elemento in idades:
  soma += elemento
  if elemento > mais_velho:
    mais_velho = elemento
  
  if elemento < mais_novo:
    mais_novo = elemento
    
  if elemento >= 18:
    qtde_maiores_idade += 1
  else:
    qtde_menores_idade += 1

media = soma / len(idades)

print(f"""
    Relatório das idades
    Média das idades: {media}
    Idade do mais velho: {mais_velho}
    Idade do mais novo: {mais_novo}
    Quantidade de maiores de idade: {qtde_maiores_idade}
    Quantidade de menores de idade: {qtde_menores_idade}
""")