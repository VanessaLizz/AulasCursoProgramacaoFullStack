# AULA 17 - PYTHON 
# AULA 03 - BANCO DE DADOS - INNER JOIN

# MONTAGEM DO BANCO
# UM BANCO PARA REPRESENTAR UMA LIVRARIA
# USE O BANCO
# CRIE UMA TABELA PARA REPRESENTAR OS AUTORES DOS LIVROS: ID, NOME, NACIONALIDADE, IDADE
# CRIE UMA TABELA PARA REPRESENTAR OS LIVROS: ID, TITULO, GENERO, QTDE_PAGINAS, ID_AUTOR
# INSIRA 5 AUTORES E 12 LIVROS.

CREATE DATABASE livraria;
USE livraria;

CREATE TABLE autores(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    nacionalidade VARCHAR(20),
    idade TINYINT
);

CREATE TABLE livros(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(60) NOT NULL,
    genero VARCHAR(30) NOT NULL,
    qtde_paginas MEDIUMINT NOT NULL,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores (id)
);


INSERT INTO autores (nome, nacionalidade, idade) VALUES
('Machado de Assis', 'Brasileira', 69),
('Clarice Lispector', 'Brasileira', 56),
('George Orwell', 'Britânica', 46),
('J.K. Rowling', 'Britânica', 58),
('Gabriel García Márquez', 'Colombiana', 87);


INSERT INTO livros (titulo, genero, qtde_paginas, id_autor) VALUES
('Dom Casmurro', 'Romance', 256, 1),
('Memórias Póstumas de Brás Cubas', 'Romance', 208, 1),
('A Hora da Estrela', 'Ficção', 96, 2),
('Laços de Família', 'Contos', 136, 2),
('1984', 'Distopia', 328, 3),
('A Revolução dos Bichos', 'Fábula', 152, 3),
('Harry Potter e a Pedra Filosofal', 'Fantasia', 320, 4),
('Harry Potter e a Câmara Secreta', 'Fantasia', 352, 4),
('Harry Potter e o Prisioneiro de Azkaban', 'Fantasia', 448, 4),
('Cem Anos de Solidão', 'Realismo Mágico', 432, 5),
('O Amor nos Tempos do Cólera', 'Romance', 368, 5),
('Crônica de uma Morte Anunciada', 'Romance', 144, 5);


# FAÇA AS CONSULTAS:
# [ ] TODOS OS CAMPOS DE TODOS OS LIVROS
# [ ] O TITULO E O GENERO DE TODOS OS LIVROS
# [ ] TODOS OS CAMPOS DOS LIVROS QUE TENHAM MAIS DE 300 PÁGINAS
# [ ] TITULO E A QTDE_PAGINAS DOS LIVROS QUE TENHA MENOS QUE 300 PÁGINAS
CREATE DATABASE livraria;
USE livraria;

CREATE TABLE autores(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    nacionalidade VARCHAR(20),
    idade TINYINT
);

CREATE TABLE livros(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(60) NOT NULL,
    genero VARCHAR(30) NOT NULL,
    qtde_paginas MEDIUMINT NOT NULL,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores (id)
);


INSERT INTO autores (nome, nacionalidade, idade) VALUES
('Machado de Assis', 'Brasileira', 69),
('Clarice Lispector', 'Brasileira', 56),
('George Orwell', 'Britânica', 46),
('J.K. Rowling', 'Britânica', 58),
('Gabriel García Márquez', 'Colombiana', 87);


INSERT INTO livros (titulo, genero, qtde_paginas, id_autor) VALUES
('Dom Casmurro', 'Romance', 256, 1),
('Memórias Póstumas de Brás Cubas', 'Romance', 208, 1),
('A Hora da Estrela', 'Ficção', 96, 2),
('Laços de Família', 'Contos', 136, 2),
('1984', 'Distopia', 328, 3),
('A Revolução dos Bichos', 'Fábula', 152, 3),
('Harry Potter e a Pedra Filosofal', 'Fantasia', 320, 4),
('Harry Potter e a Câmara Secreta', 'Fantasia', 352, 4),
('Harry Potter e o Prisioneiro de Azkaban', 'Fantasia', 448, 4),
('Cem Anos de Solidão', 'Realismo Mágico', 432, 5),
('O Amor nos Tempos do Cólera', 'Romance', 368, 5),
('Crônica de uma Morte Anunciada', 'Romance', 144, 5);



SELECT * FROM livros;
SELECT titulo, genero FROM livros;
SELECT * FROM livros WHERE qtde_paginas > 300;
SELECT titulo, qtde_paginas FROM livros WHERE qtde_paginas < 300;


SELECT
	livros.titulo AS 'Título do Livro',
    livros.genero AS 'Gênero do Livro',
    autores.nome AS 'Nome do Autor',
    autores.nacionalidade AS 'Nacionalidade do Autor'
    FROM livros
		INNER JOIN autores ON livros.id_autor = autores.id;
        

SELECT
	livros.titulo AS 'Título do Livro',
    livros.genero AS 'Gênero do Livro',
    autores.nome AS 'Nome do Autor',
    autores.nacionalidade AS 'Nacionalidade do Autor'
    FROM livros
		INNER JOIN autores ON livros.id_autor = autores.id
			WHERE autores.nacionalidade = 'Brasileira';

# ATIVIDADE 1
# FAÇA UM BANCO PARA REPRESENTAR UMA LANCHONETE
# USE O BANCO
# CRIE UMA TABELA PARA REPRESENTAR OS CLIENTES: ID, NOME, TELEFONE
# CRIE UMA TABELA PARA REPRESENTAR OS PRODUTOS: ID, NOME, PREÇO
# CRIE UMA TABELA PARA REPRESENTAR OS ATENDENTES: ID, NOME, SALARIO
# CRIE UMA TABELA PARA REPRESENTAR UMA VENDA: ID, DATA_VENDA, ID_CLIENTE, ID_PRODUTO, ID_ATENDENTE, QTDE_PRODUTOS, VALOR_TOTAL.
# INSIRA 10 CLIENTES, 20 PRODUTOS, 3 ATENDENTES E 5 VENDAS.

# ---
# FAÇA UMA CONSULTA QUE TRAGA:
# NOME DO CLIENTE, NOME DO ATENDENTE, NOME DO PRODUTO, PREÇO UNITÁRIO DO PRODUTO, DATA DA VENDA, QTDE_PRODUTOS, VALOR_TOTAL

CREATE DATABASE lanchonete;
USE lanchonete;

CREATE TABLE clientes (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE produtos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    preco DECIMAL(5,2) NOT NULL
);

CREATE TABLE atendentes (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    salario DECIMAL(7,2) NOT NULL
);

CREATE TABLE vendas(
	id INT AUTO_INCREMENT PRIMARY KEY,
    data_venda DATETIME NOT NULL,
    id_cliente INT NOT NULL,
    id_produto INT NOT NULL,
    id_atendente INT NOT NULL,
    qtde_produtos INT NOT NULL, 
    valor_total DECIMAL(6,2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes (id),
    FOREIGN KEY (id_produto) REFERENCES produtos (id),
    FOREIGN KEY (id_atendente) REFERENCES atendentes (id)
);

INSERT INTO clientes (nome, telefone) VALUES
('Ana Silva', '11999990001'),
('Bruno Costa', '11999990002'),
('Carlos Lima', '11999990003'),
('Daniel Souza', '11999990004'),
('Eduarda Rocha', '11999990005'),
('Fernanda Alves', '11999990006'),
('Gabriel Martins', '11999990007'),
('Helena Pires', '11999990008'),
('Igor Nunes', '11999990009'),
('Juliana Teixeira', '11999990010');

INSERT INTO produtos (nome, preco) VALUES
('Whey Protein', 120),
('Creatina', 90),
('BCAA', 80),
('Pré-treino', 110),
('Luvas', 45),
('Corda', 30),
('Garrafa', 25),
('Toalha', 35),
('Barra Proteica', 15),
('Colágeno', 70),
('Multivitamínico', 60),
('Shaker', 20),
('Faixa Elástica', 40),
('Cinturão', 85),
('Cafeína', 50),
('Ômega 3', 65),
('Glutamina', 75),
('Termogênico', 95),
('Camisa Dry Fit', 55),
('Shorts Treino', 60);

INSERT INTO atendentes (nome, salario) VALUES
('Lucas Andrade', 2500),
('Mariana Lopes', 2600),
('Rafael Oliveira', 2400);

INSERT INTO vendas 
(data_venda, id_cliente, id_produto, id_atendente, qtde_produtos, valor_total) 
VALUES
('2026-01-10 10:30:00', 1, 1, 1, 2, 240),
('2026-01-11 14:20:00', 3, 4, 2, 1, 110),
('2026-01-12 16:45:00', 5, 9, 1, 3, 45),
('2026-01-13 09:10:00', 7, 15, 3, 2, 100),
('2026-01-14 18:00:00', 2, 20, 2, 1, 60);


INSERT INTO vendas 
(data_venda, id_cliente, id_produto, id_atendente, qtde_produtos, valor_total) 
VALUES
('2026-01-11 14:20:00', 3, 1, 3, 4, 480);

SELECT 
	clientes.nome AS 'Cliente',
    atendentes.nome AS 'Atendente',
    produtos.nome AS 'Produto',
    produtos.preco AS 'Preço do Produto',
    vendas.data_venda AS 'Data da Venda',
    vendas.qtde_produtos AS 'Quantidade de Produtos',
    vendas.valor_total AS 'Valor total'
		FROM vendas
			INNER JOIN clientes ON vendas.id_cliente = clientes.id
            INNER JOIN produtos ON vendas.id_produto = produtos.id
            INNER JOIN atendentes ON vendas.id_atendente = atendentes.id;