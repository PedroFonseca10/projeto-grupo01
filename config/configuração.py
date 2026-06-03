#leitura das configuracoes 
import os
from dotenv import load_dotenv

load_dotenv()

class Configuracao:
    # Autenticação
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    JWT_SECRET = os.getenv('JWT_SECRET')
    
    # Banco de Dados SQL Server
    # Engine: 'mssql' (pyodbc) or 'sqlite'
    DB_ENGINE = os.getenv('DB_ENGINE', 'sqlite')
    DB_SERVER = os.getenv('DB_SERVER', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'ControleEstoque')
    DB_USER = os.getenv('DB_USER', 'sa')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'senha123')
    # Arquivo SQLite (quando DB_ENGINE=sqlite)
    SQLITE_FILE = os.getenv('SQLITE_FILE', 'db/controle_estoque.db')
    
    # Aplicação
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
