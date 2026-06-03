import os
from dotenv import load_dotenv

load_dotenv()

from config.configuração import Configuracao

class Database:
    _connection = None
    
    @classmethod
    def get_connection(cls):
        """Obtém ou cria uma conexão com o banco de dados (SQLite ou SQL Server)"""
        if cls._connection is None:
            engine = Configuracao.DB_ENGINE.lower()
            try:
                if engine == 'sqlite':
                    import sqlite3
                    db_path = Configuracao.SQLITE_FILE
                    # garante diretório
                    os.makedirs(os.path.dirname(db_path), exist_ok=True)
                    cls._connection = sqlite3.connect(db_path, check_same_thread=False)
                    cls._connection.row_factory = sqlite3.Row
                else:
                    import pyodbc
                    connection_string = (
                        f"Driver={{ODBC Driver 17 for SQL Server}};"
                        f"Server={Configuracao.DB_SERVER};"
                        f"Database={Configuracao.DB_NAME};"
                        f"UID={Configuracao.DB_USER};"
                        f"PWD={Configuracao.DB_PASSWORD};"
                    )
                    cls._connection = pyodbc.connect(connection_string)
                    cls._connection.autocommit = True
            except Exception as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
                raise
        return cls._connection
    
    @classmethod
    def commit(cls):
        """Executa commit na conexão ativa"""
        connection = cls.get_connection()
        connection.commit()

    @classmethod
    def close_connection(cls):
        """Fecha a conexão com o banco de dados"""
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
    
    @classmethod
    def execute_query(cls, query, params=None):
        """Executa uma query e retorna os resultados. Compatível com sqlite3 e pyodbc cursors."""
        try:
            connection = cls.get_connection()
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor
        except Exception as e:
            print(f"Erro ao executar query: {e}")
            raise
