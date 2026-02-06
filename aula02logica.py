# _ATIVIDADE 03 - LÓGICA DE PROGRAMAÇÃO : LOOP WHILE

# ATIVIDADE REVISÃO
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR QUANTO ELE GANHA POR HORA E QUANTAS HORAS ELE TRABALHA NO MÊS:
# SALÁRIO BRUTO - QTDE * VALOR
# DESCONTO DO IMPOSTO DE RENDA - 7.5%
# DESCONTO DO INSS - 8% 
# SALÁRIO LIQUIDO - BRUTO - INSS - IR
valor_hora = float(input("Digite quanto você ganha por hora: "))
qtde_horas = int(input("Digite quantas horas você trabalha por mês: "))

salario_bruto = valor_hora * qtde_horas
desconto_ir = salario_bruto * 0.075
desconto_inss = salario_bruto * 0.08
salario_liquido = salario_bruto - desconto_ir - desconto_inss

print(f"Salário bruto: {salario_bruto:.2f}")
print(f"Desconto do Imposto de Renda: {desconto_ir:.2f}")
print(f"Desconto do INSS: {desconto_inss:.2f}")
print(f"Salário liquido: {salario_liquido:.2f}")


# OPERADORES DE COMPARAÇÃO
n1 = 5
n2 = 8
print(n1 > n2) #False
print(n1 >= n2) #False
print(n1 < n2) #True
print(n1 <= n2) #True
print(n1 == n2) #False
print(n1 != n2) #True


# CONDICIONAIS
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("JÁ PODE SER PRESO")
else:
    print("VAI PRA FEBEM")

# ATIVIDADE 1
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UM NÚMERO QUALQUER E MOSTRE NO PRINT SE ESSE NÚMERO É POSITIVO OU NEGATIVO.
numero_qualquer = float(input("Digite um número: "))

if numero_qualquer > 0:
  print("POSITIVO")
elif numero_qualquer < 0:
  print("NEGATIVO")
else:
  print("NEUTRO")


# ATIVIDADE 2
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UMA COR DO SEMÁFORO E MOSTRE NO PRINT UMA MENSAGEM RESPECTIVA AS CORES:
# PARE
# ATENÇÃO
# SIGA
cor = input("Digite uma cor do semáforo: ").lower().strip()
#lower() serve para transformar todo o texto em minUSCULOOOO. 
#strip() serve para tirar os espaços de antes ou de depois do que foi digitado.

if cor == "vermelho":
  print("PARE")
elif cor == "amarelo":
  print("ATENÇÃO")
elif cor == "verde":
  print("SIGA")
else:
  print("DIGITA DIREITO BAITOLA.")
# ATIVIDADE 3
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR SUA IDADE E MOSTRE NA TELA SUA FAIXA ETÁRIA:
# - CRIANÇA - ATÉ 12
# - ADOLESCENTE - 13 A 17
# - ADULTO - 18 A 64
# - IDOSO - 65 PRA CIMAidade = int(input("Digite sua idade: "))

if idade <= 12:
  print("CRIANÇA")
elif idade >= 13 and idade <= 17:
  print("ADOLESCENTE")
elif idade >= 18 and idade <= 64:
  print("ADULTO")
else:
  print("IDOSO")

# VERSÃO 2
idade = int(input("Digite sua idade: "))

if idade < 0 or idade > 140:
  print("DIGITA DIREITO BAITOLA.")
elif idade <= 12:
  print("CRIANÇA")
elif idade >= 13 and idade <= 17:
  print("ADOLESCENTE")
elif idade >= 18 and idade <= 64:
  print("ADULTO")
else:
  print("IDOSO")

# VERSÃO 3
idade = int(input("Digite sua idade: "))

if idade < 0 or idade > 140:
  print("DIGITA DIREITO BAITOLA.")
elif idade <= 12:
  print("CRIANÇA")
elif idade <= 17:
  print("ADOLESCENTE")
elif idade <= 64:
  print("ADULTO")
else:
  print("IDOSO")

# ATIVIDADE FINAL
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR SEU PESO E SUA ALTURA, CALCULE SEU IMC E EXIBA EM QUE FAIXA ELE ESTÁ:
# IMC = peso / (altura x altura)
# MENOR QUE 18.5 - BAIXO PESO
# 18.5 A 24.9 - PESO NORMAL
# 25 A 29.9 - EXCESSO DE PESO
# 30 A 34.9 - OBESIDADE I
# 35 A 39.9 - OBESIDADE II
# 40 PRA CIMA - OBESIDADE III