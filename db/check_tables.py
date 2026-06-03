import sqlite3

DB = 'db/controle_estoque.db'

def list_tables():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    rows = cur.fetchall()
    conn.close()
    print('Tabelas no DB:', rows)

if __name__ == '__main__':
    list_tables()
