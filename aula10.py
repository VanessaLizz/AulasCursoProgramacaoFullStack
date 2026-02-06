# AULA 10 - PYTHON: INTERFACE FLET II

# ATIVIDADE REVISÃO
# FAÇA UM PROGRAMA EM FLET QUE PEDE PARA O USUÁRIO DIGITAR SEU PESO E SUA ALTURA E CALCULE SEU IMC E ENTÃO EXIBA NA TELA SEU RESULTADO:
# MENOR QUE 18.5 : BAIXO DO PESO - #fcbd16
# 18.5 A 24.9 : PESO NORMAL - #80bf66
# 25 A 29.9 : EXCESSO DE PESO - #f18815
# 30 A 34.9 : OBESIDADE I - #df1f12
# 35 A 39.9 : OBESIDADE II - #b21d17
# ACIMA DE 40: OBESIDADE III - #801711 


import flet as ft


def main(page: ft.Page):
    def realizarCalculo(e):
        p = float(peso.value.replace(",","."))
        a = float(altura.value.replace(",","."))
        imc = p / a ** 2
        if imc < 18.5:
            resultado.value = f"Abaixo do Peso, com IMC: {imc:.2f}"
            resultado.color = "#fcbd16"
        elif imc <= 24.99:
            resultado.value = f"Peso Normal, com IMC: {imc:.2f}"
            resultado.color = "#80bf66"
        elif imc <= 29.99:
            resultado.value = f"Excesso de Peso, com IMC: {imc:.2f}"
            resultado.color = "#f18815"
        elif imc <= 34.99:
            resultado.value = f"Obesidade I, com IMC: {imc:.2f}"
            resultado.color = "#df1f12"
        elif imc <= 39.99:
            resultado.value = f"Obesidade II, com IMC: {imc:.2f}"
            resultado.color = "#b21d17"
        else:
            resultado.value = f"Obesidade III, com IMC: {imc:.2f}"
            resultado.color = "#801711"
        page.update()

    page.title = "Calculadora de IMC"
    msg = ft.Text(value="Informe seu dados")
    peso = ft.TextField(label="Peso")
    altura = ft.TextField(label="Altura")
    botao = ft.ElevatedButton(text="Calcular", on_click=realizarCalculo)
    resultado = ft.Text(value="")
    page.add(msg, peso, altura, botao, resultado)


ft.app(target=main)



# INTRODUÇÃO A POO
class Telefone():
  def __init__(self, marca:str, modelo:str, cor: str, preco: float, polegadas:float, qtde_cameras:int, armazenamento: int, caneta:bool):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.preco = preco
    self.polegadas = polegadas
    self.qtde_cameras = qtde_cameras
    self.armazenamento = armazenamento
    self.caneta = caneta
  
  def ligar(self):
    return f"O telefone {self.marca} {self.modelo} ligou"
  def desligar(self):
    return f"O telefone {self.marca} {self.modelo} desligou"
  def realizarChamada(self, numero:str):
    return f"O telefone {self.marca} {self.modelo} está realizando uma chamada para o número {numero}"

tel1 = Telefone(marca="Samsung", modelo="S24 Ultra", cor="Azul/Cinza", preco=6000, polegadas=6.2, qtde_cameras=5, armazenamento=512, caneta=True)

outro_telefone = Telefone(marca="Apple", modelo="Iphone 17 PRO MAX", cor="Rosa", preco=14500, polegadas=6.5, qtde_cameras=3, armazenamento=512, caneta=False)

print(tel1.marca)
print(outro_telefone.marca)
print(tel1.ligar())
print(tel1.realizarChamada(numero="85985302658"))
print(outro_telefone.realizarChamada(numero="85985302658"))







# APLICAÇÃO INICIAL
class Carro():
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, preco: float, automatico: bool, placa: str, velocidade_maxima: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco
        self.automatico = automatico
        self.placa = placa
        self.ligado = False
        self.velocidade_atual = 0
        self.velocidade_maxima = velocidade_maxima

    def ligar(self):
        self.ligado = True
        return f"O Carro de placa {self.placa} ligou"

    def desligar(self):
        self.ligado = False
        return f"O Carro de placa {self.placa} desligou"

    def acelerar(self, velocidade: int):
        if self.ligado:
            if self.velocidade_atual + velocidade <= self.velocidade_maxima:
                self.velocidade_atual += velocidade
                return f"O Carro de placa {self.placa} acelerou e está a {self.velocidade_atual}KM/h"
            else:
                self.velocidade_atual = self.velocidade_maxima
                return f"O Carro de placa {self.placa} acelerou e está a {self.velocidade_atual}KM/h (tu vai morrer baitola)"
        else:
            return "Ligue o carro primeiro"

    def freiar(self, velocidade: int):
        return f"O Carro de placa {self.placa} acelerou e está a {velocidade}KM/h"


c1 = Carro(marca="Honda", modelo="Civic", ano=2016, cor="Prata",
           preco=60000, automatico=True, placa="HKO9-532", velocidade_maxima=245)

x = Carro(marca="Fiat", modelo="Uno", ano=2005, cor="Azul", preco=14000,
          automatico=False, placa="OSDQ-F53", velocidade_maxima=150)


print(c1.ligar())
print(c1.acelerar(velocidade=50))
print(c1.acelerar(velocidade=300))
print(c1.desligar())
print(c1.acelerar(velocidade=100))