from config.database import Database

class SaidaModel:
    """Modelo para gerenciar registros de saída"""
    
    @staticmethod
    def criar(dados):
        """Cria um novo registro de saída"""
        query = """
        INSERT INTO Registrar_Saida 
        (produto, quantidade, destino, responsavel, data_saida, motivo, observacoes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            dados.get('produto'),
            dados.get('quantidade'),
            dados.get('destino'),
            dados.get('responsavel'),
            dados.get('data_saida'),
            dados.get('motivo'),
            dados.get('observacoes')
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Saída registrada com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def listar():
        """Lista todos os registros de saída"""
        query = "SELECT * FROM Registrar_Saida"
        try:
            cursor = Database.execute_query(query)
            colunas = [desc[0] for desc in cursor.description]
            saidas = []
            for row in cursor.fetchall():
                saidas.append(dict(zip(colunas, row)))
            return saidas
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def obter_por_id(id_saida):
        """Obtém um registro de saída específico"""
        query = "SELECT * FROM Registrar_Saida WHERE id_registrar_saida = ?"
        try:
            cursor = Database.execute_query(query, (id_saida,))
            colunas = [desc[0] for desc in cursor.description]
            row = cursor.fetchone()
            if row:
                return dict(zip(colunas, row))
            return None
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def atualizar(id_saida, dados):
        """Atualiza um registro de saída"""
        query = """
        UPDATE Registrar_Saida SET 
        produto=?, quantidade=?, destino=?, responsavel=?, 
        data_saida=?, motivo=?, observacoes=?
        WHERE id_registrar_saida = ?
        """
        params = (
            dados.get('produto'),
            dados.get('quantidade'),
            dados.get('destino'),
            dados.get('responsavel'),
            dados.get('data_saida'),
            dados.get('motivo'),
            dados.get('observacoes'),
            id_saida
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Saída atualizada com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def deletar(id_saida):
        """Deleta um registro de saída"""
        query = "DELETE FROM Registrar_Saida WHERE id_registrar_saida = ?"
        try:
            cursor = Database.execute_query(query, (id_saida,))
            Database.commit()
            return {"sucesso": True, "mensagem": "Saída deletada com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
