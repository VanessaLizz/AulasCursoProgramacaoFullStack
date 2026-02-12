# for AULA 03 - PYTHON: DICIONÁRIOS E CONJUNTOS 

lista_frutas = ["Uva", "Maçã", "Banana", "Melancia"]
tupla_frutas = ("Uva", "Maçã", "Banana", "Melancia")
conjunto_frutas = {"Uva", "Maçã", "Banana", "Melancia"}

# CONJUNTOS
minhas_frutas = {"Uva", "Maçã", "Banana", "Melancia"}
vizinho_frutas = {"Acerola", "Abacaxi", "Uva", "Cabeludinha"}
print(minhas_frutas.intersection(vizinho_frutas))
print(minhas_frutas.difference(vizinho_frutas))
print(minhas_frutas.union(vizinho_frutas))

# DICIONÁRIOS
dados_pessoais = {
  "Nome": "Abel",
  "Idade": 30,
  "Altura": 1.79,
  "Sapato": 42,
  "Habilitado": True,
  "Queima ou nao queima": False,
  "Profissão": "Professor",
  "Frutas Preferidas": ["Abacaxi", "Melancia", "Uva"]

}

if dados_pessoais["Idade"] >= 18:
  print("Maior de idade")


# ATIVIDADE 1
# CRIE UM DICIONÁRIO COM AS INFORMAÇÕES DO SEU PET (SE VOCÊ NÃO TIVER UM PET, INVENTA UM)
# NOME, COR, TAMANHO, PESO, ESPECIE,  RAÇA
pet = {
  "Nome": "Spike",
  "Cor": "Branco",
  "Tamanho": "Médio",
  "Peso": 19.4,
  "Especie": "Cachorro",
  "Raça": "Pitbull"
}
print(pet)

print(f"""
    ===================
    Dados do PET 
    Nome: {pet['Nome']}
    Cor: {pet['Cor']}
    Tamanho: {pet['Tamanho']}
    Peso: {pet['Peso']}Kg
    Especie: {pet['Especie']}
    Raça: {pet['Raça']}
    ===================
""")


# ADICIONANDO VARIÁVEIS
nome = input("Digite o nome do seu pet: ")
peso = float(input("Digite o peso do seu pet: "))

pet = {
  "Nome": nome,
  "Cor": input("Digite a cor do seu pet: "),
  "Tamanho": input("Digite o tamanho do seu pet: "),
  "Peso": peso,
  "Especie": "Cachorro",
  "Raça": "Pitbull"
}
print(pet)

print(f"""
    ===================
    Dados do PET 
    Nome: {pet['Nome']}
    Cor: {pet['Cor']}
    Tamanho: {pet['Tamanho']}
    Peso: {pet['Peso']}Kg
    Especie: {pet['Especie']}
    Raça: {pet['Raça']}
    ===================
""")


# ATIVIDADE 2
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR:
# SEU NOME, IDADE, PESO, ALTURA
# CRIE UM DICIONÁRIO E GUARDE TODAS ESSAS INFORMAÇÕES DENTRO.
# EXIBA O DICIONÁRIO NA TELA.
nome = input("Digite seu nome: ")
idade = int(input("Digite seu idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

pessoa = {
  "Nome": nome,
  "Idade": idade,
  "Peso": peso,
  "Altura": altura
}

print(f"""
    |=-=-=-=-=-=-=-=-==-=-=-=-=-=-=|
             Dados Pessoais
      Nome: {pessoa['Nome']}
      Idade: {pessoa['Idade']} anos
      Peso: {pessoa['Peso']}Kg
      Altura: {pessoa['Altura']}m
    |=-=-=-=-=-=-=-=-==-=-=-=-=-=-=|
""")


# LISTA DE DICIONÁRIOS
lista_de_pessoas = []
for i in range(5):
  nome = input("Digite seu nome: ")
  idade = int(input("Digite seu idade: "))
  peso = float(input("Digite seu peso: "))
  altura = float(input("Digite sua altura: "))

  pessoa = {
    "Nome": nome,
    "Idade": idade,
    "Peso": peso,
    "Altura": altura
  }
  lista_de_pessoas.append(pessoa)
  print(f"{pessoa['Nome']} cadastrado com sucesso")


for elemento in lista_de_pessoas:
  print(f"""
      |=-=-=-=-=-=-=-=-==-=-=-=-=-=-=|
              Dados Pessoais
        Nome: {elemento['Nome']}
        Idade: {elemento['Idade']} anos
        Peso: {elemento['Peso']}Kg
        Altura: {elemento['Altura']}m
      |=-=-=-=-=-=-=-=-==-=-=-=-=-=-=|
  """)


# LISTA DE DICIONÁRIOS PRONTA

filmes = [
    {
        "titulo": "O Poderoso Chefão",
        "diretor": "Francis Ford Coppola",
        "ano": 1972,
        "genero": "Crime",
        "nota": 9.2
    },
    {
        "titulo": "Clube da Luta",
        "diretor": "David Fincher",
        "ano": 1999,
        "genero": "Drama",
        "nota": 8.8
    },
    {
        "titulo": "A Origem",
        "diretor": "Christopher Nolan",
        "ano": 2010,
        "genero": "Ficção Científica",
        "nota": 8.8
    },

    {
        "titulo": "Pulp Fiction",
        "diretor": "Quentin Tarantino",
        "ano": 1994,
        "genero": "Crime",
        "nota": 8.9
    },
    {
        "titulo": "Parasita",
        "diretor": "Bong Joon-ho",
        "ano": 2019,
        "genero": "Drama",
        "nota": 8.6
    }
]

# DESAFIO FINAL
# CONSIDERANDO A LISTA DE FILME ACIMA, FAÇA UM PROGRAMA QUE:
# PEDE PARA O USUÁRIO CADASTRAR MAIS 4 FILMES
# ADICIONA NA LISTA ANTERIOR
# PERCORRA A LISTA ANTERIOR E:
# MOSTRE QUAL O FILME TEM MAIOR NOTA
# MOSTRE QUANTOS FILMES DO GENERO "CRIME" EXISTEM NA LISTA.
filmes = [
    {
        "titulo": "O Poderoso Chefão",
        "diretor": "Francis Ford Coppola",
        "ano": 1972,
        "genero": "Crime",
        "nota": 9.2
    },
    {
        "titulo": "Clube da Luta",
        "diretor": "David Fincher",
        "ano": 1999,
        "genero": "Drama",
        "nota": 8.8
    },
    {
        "titulo": "A Origem",
        "diretor": "Christopher Nolan",
        "ano": 2010,
        "genero": "Ficção Científica",
        "nota": 8.8
    },
    {
        "titulo": "Pulp Fiction",
        "diretor": "Quentin Tarantino",
        "ano": 1994,
        "genero": "Crime",
        "nota": 8.9
    },
    {
        "titulo": "Parasita",
        "diretor": "Bong Joon-ho",
        "ano": 2019,
        "genero": "Drama",
        "nota": 8.6
    }
]

for i in range(4):
    titulo = input("Digite o título do filme: ")
    diretor = input("Digite o diretor do filme: ")
    ano = int(input("Digite o ano do filme: "))
    genero = input("Digite o gênero do filme: ")
    nota = float(input("Digite a nota do filme: "))
    
    novo_filme = {
        "titulo": titulo,
        "diretor": diretor,
        "ano": ano,
        "genero": genero,
        "nota": nota
    }
    filmes.append(novo_filme)
    print("Filme adicionado com sucesso")


filme_maior_nota = filmes[0]
qtde_genero_crime = 0

for element in filmes:
    if element["nota"] > filme_maior_nota["nota"]:
        filme_maior_nota = element
    
    if element["genero"].lower() == "crime":
        qtde_genero_crime += 1

print(f"O filme com maior nota é: {filme_maior_nota['titulo']}, com a nota: {filme_maior_nota['nota']}")

print(f"A quantidade de filmes de crime é: {qtde_genero_crime}")