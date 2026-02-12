# AULA 09 - PYTHON: INTERFACE FLET I
# https://mybrandnewlogo.com/pt/gerador-de-paleta-de-cores

# RECEITA DE BOLO


import flet as ft
def main(pagina:ft.Page):
  ...
ft.app(target=main)



# TEXT
import flet as ft
def main(pagina:ft.Page):
  pagina.title = "Aula 09 - Flet"
  mensagem = ft.Text(value="Meu Primeiro código Flet", color="#62afff", size=60)
  pagina.add(mensagem)
ft.app(target=main)


# TEXTFIELD E BUTTON
import flet as ft
def main(pagina:ft.Page):
  pagina.title = "Aula 09 - Flet"
  mensagem = ft.Text(value="Meu Primeiro código Flet", color="#62afff", size=60)
  entrada_aluno = ft.TextField(label="Aluno")
  botao = ft.Button(text="Enviar")
  pagina.add(mensagem, entrada_aluno, botao)
ft.app(target=main)

# APLICAÇÃO COM CLICK
import flet as ft
def main(pagina:ft.Page):
  def enviar(e):
    resultado.value = f"Olá {entrada_aluno.value} seja bem vindo(a)"
    pagina.update()
  pagina.title = "Aula 09 - Flet"
  mensagem = ft.Text(value="Meu Primeiro código Flet", color="#62afff", size=60)
  entrada_aluno = ft.TextField(label="Aluno")
  botao = ft.Button(text="Enviar", on_click=enviar)
  resultado = ft.Text(value="")
  pagina.add(mensagem, entrada_aluno, botao, resultado)
ft.app(target=main)

# ATIVIDADE 1
# FAÇA UM PROGRAMA EM FLET QUE PEDE PARA O USUÁRIO DIGITAR SUA IDADE E MOSTRE NA TELA SE ELE É MAIOR OU MENOR DE IDADE.
import flet as ft
def main(pagina:ft.Page):
  def checar(e):
    if int(entrada_idade.value) >= 18:
      resultado.value = "Maior de idade"
    else:
      resultado.value = "Menor de idade"
    pagina.update()
  pagina.title = "Checador de Idades"
  mensagem = ft.Text(value="Teste a sua idade")
  entrada_idade = ft.TextField(label="Idade")
  botao = ft.Button(text="Checar", on_click=checar)
  resultado = ft.Text(value="")
  pagina.add(mensagem, entrada_idade, botao, resultado)
ft.app(target=main)


# ATIVIDADE 2
# FAÇA UM PROGRAMA EM FLET QUE PEDE PARA O USUÁRIO DIGITAR 4 NOTAS, CALCULE A MÉDIA E MOSTRE NA TELA SE ELE APROVADO OU REPROVADO (CONSIDERE A MÉDIA 7)
# SE ELE FOR APROVADO, MOSTRAR O TEXTO DA COR VERDE, SE NÃO DA COR VERMELHA.
import flet as ft


def main(pagina: ft.Page):
    def calculcarMedia(e):
        n1 = float(nota1.value)
        n2 = float(nota2.value)
        n3 = float(nota3.value)
        n4 = float(nota4.value)
        media = (n1 + n2 + n3 + n4) / 4
        if media >= 7:
            resultado.value = f"Aprovado com a média {media:.2f}"
            resultado.color = "#12624c"
        else:
            resultado.value = f"Reprovado com a média {media:.2f}"
            resultado.color = "#93204d"
        resultado.value= f

    pagina.title = "Colégio X"
    mensagem = ft.Text(value="Calculadora da Médias", size=50, color="#006b73")
    nota1 = ft.TextField(label="Nota 1")
    nota2 = ft.TextField(label="Nota 2")
    nota3 = ft.TextField(label="Nota 3")
    nota4 = ft.TextField(label="Nota 4")
    botao = ft.Button(text="Consultar", on_click=calculcarMedia)
    resultado = ft.Text(value="")
    pagina.add(mensagem, nota1, nota2, nota3, nota4, botao, resultado)


ft.app(target=main)