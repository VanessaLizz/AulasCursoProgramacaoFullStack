# AULA 15 - PYTHON
# AULA 01 - BANCO DE DADOS - INTRODUÇÃO


# TERMOS

# SQL - LINGUAGEM (PODE SER USADA POR QUALQUER EMPRESA) 

# MYSQL - SGBD (SISTEMA DE GERENCIAMENTO DE BANCO DE DADOS (RELACIONAL) ) É TIPO A EMPRESA

# WORKBENCH - IDE (PROGRAMA QUE VAMOS USAR PARA RODAR O BANCO)

# MYSQL SERVER - SERVIDOR DA EMPRESA MYSQL

# XAMPP - SERVIDOR SIMULADO.

# mysql
# https://dev.mysql.com/downloads/installer/

# xampp
# Download XAMPP

create database aula515;
use aula515;

create table alunos(
    id INT AUTO_INCREMENT PRIMARY KEY,
	nome varchar(45) NOT NULL,
    idade tinyint,
    email varchar(50),
    telefone varchar(20),
    cpf char(11) NOT NULL UNIQUE,
    endereço VARCHAR(80),
    altura decimal(3,2),
    salario decimal (8,2),
    biografia text,
    data_nascimento date,
    horario_aula time,
    presenca datetime,
    matriculado bool,
    sala_de_aula enum('londres', 'berlin')
);

drop table alunos;

alter table alunos




# AULA 16 - PYTHON
# AULA 02 - BANCO DE DADOS - CRUD DE DADOS

# ATIVIDADE REVISÃO
# CRIE UM BANCO PARA REPRESENTAR UMA ACADEMIA
# USE ESSE BANCO
# CRIE UMA TABELA PARA REPRESENTAR OS ALUNOS DA ACADEMIA COM OS CAMPOS:
# ID, NOME, CPF, TELEFONE, EMAIL, ENDEREÇO, DATA_INSCRIÇÃO
CREATE DATABASE academia;
USE academia;

CREATE TABLE alunos(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(50) UNIQUE,
    endereco VARCHAR(80),
    data_inscricao DATE NOT NULL
);