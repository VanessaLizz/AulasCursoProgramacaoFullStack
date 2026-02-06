# AULA 11 - PYTHON: INTRODUÇÃO A POO

# EXEMPLO 1
class Gato():
  def __init__(self, nome:str, raca:str, cor:str, idade:int, peso:float, castrado:bool):
    self.nome = nome
    self.raca = raca
    self.cor = cor
    self.idade = idade
    self.peso = peso
    self.castrado = castrado
  def mostrarInfos(self):
    return f""""
    Nome: {self.nome}
    Raça: {self.raca}
    Cor: {self.cor}
    Idade: {self.idade}
    Peso: {self.peso}
    Castrado: {self.castrado}
  """

gato1 = Gato(nome="Xanim", raca="Persa", cor="Bege", idade=4, peso=2.9, castrado=False)
outro_gato = Gato(nome="Abel", raca="Humano", cor="Branco", idade=30, peso=115, castrado=False)

print(gato1.nome)
print(outro_gato.raca)
print(gato1.mostrarInfos())
print(outro_gato.mostrarInfos())

# EXERCICIO 1
# FAÇA UM CLASSE PARA REPRESENTAR UM FUNCIONARIO, COM OS ATRIBUTOS:
# NOME, CPF, TELEFONE, SALARIO, SETOR(ÁREA DE ATUAÇÃO), CARGO.

# INSTANCIE 3 FUNCIONARIO
# MOSTRE NA TELA O NOME E O CARGO DO SEGUNDO FUNCIONARIO
# MOSTRE TODAS AS INFORMAÇÕES DO 3° FUNCIONARIO
# CHEQUE SE O PRIMEIRO FUNCIONARIO GANHA ACIMA DE DOIS SALÁRIOS MINIMOS.

class Funcionario():
  def __init__(self, nome:str, cpf:str, telefone: str, salario:float, setor:str, cargo:str):
    self.nome = nome
    self.cpf = cpf
    self.telefone = telefone
    self.salario = salario
    self.setor = setor
    self.cargo = cargo
  def monstrarInfos(self):
    return f"""
    DADOS DO FUNCIONÁRIO
    Nome: {self.nome}
    CPF: {self.cpf}
    Telefone: {self.telefone}
    Salário: {self.salario}
    Setor: {self.setor}
    Cargo: {self.cargo}
  """
  def checarSalario(self):
    if self.salario > 1518 * 2:
      return f"O funcionário {self.nome} ganha acima de 2 salários minimos"
    else:
      return f"O funcionário {self.nome} ganha abaixo de 2 salários minimos"

funcionario1 = Funcionario(nome="João", cpf="03216974155", telefone="8595632675", salario=2900, setor="Financeiro", cargo="Analista")

funcionario2 = Funcionario(nome="Maria", cpf="85236971123", telefone="85696548322", salario=6700, setor="T.I", cargo="Desenvolvedora Pleno")

funcionario3 = Funcionario(nome="Pedro", cpf="85632145698", telefone="859856326245", salario=1518, setor="Deposito", cargo="Repositor")

print(funcionario2.nome, funcionario2.cargo)

print(funcionario3.monstrarInfos())

print(funcionario1.checarSalario())
print(funcionario2.checarSalario())
print(funcionario3.checarSalario())


# ATIVIDADE 1
# CRIE UMA CLASSE PARA REPRESENTAR UMA CONTA BANCÁRIA COM OS ATRIBUTOS:
# CONTA, AGENCIA, PROPRIETARIO, SALDO 
# E OS MÉTODOS:
# SACAR ( )
# DEPOSITAR( )
# CHECAR SALDO ( )
# INSTANCIE 1 CONTA E TESTE TODOS OS MÉTODOS

class ContaBancaria():
  def __init__(self, conta:str, agencia:str, titular:str, saldo:float):
    self.conta = conta
    self.agencia = agencia
    self.titular = titular
    self.saldo = saldo
  
  def sacar(self, valor:float):
    if valor > 0:
      if valor <= self.saldo:
        self.saldo -= valor
        return f"Saque no valor de R${valor} realizado com sucesso."
      else:
        return "Saldo insuficiente"
    else:
      return "Valor mínimo para saque: R$ 1.00"
  def depositar(self, valor:float):
    if valor > 0:
      self.saldo += valor
      return f"Deposito de R${valor} realizado com sucesso"
    else:
      return "Valor mínimo para o deposito é: R$ 1.00"
  
  def checarSaldo(self):
    return f"Seu saldo atual é {self.saldo}"

conta1 = ContaBancaria(conta="0001", agencia="0256-51", titular="João", saldo=1000)

print(conta1.sacar(valor=5000))
print(conta1.sacar(valor=-10))
print(conta1.sacar(valor=250))

print(conta1.depositar(valor=-1))
print(conta1.depositar(valor=500))

print(conta1.checarSaldo())

# DESAFIO FINAL
# FAÇA UMA CLASSE PARA REPRESENTAR UM TAMAGOTCHI (POU) 
# ELE VAI TER OS ATRIBUTOS:
# NOME, ESPECIE, VIDA_MAXIMA, ENERGIA_MAXIMA, SACIEDADE
# E OS MÉTODOS:
# BRINCAR ( ) - GASTA ENERGIA DIMINUI A SACIEDADE 
# COMER ( )  - AUMENTA A SACIEDADE E RECUPERA ENERGIA E VIDA
# LUTAR ( ) - GASTA ENERGIA E VIDA E DIMINUI A SACIDADE
# DORMIR ( ) - REGENERA A ENERGIA.

class Tamagotchi():
    def __init__(self, nome: str, especie: str, vida_maxima: int, energia_maxima: int, saciedade_maxima: int):
        self.nome = nome
        self.especie = especie
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.energia_maxima = energia_maxima
        self.energia_atual = energia_maxima
        self.saciedade_maxima = saciedade_maxima
        self.saciedade_atual = saciedade_maxima

    def brincar(self):
        if self.vida_atual > 0:
            if self.energia_atual > 10:
                if self.saciedade_atual > 5:
                    self.energia_atual -= 10
                    self.saciedade_atual -= 5
                    return f"O {self.nome} brincou"
                else:
                    return "Vai dar de comer pro bixo man"
            else:
                return "Energia insuficiente"
        else:
            return "Não da pra brincar com o bixim morto"

    def comer(self):
        if self.vida_atual > 0:
            if self.vida_atual + 20 <= self.vida_maxima:
                if self.energia_atual + 15 <= self.energia_maxima:
                    if self.saciedade_atual + 10 <= self.saciedade_maxima:
                        self.energia_atual += 15
                        self.saciedade_atual += 10
                        self.vida_atual += 20
                        return f"O {self.nome} comeu"
                    else:
                        self.energia_atual += 15
                        self.saciedade_atual = self.saciedade_maxima
                        self.vida_atual += 20
                        return f"O {self.nome} comeu"
                else:
                    self.energia_atual = self.energia_maxima
                    self.saciedade_atual += 10
                    self.vida_atual += 20
                    return f"O {self.nome} comeu"
            else:
                self.energia_atual += 15
                self.saciedade_atual += 10
                self.vida_atual = self.vida_maxima
                return f"O {self.nome} comeu"
        else:
            return "Não da pra alimentar o bixim morto"

    def lutar(self):
        if self.vida_atual > 0:
            if self.energia_atual > 10:
                if self.saciedade_atual > 5:
                    if self.vida_atual > 15:
                        self.energia_atual -= 10
                        self.saciedade_atual -= 5
                        self.vida_atual -= 15
                        return f"O {self.nome} brincou"
                    else:
                        return "Não é possíve lutar pois a vida está muito baixa"
                else:
                    return "Vai dar de comer pro bixo man"
            else:
                return "Energia insuficiente"
        else:
            return "Não da pra brincar com o bixim morto"

    def dormir(self):
        if self.vida_atual > 0:
          if self.energia_atual + 15 <= self.energia_maxima:
            self.energia_atual += 15
            return f"O {self.nome} dormiu"
                    
          else:
            self.energia_atual = self.energia_maxima
            return f"O {self.nome} dormiu"
        else:
            return "Não da pra dormir estando morto"