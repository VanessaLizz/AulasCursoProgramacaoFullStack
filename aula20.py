#AULA 20 - PYTHON 
#AULA 06 - BANCO DE DADOS - CRIAÇÃO DE API COM FLASK


#RESPOSTAS DAS REQUISIÇÕES
#1. Respostas Informativas (100 – 199)
#2. Respostas bem-sucedidas (200 – 299)
#3. Mensagens de redirecionamento (300 – 399)
#4. Respostas de erro do cliente (400 – 499)
#5. Respostas de erro do servidor (500 – 599)

#pip install flask
#pip install flask-cors


# BASE DE UMA API
# import mysql.connector
# from flask import Flask, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pokedex'
)

@app.route("/api/bixinhos", methods=['GET'])
def buscarPokemons():
    abinha = conexao.cursor(dictionary=True)
    abinha.execute('SELECT * FROM pokemons')
    lista_pokemons = abinha.fetchall()
    abinha.close()  
    return jsonify(lista_pokemons)

if __name__ == '__main__':
  app.run(debug=True)



#CRUD COMPLETO
import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pokedex'
)

@app.route("/api/bixinhos", methods=['GET'])
def buscarPokemons():
    abinha = conexao.cursor(dictionary=True)
    abinha.execute('SELECT * FROM pokemons')
    lista_pokemons = abinha.fetchall()
    abinha.close()  
    return jsonify(lista_pokemons)

@app.route("/api/bixinhos", methods=['POST'])
def cadastrarPokemon():
  dados = request.json
  abinha = conexao.cursor(dictionary=True)
  consulta = '''
      INSERT INTO pokemons (nome, tipo, imagem) 
          VALUES (%s, %s, %s)
      '''
  itens = (dados['nome'], dados['tipo'], dados['imagem'])
  abinha.execute(consulta,itens)
  conexao.commit()
  abinha.close()
  return jsonify({"mensagem": "foi sal"})


@app.route("/api/bixinhos/<int:id>", methods=['PUT'])
def editarPokemon(id):
  dados = request.json
  abinha = conexao.cursor(dictionary=True)
  consulta = '''
      UPDATE pokemons SET nome = %s, tipo = %s, imagem = %s WHERE id = %s
      '''
  itens = (dados['nome'], dados['tipo'], dados['imagem'], id)
  abinha.execute(consulta,itens)
  conexao.commit()
  abinha.close()
  return jsonify({"mensagem": "foi sal mais uma vez"})


@app.route("/api/bixinhos/<int:id>", methods=['DELETE'])
def deletarPokemon(id):
  abinha = conexao.cursor(dictionary=True)
  consulta = 'DELETE FROM pokemons WHERE id = %s'
  item = (id)
  abinha.execute(consulta, item)
  conexao.commit()
  abinha.close()
  return jsonify({"mensagem": "Foi sal também"})

if __name__ == '__main__':
  app.run(debug=True)



# PROJETO FINAL
# FAÇA UM BACK-END / API / BANCO DE DADOS
# PARA UM CONTROLE DE ESTOQUE.
# - PRIMEIRO FAÇA O BANCO
# - SEGUNDO CONECTA O BANCO COM O PYTHON
# - TERCEIRO CRIA UMA API
# - MONTA AS 4 ROTAS