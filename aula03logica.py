# iAULA 04 - LÓGICA DE PROGRAMAÇÃO
# ATIVIDADE REVISÃO
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR SEU PESO E SUA ALTURA, CALCULE SEU IMC E EXIBA EM QUE FAIXA ELE ESTÁ:
# IMC = peso / (altura x altura)
# MENOR QUE 18.5 - BAIXO PESO
# 18.5 A 24.9 - PESO NORMAL
# 25 A 29.9 - EXCESSO DE PESO
# 30 A 34.9 - OBESIDADE I
# 35 A 39.9 - OBESIDADE II
# 40 PRA CIMA - OBESIDADE III
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
  print("Abaixo do peso")
elif imc <= 24.9:
  print("Peso normal")
elif imc <= 29.9:
  print("Excesso de peso")
elif imc <= 34.9:
  print("OBESIDADE I")
elif imc <= 39.9:
  print("OBESIDADE II")
else:
  print("OBESIDADE III")



# LOOP DE REPETIÇÃO WHILE
contador = 1

while contador <= 10:
  print("Estou contando", contador)
  contador += 1
print("Fim do loop")


# APLICANDO WHILE
contador = 1
soma = 0

while contador <= 4:
  nota = float(input("Digite um nota: "))
  soma += nota
  contador += 1
media = soma / 4


# ATIVIDADE 1
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR A IDADE DE 8 PESSOAS, CALCULE A MÉDIA DAS IDADES.
cont = 1
soma = 0

while cont <= 8:
  idade = int(input("Digite uma idade"))
  soma += idade
  cont += 1

media = soma / 8
print(f"A média das idades é: {media:.2f}")
 

# ATIVIDADE 2
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR A NOTA FINAL DE 6 ALUNOS E CONTE QUANTOS ALUNOS DESSES 6 FORAM APROVADOS (CONSIDERE A MÉDIA DE APROVAÇÃO: 7)
count = 1
qtde_alunos_aprovados = 0

while count <= 6:
  nota_final = float(input("Digite a nota final: "))
  if nota_final >= 7:
    qtde_alunos_aprovados += 1
  count += 1

print(f"{qtde_alunos_aprovados} foram aprovados")


# WHILE TRUE
while True:
  menu = input("""
  ====================
  Escolha uma opção:
  1 - Adicionar produto
  2 - Sair
""")
  if menu == "1":
    print('Finge que eu to adicionando um produto')
  elif menu == "2":
    break
  else:
    print("DIGITA DIREITO BAITOLA.")

print("saiu do loop")

# DESAFIO FINAL
# VOCÊS FORAM CONTRATADOS PARA DESENVOLVER UM SOFTWARE PARA UMA LOJA DE DOCES!
# O DONO DESEJA REGISTRAR TODAS AS VENDAS DO DIA, COM:
# NOME DO CLIENTE, PRODUTO COMPRADO, VALOR DA COMPRA
# E NO FINAL DO DIA ELE DESEJA FAZER UM SORTEIO PARA DAR UM KIT DE 50 DOCINHOS PARA UM DOS CLIENTES DO DIA. DESENVOLVA ESSE SISTEMA.
# OBS: SÓ PARTICIPAM DO SORTEIO CLIENTES COM COMPRAS ACIMA DE 50 REAIS E NO FINAL MOSTRAR QUAL FOI O PRODUTO MAIS VENDIDO DO DIA.