CREATE DATABASE ControleEstoque;
GO

USE ControleEstoque;
GO

CREATE TABLE Cad_Fornecedor (
    id_cad_fornecedor INT PRIMARY KEY IDENTITY(1,1),
    razao_social NVARCHAR(150),
    nome_fantasia NVARCHAR(150),
    cnpj VARCHAR(20),
    incricao_estadual VARCHAR(30),
    categoria VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(100),
    site VARCHAR(100),
    endereco VARCHAR(200),
    prazo_entrega VARCHAR(50),
    cond_pagamento VARCHAR(100),
    observacoes NVARCHAR(255)
);

CREATE TABLE Cad_Produto (
    id_produto INT PRIMARY KEY IDENTITY(1,1),
    nome_produto NVARCHAR(150),
    sku_codigo VARCHAR(50),
    categoria VARCHAR(100),
    quant_atual INT,
    quant_min INT,
    quant_max INT,
    valor_uni DECIMAL(10,2),
    unidade VARCHAR(20),
    localizacao VARCHAR(100),
    fornecedor INT,
    descricao NVARCHAR(255),

    CONSTRAINT FK_Produto_Fornecedor
        FOREIGN KEY (fornecedor)
        REFERENCES Cad_Fornecedor(id_cad_fornecedor)
);

CREATE TABLE Cad_Usuario (
    id_cad_usuario INT PRIMARY KEY IDENTITY(1,1),
    nome_completo NVARCHAR(150),
    email VARCHAR(100),
    funcao VARCHAR(100),
    departamento VARCHAR(100),
    status VARCHAR(20),
    telefone VARCHAR(20),
    senha VARCHAR(100),
    confirmacao_senha VARCHAR(100),
    visualizar_estoque BIT,
    excluir_registros BIT,
    configuracoes BIT,
    registrar_entradas BIT,
    registrar_saidas BIT,
    gerenciar_usuarios BIT,
    gerenciar_relatorios BIT,
    gerenciar_fornecedores BIT
);

CREATE TABLE Registrar_Entrada (
    id_registrar_entrada INT PRIMARY KEY IDENTITY(1,1),
    produto INT,
    quantidade INT,
    fornecedor INT,
    numero_nf VARCHAR(50),
    data_recebimento DATE,
    valor_uni DECIMAL(10,2),
    observacoes NVARCHAR(255),

    CONSTRAINT FK_Entrada_Produto
        FOREIGN KEY (produto)
        REFERENCES Cad_Produto(id_produto),

    CONSTRAINT FK_Entrada_Fornecedor
        FOREIGN KEY (fornecedor)
        REFERENCES Cad_Fornecedor(id_cad_fornecedor)
);

CREATE TABLE Registrar_Saida (
    id_registrar_saida INT PRIMARY KEY IDENTITY(1,1),
    produto INT,
    quantidade INT,
    destino VARCHAR(150),
    responsavel INT,
    data_saida DATE,
    motivo VARCHAR(150),
    observacoes NVARCHAR(255),

    CONSTRAINT FK_Saida_Produto
        FOREIGN KEY (produto)
        REFERENCES Cad_Produto(id_produto),

    CONSTRAINT FK_Saida_Usuario
        FOREIGN KEY (responsavel)
        REFERENCES Cad_Usuario(id_cad_usuario)
);
