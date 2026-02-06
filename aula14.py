#AULA 14 - PROJETO DE POO


#alunos.py
class Aluno():
    def __init__(self, numero_matricula: int, nome: str, telefone: str, email: str):
        self.numero_matricula = numero_matricula
        self.nome = nome
        self.telefone = telefone
        self.email = email


#escolas.py

from alunos import Aluno
from turmas import Turma

class Escola():
    def __init__(self, nome: str, cnpj: str, endereco: str, telefone: str):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.lista_de_alunos = []
        self.lista_de_turmas = []
        self.numero_matricula_atual = 0

    def cadastrarAluno(self):
        nome = input("Digite o nome do novo aluno: ")
        email = input("Digite o email do novo aluno: ")
        telefone = input("Digite o telefone do novo aluno: ")
        novo_aluno = Aluno(numero_matricula=self.numero_matricula_atual,
                      nome=nome, email=email, telefone=telefone)
        self.numero_matricula_atual += 1
        self.lista_de_alunos.append(novo_aluno)
        return "Aluno cadastrado com sucesso"

    def listarAlunos(self):
        for element in self.lista_de_alunos:
            print(f"""
      ======================
      INFORMAÇÕES DO ALUNO
      Matrícula: {element.numero_matricula}
      Nome: {element.nome}
      E-Mail: {element.email}
      Telefone de Contato: {element.telefone}
      ======================
      """)

    def editarAluno(self):
        ...

    def excluirAluno(self):
        ...





    def cadastrarTurma(self):
        ...

    def listarTurmas(self):
        ...

    def editarTurma(self):
        ...

    def excluirTurma(self):
        ...





    def cadastrarMatriula(self):
        ...

    def listarMatriulas(self):
        ...

    def editarMatriula(self):
        ...

    def excluirMatriula(self):
        ...


#main.py
    from escolas import Escola
    
    escola1 = Escola(nome="Abel Code", cnpj="666", endereco="Rua logo ali, -4", telefone="859856330356")
    while True:
      menu = input("""
        MENU PRINCIPAL
        1 - Fluxo de Alunos
        2 - Fluxo de Turmas
        3 - Fluxo de Matrículas
        0 - Sair
    """)
      match menu:
        case "1":
          while True:
            menu_aluno = input("""
            MENU DOS ALUNOS
            1 - Cadastrar novo aluno
            2 - Listar todos os alunos
            3 - Editar um aluno cadastrado
            4 - Excluir um aluno cadastrado
            0 - Voltar
            """)
            match menu_aluno:
              case "1":
                print(escola1.cadastrarAluno())
              case "2":
                escola1.listarAlunos()
              case "3":
                ...
              case "4":
                ...
              case "0":
                break
              case _:
                print("Opção inválida")
        case "2":
          ...
        case "3":
          ...
        case "0":
          break
        case _:
          print("Opção inválida")

#matriculas.py
from alunos import Aluno
from turmas import Turma
class Matricula():
  def __init__(self, aluno: Aluno, turma:Turma, data:str ):
    self.aluno = aluno
    self.turma = turma
    self.data = data

#turma.py
class Turma():
    def __init__(self, numero: int, curso: str, valor_mensalidade: float):
        self.numero = numero
        self.curso = curso
        self.valor_mensalidade = valor_mensalidade
        self.vagas_abertas = True


# QUANDO FOR ENVIAR O PROJETO, MANDE ESCRITO JUNTO COM ELE:

# "O PROFESSOR ABEL INFORMOU QUE O USO DA BIBLIOTECA FLET É OPCIONAL"