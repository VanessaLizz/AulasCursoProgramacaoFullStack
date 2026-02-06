#AULA 13 - PYTHON: ENCAPSULAMENTO

class Aluno():
    def __init__(self, nome: str, idade: int, email: str, senha: str):
        self.__nome = nome
        self.idade = idade
        self.__email = email
        self.__senha = senha
    
    def verNome(self):
      return self.__nome
  
    def mudarSenha(self):
      senha_atual = input("Digite sua senha atual para trocar a senha: ")
      if senha_atual == self.__senha:
        nova_senha = input("Digite a nova senha: ")
        confimar_senha = input("Digite novamente a nova senha para confirmar: ")
        if confimar_senha == nova_senha:
          self.__senha = nova_senha
          return "Senha alterada com sucesso"
        else:
          return "A senha não foi confirmada, as duas senhas tem que ser iguais."
      else:
        return "Senha atual está errada."
      

    def verEmail(self):
        return self.__email

    def trocarEmail(self, novo_email: str):
        senha_digitada = input("Digite sua senha para poder trocar o email: ")
        if senha_digitada == self.senha:
          if "@" in novo_email:
            self.__email = novo_email
            return "Email trocado com sucesso."
          else:
            return "Email no formato inválido"
        else:
            return "Senha inválida"


aluno1 = Aluno(nome="João", idade=18, email="joao@email.com", senha="123456")


aluno1.idade = "arroz"
aluno1.idade = -5
print(aluno1.idade)

print(aluno1.mudarSenha())
print(aluno1.mudarSenha())
print(aluno1.verSenha())

print(aluno1.trocarEmail(novo_email="x"))
print(aluno1.trocarEmail(novo_email="joaozim_da_tuf@gmail.com"))
print(aluno1.trocarEmail(novo_email="joaozim_da_cearamor@gmail.com"))
print(aluno1.verEmail())

# ATIVIDADE 1

# CRIE UMA CLASSE PARA REPRESENTAR UMA CONTA BANCARIA:
# COM OS ATRIBUTOS:
# TITULAR, NUMERO, AGENCIA, SALDO, SENHA
# E OS MÉTODOS:
# SACAR ( )
# DEPOSITAR ( )
# CHECAR SALDO ( ) 
class Conta():
  def __init__(self, titular:str, numero:str, agencia:str, saldo:float, senha:str):
    self.__titular = titular
    self.__numero = numero
    self.__agencia = agencia
    self.__saldo = saldo
    self.__senha = senha
    
  def getTitular(self):
    return self.__titular
  def getNumero(self):
    return self.__numero
  def getAgencia(self):
    return self.__agencia
  
  def sacar(self, valor:float):
    senha_digitada = input("Digite sua senha para sacar: ")
    if senha_digitada == self.__senha:
      if valor <= self.__saldo:
        self.saldo -= valor
        return f"Saque de R${valor} realizado com sucesso"
      else:
        return "Saldo insuficiente"
    else:
      return "Senha inválida"

  def depositar(self, valor:float):
    senha_digitada = input("Digite sua senha para sacar: ")
    if senha_digitada == self.__senha:
        self.saldo += valor
        return f"Deposito de R${valor} realizado com sucesso"
    else:
      return "Senha inválida"
  
  def checarSaldo(self):
    senha_digitada = input("Digite sua senha para sacar: ")
    if senha_digitada == self.__senha:
        return f"Seu saldo atual é: {self.__saldo}"
    else:
      return "Senha inválida"



# PROJETO DA AULA 13
class Cliente():
  def __init__(self, nome,idade):
    self.nome = nome
    self.idade = idade
  
class Quarto():
  ...

class Motel():
  def __init__(self, nome:str, cnpj:str, endereco:str):
    self.nome = nome
    self.cnpj = cnpj
    self.endereco = endereco
    self.lista_de_clientes = []
    self.lista_de_quartos = []
    
  def cadastrarCliente(self):
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    novo_cliente = Cliente(nome=nome, idade=idade)
    self.lista_de_clientes.append(novo_cliente)
    return "Cliente cadastrado com sucesso."