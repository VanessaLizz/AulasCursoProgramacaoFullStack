# AULA 18 - PYTHON 
# AULA 04 - BANCO DE DADOS - CONECTANDO COM O PYTHON

# EXERCICIO PREPARATÓRIO:
# FAÇA UM BANCO PARA REPRESENTAR UMA GIBITECA
# USE O BANCO
# CRIE UMA TABELA PARA REPRESENTAR AS EQUIPES COM OS CAMPOS:
# ID, NOME.

# CRIE UMA TABELA PARA REPRESENTAR OS HEROIS COM OS CAMPOS:
# ID, ALTER_EGO, NOME, EMPRESA, PODER_PRINCIPAL, ID_EQUIPE.

# CRIE UMA TABELA PARA REPRESENTAR OS VILÕES COM OS CAMPOS:
# ID, NOME, EMPRESA, ID_EQUIPE, ID_HEROI
# ---

# INSIRA 3 GRUPOS, E 20 HEROIS E 10 VILOES

CREATE DATABASE gibiteca;
USE gibiteca;

CREATE TABLE equipes(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL
);
 
CREATE TABLE herois(
	id INT AUTO_INCREMENT PRIMARY KEY,
    alter_ego VARCHAR(30),
    nome VARCHAR(30) NOT NULL UNIQUE,
    empresa VARCHAR(15),
    poder_principal VARCHAR(30),
    id_equipe INT NULL,
    FOREIGN KEY (id_equipe) REFERENCES equipes (id)
);

CREATE TABLE viloes(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL UNIQUE,
    empresa VARCHAR(15),
    id_equipe INT NULL,
	id_heroi INT NULL,
    FOREIGN KEY (id_equipe) REFERENCES equipes (id),
    FOREIGN KEY (id_heroi) REFERENCES herois (id)
);

INSERT INTO equipes (nome) VALUES
('Vingadores'),
('Liga da Justiça'),
('X-Men');

INSERT INTO herois (alter_ego, nome, empresa, poder_principal, id_equipe) VALUES
('Tony Stark', 'Homem de Ferro', 'Marvel', 'Armadura tecnológica', 1),
('Steve Rogers', 'Capitão América', 'Marvel', 'Força e liderança', 1),
('Thor Odinson', 'Thor', 'Marvel', 'Controle do trovão', 1),
('Natasha Romanoff', 'Viúva Negra', 'Marvel', 'Espionagem', 1),
('Bruce Banner', 'Hulk', 'Marvel', 'Força extrema', 1),

('Bruce Wayne', 'Batman', 'DC', 'Intelecto e tecnologia', 2),
('Clark Kent', 'Superman', 'DC', 'Super força', 2),
('Diana Prince', 'Mulher-Maravilha', 'DC', 'Força e combate', 2),
('Barry Allen', 'Flash', 'DC', 'Super velocidade', 2),
('Arthur Curry', 'Aquaman', 'DC', 'Controle dos mares', 2),

('Logan', 'Wolverine', 'Marvel', 'Regeneração', 3),
('Scott Summers', 'Ciclope', 'Marvel', 'Raios ópicos', 3),
('Ororo Munroe', 'Tempestade', 'Marvel', 'Controle climático', 3),
('Jean Grey', 'Fênix', 'Marvel', 'Telepatia', 3),
('Charles Xavier', 'Professor X', 'Marvel', 'Telepatia', 3),

('Wade Wilson', 'Deadpool', 'Marvel', 'Regeneração', NULL),
('Peter Parker', 'Homem-Aranha', 'Marvel', 'Agilidade e teia', NULL),
('Stephen Strange', 'Doutor Estranho', 'Marvel', 'Magia', NULL),
('Al Simmons', 'Spawn', 'Image', 'Poderes infernais', NULL),
('Anung Un Rama', 'Hellboy', 'Dark Horse', 'Força demoníaca', NULL);


INSERT INTO viloes (nome, empresa, id_equipe, id_heroi) VALUES
('Loki', 'Marvel', 1, NULL),          
('Ultron', 'Marvel', 1, 1),             
('Coringa', 'DC', NULL, 6),               
('Lex Luthor', 'DC', 2, 7),               
('Flash Reverso', 'DC', NULL, 9),          
('Magneto', 'Marvel', 3, NULL),            
('Apocalipse', 'Marvel', 3, NULL),        
('Duende Verde', 'Marvel', NULL, 17),      
('Dormammu', 'Marvel', NULL, 18),          
('Lobo', 'DC', NULL, NULL);           

# pip install mysql-connector-python



import mysql.connector

conexao = mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='gibiteca'
)

if conexao.is_connected():
  print("Conexão estabelecida com sucesso.")
else:
  print("Erro ao conectar no banco")