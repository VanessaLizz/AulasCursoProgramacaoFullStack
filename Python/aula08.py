# AULA 08 - PYTHON: REVISÃO GERAL

# ATIVIDADE 1
# DADO A LISTA:
# idades = [20, 30, 10]
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR 5 IDADES E ADICIONA ELAS NA LISTA EXISTENTE
# DEPOIS PERCORRA ESSA LISTA E:
# [x] CONTE QUANTAS PESSOAS SÃO MAIORES DE IDADE
# [x] CONTE QUANTAS PESSOAS SÃO MENORES DE IDADE
# [x] MOSTRE O MAIS VELHO
# [x] MOSTRE O MAIS NOVO
# [x] CALCULE A MÉDIA DAS IDADES
# E EXIBA NA TELA SE A MÉDIA DAS IDADES É:
# INFANTIL - 0 A 12 ANOS
# JOVEM - 13 A 20 ANOS
# ADULTO - 21 A 64 ANOS
# IDOSO - 65 PRA CIMA

# MODO NORMAL
idades = [20, 30, 10]

for i in range(5):
  nova_idade = int(input("Digite uma idade: "))
  idades.append(nova_idade)


qtde_maiores_idade = 0
qtde_menores_idade = 0
for element in idades:
  if element >= 18:
    qtde_maiores_idade += 1
  else:
    qtde_menores_idade += 1

mais_velho = idades[0]
mais_novo = idades[0]
for element in idades:
  if element > mais_velho:
    mais_velho = element
  if element < mais_novo:
    mais_novo = element

soma = 0
for element in idades:
  soma += element
media = soma / len(idades)

  
print(f"A Quantidade de pessoas maiores de idade é: {qtde_maiores_idade}")
print(f"A Quantidade de pessoas menores de idade é: {qtde_menores_idade}")
print(f"A idade do mais velho é: {mais_velho}")
print(f"A idade do mais novo é: {mais_novo}")
print(f"A média das idades é: {media}")
if media >= 0 and media <= 12:
  print("Infantil")
elif media <= 20:
  print("Jovem")
elif media <= 64:
  print("Adulto")
else:
  print("Idoso")



# MODO AVANÇADO
idades = [20, 30, 10]

for i in range(5):
  nova_idade = int(input("Digite uma idade: "))
  idades.append(nova_idade)

qtde_maiores_idade = 0
qtde_menores_idade = 0
mais_velho = max(idades)
mais_novo = min(idades)
for element in idades:
  if element >= 18:
    qtde_maiores_idade += 1
  else:
    qtde_menores_idade += 1
media = sum(idades) / len(idades)

faixa_etaria = ""
if media >= 0 and media <= 12:
  faixa_etaria = "Infantil"
elif media <= 20:
    faixa_etaria = "Jovem"
elif media <= 64:
    faixa_etaria = "Adulto"
else:
    faixa_etaria = "Idoso"

print(f"""
      A Quantidade de pessoas maiores de idade é: {qtde_maiores_idade}
      A Quantidade de pessoas menores de idade é: {qtde_menores_idade}
      A idade do mais velho é: {mais_velho}
      A idade do mais novo é: {mais_novo}
      A média das idades é: {media}
      A faixa etária das idades é: {faixa_etaria}
      """)

# ATIVIDADE 2
# FAÇA UM PROGRAMA DE CADASTRO DE FILMES (PARA UMA LOCADORA)
# COM O MENU:
# 1 - CADASTRAR FILME
# 2 - VER TODOS OS FILMES
# 3 - EXCLUIR FILME
# 4 - FILTRAR FILME POR GÊNERO
# 0 - SAIR
# CADA FILME VAI TER:
# TÍTULO, ANO, GÊNERO, FAIXA_ETARIA

locadora = []
while True:
    menu = input("""
    1 - CADASTRAR FILME
    2 - VER TODOS OS FILMES
    3 - EXCLUIR FILME
    4 - FILTRAR FILME POR GÊNERO
    0 - SAIR      
  """)
    match menu:
      case "1":
        titulo = input("Digite o título do filme: ")
        while True:
          ano = int(input("Digite o ano do filme: "))
          if ano < 1888:
            print("Digite um ano válido")
          else:
            break
        genero = input("Digite o gênero do filme: ")
        faixa_etaria = int(input("Digite a idade minima do filme: "))
        
        novo_filme = {
          "Título": titulo,
          "Ano": ano,
          "Gênero": genero,
          "Faixa": faixa_etaria
        }
        locadora.append(novo_filme)
        print("Filme cadastrado com sucesso.")
      case "2":
        if len(locadora) == 0:
          print("Nenhum filme cadastrado.")
        else:
          for element in locadora:
            print(f"{element['Título']} - {element['Gênero']}")
      case "3":
        filme_excluido = input("Digite o nome do filme que você deseja excluir: ")
        qtde_encontrados = 0
        for element in locadora:
          if element["Título"] == filme_excluido:
            locadora.remove(element)
            qtde_encontrados += 1
            print("Filme removido com sucesso.")
        if qtde_encontrados == 0:
          print("Nenhum resultado encontrado.")
      case "4":
        genero_escolhido = input("Digite o gênero que você deseja filtrar: ")
        qtde_encontrados = 0
        for element in locadora:
          if element["Gênero"] == genero_escolhido:
            qtde_encontrados += 1
            print(f"{element['Título']} - {element['Gênero']}")
        if qtde_encontrados == 0:
          print("Nenhum resultado encontrado.")
      case "0":
        break
      case _:
        print("Opção inválida, escolha um número válido")