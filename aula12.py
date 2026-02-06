# AULA 12 - PYTHON: POO II: HERANÇA E POLIMORFISMO


# ATIVIDADE REVISÃO
# CRIE UMA CLASSE PARA REPRESENTAR UM CACHORRO COM OS ATRIBUTOS:
# NOME, RAÇA, COR, PESO, IDADE, PEDIGREE
# E OS MÉTODOS:
# ACORDAR( )
# DORMIR ( )
# COMER ( )
# LATIR ( )
# PEGAR_BOLINHA ( )

# CRIE UMA CLASSE PARA REPRESENTAR UM GATO COM OS ATRIBUTOS:
# NOME, RAÇA, COR, PESO, IDADE, CASTRADO
# E OS MÉTODOS:
# ACORDAR( )
# DORMIR ( )
# COMER ( )
# MIAR ( )
# AMASSAR_PAOZINHO ( )

# CRIE UMA CLASSE PARA REPRESENTAR UM PASSARO COM OS ATRIBUTOS:
# NOME, RAÇA, COR, PESO, IDADE
# E O MÉTODOS:
# ACORDAR( )
# DORMIR ( )
# COMER ( )
# VOAR ( )

# MÉTODO MÓ PAIA
class Cachorro():
  def __init__(self, nome:str, raca:str, cor:str, idade:int, peso:float, pedigree:bool):
    self.nome = nome
    self.raca = raca
    self.cor = cor
    self.idade = idade
    self.peso = peso
    self.pedigree = pedigree
    self.acordado = True  
  def acordar(self):
    if not self.acordado:
      self.acordado = True
      return f"O {self.nome} acordou"
    else:
      return "Não é possível acordar pois já está acordado"
  def dormir(self):
    if self.acordado:
      self.acordado = False
      return f"O {self.nome} dormiu"
    else:
      return "Não é possível dormir pois já está dormindo"
  def comer(self, alimento:str):
    if self.acordado:
      return f"O {self.nome} comeu {alimento}"
    else:
      return "Não é possível comer pois está dormindo"
  def latir(self):
    if self.acordado:
      return "Au au"
    else:
      return "Não é possível latir pois já está dormindo"
  def pegar_bolinha(self):
    if self.acordado:
      return f"{self.nome} foi pegar a bolinha"
    else:
      return "Não é possível pegar a bolinha pois está dormindo"

class Gato():
  def __init__(self, nome:str, raca:str, cor:str, idade:int, peso:float, castrado:bool):
    self.nome = nome
    self.raca = raca
    self.cor = cor
    self.idade = idade
    self.peso = peso
    self.castrado = castrado
    self.acordado = True  
  def acordar(self):
    if not self.acordado:
      self.acordado = True
      return f"O {self.nome} acordou"
    else:
      return "Não é possível acordar pois já está acordado"
  def dormir(self):
    if self.acordado:
      self.acordado = False
      return f"O {self.nome} dormiu"
    else:
      return "Não é possível dormir pois já está dormindo"
  def comer(self, alimento:str):
    if self.acordado:
      return f"O {self.nome} comeu {alimento}"
    else:
      return "Não é possível comer pois está dormindo"
  def miar(self):
    if self.acordado:
      return "Miauuuuuuuuu"
    else:
      return "Não é possível miar pois já está dormindo"
  def amassa_paozinho(self):
    if self.acordado:
      return f"{self.nome} amassou pãozinho"
    else:
      return "Não é possível amassar pãozinho pois está dormindo"

class Passaro():
  def __init__(self, nome:str, raca:str, cor:str, idade:int, peso:float):
    self.nome = nome
    self.raca = raca
    self.cor = cor
    self.idade = idade
    self.peso = peso
    self.acordado = True  
  def acordar(self):
    if not self.acordado:
      self.acordado = True
      return f"O {self.nome} acordou"
    else:
      return "Não é possível acordar pois já está acordado"
  def dormir(self):
    if self.acordado:
      self.acordado = False
      return f"O {self.nome} dormiu"
    else:
      return "Não é possível dormir pois já está dormindo"
  def comer(self, alimento:str):
    if self.acordado:
      return f"O {self.nome} comeu {alimento}"
    else:
      return "Não é possível comer pois está dormindo"
  def voar(self):
    if self.acordado:
      return f"{self.nome} voou"
    else:
      return "Não é possível voar pois está dormindo"

doguim = Cachorro(nome="Spike", raca="Pitbull", cor="Preto", idade=4, peso=28.6, pedigree=True)

gatim = Gato(nome="Floquinho", raca="Angorá", cor="Branco", idade=2, peso=1.2, castrado=False)

passarim = Passaro(nome="Piu piu", raca="Canário", cor="Amarelo", idade=3, peso=0.4)

print(doguim.acordar()) # vai dar erro
print(doguim.dormir())
print(doguim.comer(alimento="Carne")) # vai dar erro
print(doguim.acordar())
print(doguim.comer(alimento="Carne"))
print(doguim.latir())
print(doguim.pegar_bolinha())


print(gatim.acordar()) # vai dar erro
print(gatim.dormir())
print(gatim.comer(alimento="Peixe")) # vai dar erro
print(gatim.acordar())
print(gatim.comer(alimento="Peixe"))
print(gatim.miar())
print(gatim.amassa_paozinho())


print(passarim.acordar()) # vai dar erro
print(passarim.dormir())
print(passarim.comer(alimento="Alpiste")) # vai dar erro
print(passarim.acordar())
print(passarim.comer(alimento="Alpiste"))
print(passarim.voar())

# USANDO HERANÇA E POLIMORFISMO

# MAIN.PY
from Animais.cachorro import *
from Animais.gato import *
from Animais.passaro import *

doguim = Cachorro(nome="Spike", raca="Pitbull", cor="Preto", idade=4, peso=28.6, pedigree=True)
gatim = Gato(nome="Floquinho", raca="Angorá", cor="Branco", idade=2, peso=1.2, castrado=False)
passarim = Passaro(nome="Piu piu", raca="Canário", cor="Amarelo", idade=3, peso=0.4)

print(doguim.acordar())  # vai dar erro
print(doguim.dormir())
print(doguim.comer(alimento="Carne"))  # vai dar erro
print(doguim.acordar())
print(doguim.comer(alimento="Carne"))
print(doguim.emitirSom())
print(doguim.pegar_bolinha())

print(gatim.acordar())  # vai dar erro
print(gatim.dormir())
print(gatim.comer(alimento="Peixe"))  # vai dar erro
print(gatim.acordar())
print(gatim.comer(alimento="Peixe"))
print(gatim.emitirSom())
print(gatim.amassa_paozinho())

print(passarim.acordar())  # vai dar erro
print(passarim.dormir())
print(passarim.comer(alimento="Alpiste"))  # vai dar erro
print(passarim.acordar())
print(passarim.comer(alimento="Alpiste"))
print(passarim.voar())


# ANIMAIS/ANIMAL.PY
class Animal():
    def __init__(self, nome: str, raca: str, cor: str, idade: int, peso: float):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.peso = peso
        self.acordado = True

    def acordar(self):
        if not self.acordado:
            self.acordado = True
            return f"O {self.nome} acordou"
        else:
            return "Não é possível acordar pois já está acordado"

    def dormir(self):
        if self.acordado:
            self.acordado = False
            return f"O {self.nome} dormiu"
        else:
            return "Não é possível dormir pois já está dormindo"

    def comer(self, alimento: str):
        if self.acordado:
            return f"O {self.nome} comeu {alimento}"
        else:
            return "Não é possível comer pois está dormindo"

    def emitirSom(self):
        if self.acordado:
            return "Som indefinido"
        else:
            return "Não é possível emitir som pois já está dormindo"
 
# ANIMAIS/CACHORRO.PY
from Animais.animal import *
class Cachorro(Animal):
    def __init__(self, nome, raca, cor, idade, peso, pedigree: bool):
        super().__init__(nome, raca, cor, idade, peso)
        self.pedigree = pedigree

    def emitirSom(self):
        if self.acordado:
            return "Au au"
        else:
            return "Não é possível latir pois já está dormindo"

    def pegar_bolinha(self):
        if self.acordado:
            return f"{self.nome} foi pegar a bolinha"
        else:
            return "Não é possível pegar a bolinha pois está dormindo"


# ANIMAIS/GATO.PY
from Animais.animal import *
class Gato(Animal):
    def __init__(self, nome, raca, cor, idade, peso, castrado: bool):
        super().__init__(nome, raca, cor, idade, peso)
        self.castrado = castrado

    def emitirSom(self):
        if self.acordado:
            return "Miauuuuuuuuu"
        else:
            return "Não é possível miar pois já está dormindo"

    def amassa_paozinho(self):
        if self.acordado:
            return f"{self.nome} amassou pãozinho"
        else:
            return "Não é possível amassar pãozinho pois está dormindo"


# ANIMAIS/PASSARO.PY
from Animais.animal import *
class Passaro(Animal):
    def __init__(self, nome, raca, cor, idade, peso):
        super().__init__(nome, raca, cor, idade, peso)

    def voar(self):
        if self.acordado:
            return f"{self.nome} voou"
        else:
            return "Não é possível voar pois está dormindo"


# ATIVIDADE FINAL 
# CRIE UMA CLASSE PAI PARA REPRESENTAR UM VEÍCULO
# COM OS ATRIBUTOS: 
# MARCA, MODELO, PLACA, COR, PREÇO, ANO, VELOCIDADE_MAXIMA
# E OS ATRIBUTOS INTERNOS:
# LIGADO, VELOCIDADE_ATUAL
# E OS MÉTODOS:
# LIGAR ( )
# DESLIGAR ( )
# ACELERAR ( )
# FREIAR ( )
# BUZINAR ( )

# CRIE UMA CLASSE FILHA PARA REPRESENTAR UM CARRO, ADICIONE OS ATRIBUTOS:
# AR_CONDICIONADO, QTDE_PORTAS
# E OS MÉTODOS:
# LIGAR_AR( )
# DESLIGAR( )
# SUBIR_VIDRO( )
# BAIXAR_VIDRO( )

# CRIE UMA CLASSE FILHA PARA REPRESENTAR UMA MOTO, ADICIONE O ATRIBUTO: CILINDRADAS
# E ADICIONE O MÉTODO:
# EMPINAR_PNEU( )

# CRIE A CLASSE FILHA PARA REPRESENTAR UM NÁVIO (NAVIO NÃO TEM ACENTO), NÃO ADICIONE NENHUM ATRIBUTO, MAS ADICIONE O MÉTODO:
# ANCORAR( )
# DESANCORAR( )

# EM TODAS AS CLASSES FILHAS, POLIMORFISE A BUZINA.

# NO FINAL INSTANCIE:
# 1 CARRO
# 1 MOTO
# 1 NÁVIO (NAVIO NÃO TEM ACENTO)
# 1 AVIÃO
# E TESTE TODOS OS MÉTODOS.