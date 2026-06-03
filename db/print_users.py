import sqlite3

DB = 'db/controle_estoque.db'

def print_users():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    try:
        cur.execute("SELECT id_cad_usuario, nome_completo, email FROM Cad_Usuario;")
        rows = cur.fetchall()
        print('Usuários:', rows)
    except Exception as e:
        print('Erro ao buscar usuários:', e)
    finally:
        conn.close()

if __name__ == '__main__':
    print_users()
