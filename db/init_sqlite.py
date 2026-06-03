"""Inicializador SQLite para demo local do ControleEstoque.
Executar: python db/init_sqlite.py
Isso criará o arquivo `db/controle_estoque.db` com as tabelas necessárias.
"""
import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(__file__), 'controle_estoque.db')

os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

schema = [
    """
    CREATE TABLE IF NOT EXISTS Cad_Fornecedor (
        id_cad_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
        razao_social TEXT,
        nome_fantasia TEXT,
        cnpj TEXT,
        incricao_estadual TEXT,
        categoria TEXT,
        telefone TEXT,
        email TEXT,
        site TEXT,
        endereco TEXT,
        prazo_entrega TEXT,
        cond_pagamento TEXT,
        observacoes TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Cad_Produto (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto TEXT,
        sku_codigo TEXT,
        categoria TEXT,
        quant_atual INTEGER,
        quant_min INTEGER,
        quant_max INTEGER,
        valor_uni REAL,
        unidade TEXT,
        localizacao TEXT,
        fornecedor INTEGER,
        descricao TEXT,
        FOREIGN KEY(fornecedor) REFERENCES Cad_Fornecedor(id_cad_fornecedor)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Cad_Usuario (
        id_cad_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT,
        email TEXT,
        funcao TEXT,
        departamento TEXT,
        status TEXT,
        telefone TEXT,
        senha TEXT,
        confirmacao_senha TEXT,
        visualizar_estoque INTEGER,
        excluir_registros INTEGER,
        configuracoes INTEGER,
        registrar_entradas INTEGER,
        registrar_saidas INTEGER,
        gerenciar_usuarios INTEGER,
        gerenciar_relatorios INTEGER,
        gerenciar_fornecedores INTEGER
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Registrar_Entrada (
        id_registrar_entrada INTEGER PRIMARY KEY AUTOINCREMENT,
        produto INTEGER,
        quantidade INTEGER,
        fornecedor INTEGER,
        numero_nf TEXT,
        data_recebimento TEXT,
        valor_uni REAL,
        observacoes TEXT,
        FOREIGN KEY(produto) REFERENCES Cad_Produto(id_produto),
        FOREIGN KEY(fornecedor) REFERENCES Cad_Fornecedor(id_cad_fornecedor)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Registrar_Saida (
        id_registrar_saida INTEGER PRIMARY KEY AUTOINCREMENT,
        produto INTEGER,
        quantidade INTEGER,
        destino TEXT,
        responsavel INTEGER,
        data_saida TEXT,
        motivo TEXT,
        observacoes TEXT,
        FOREIGN KEY(produto) REFERENCES Cad_Produto(id_produto),
        FOREIGN KEY(responsavel) REFERENCES Cad_Usuario(id_cad_usuario)
    );
    """,
]

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    for s in schema:
        cur.executescript(s)
    conn.commit()
    conn.close()
    print(f"Banco SQLite criado em: {DB_FILE}")

if __name__ == '__main__':
    init_db()
