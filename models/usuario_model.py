from config.database import Database
import hashlib

class UsuarioModel:
    """Modelo para gerenciar usuários"""
    
    @staticmethod
    def _hash_senha(senha):
        """Gera hash da senha"""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    @staticmethod
    def criar(dados):
        """Cria um novo usuário"""
        query = """
        INSERT INTO Cad_Usuario 
        (nome_completo, email, funcao, departamento, status, telefone, 
         senha, confirmacao_senha, visualizar_estoque, excluir_registros, 
         configuracoes, registrar_entradas, registrar_saidas, gerenciar_usuarios, 
         gerenciar_relatorios, gerenciar_fornecedores)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        senha_hash = UsuarioModel._hash_senha(dados.get('senha'))
        params = (
            dados.get('nome_completo'),
            dados.get('email'),
            dados.get('funcao'),
            dados.get('departamento'),
            dados.get('status', 'ativo'),
            dados.get('telefone'),
            senha_hash,
            senha_hash,
            dados.get('visualizar_estoque', 1),
            dados.get('excluir_registros', 0),
            dados.get('configuracoes', 0),
            dados.get('registrar_entradas', 0),
            dados.get('registrar_saidas', 0),
            dados.get('gerenciar_usuarios', 0),
            dados.get('gerenciar_relatorios', 0),
            dados.get('gerenciar_fornecedores', 0)
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Usuário criado com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def listar():
        """Lista todos os usuários"""
        query = "SELECT * FROM Cad_Usuario"
        try:
            cursor = Database.execute_query(query)
            colunas = [desc[0] for desc in cursor.description]
            usuarios = []
            for row in cursor.fetchall():
                usuarios.append(dict(zip(colunas, row)))
            return usuarios
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def obter_por_id(id_usuario):
        """Obtém um usuário específico"""
        query = "SELECT * FROM Cad_Usuario WHERE id_cad_usuario = ?"
        try:
            cursor = Database.execute_query(query, (id_usuario,))
            colunas = [desc[0] for desc in cursor.description]
            row = cursor.fetchone()
            if row:
                return dict(zip(colunas, row))
            return None
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def autenticar(email, senha):
        """Autentica um usuário"""
        query = "SELECT * FROM Cad_Usuario WHERE email = ?"
        try:
            cursor = Database.execute_query(query, (email,))
            colunas = [desc[0] for desc in cursor.description]
            row = cursor.fetchone()
            if row:
                usuario = dict(zip(colunas, row))
                senha_hash = UsuarioModel._hash_senha(senha)
                if usuario['senha'] == senha_hash:
                    return usuario
            return None
        except Exception as e:
            return None
    
    @staticmethod
    def atualizar(id_usuario, dados):
        """Atualiza um usuário"""
        query = """
        UPDATE Cad_Usuario SET 
        nome_completo=?, email=?, funcao=?, departamento=?, status=?, 
        telefone=?, visualizar_estoque=?, excluir_registros=?, configuracoes=?, 
        registrar_entradas=?, registrar_saidas=?, gerenciar_usuarios=?, 
        gerenciar_relatorios=?, gerenciar_fornecedores=?
        WHERE id_cad_usuario = ?
        """
        params = (
            dados.get('nome_completo'),
            dados.get('email'),
            dados.get('funcao'),
            dados.get('departamento'),
            dados.get('status'),
            dados.get('telefone'),
            dados.get('visualizar_estoque'),
            dados.get('excluir_registros'),
            dados.get('configuracoes'),
            dados.get('registrar_entradas'),
            dados.get('registrar_saidas'),
            dados.get('gerenciar_usuarios'),
            dados.get('gerenciar_relatorios'),
            dados.get('gerenciar_fornecedores'),
            id_usuario
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Usuário atualizado com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def deletar(id_usuario):
        """Deleta um usuário"""
        query = "DELETE FROM Cad_Usuario WHERE id_cad_usuario = ?"
        try:
            cursor = Database.execute_query(query, (id_usuario,))
            Database.commit()
            return {"sucesso": True, "mensagem": "Usuário deletado com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
