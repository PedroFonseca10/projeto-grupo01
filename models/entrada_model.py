from config.database import Database

class EntradaModel:
    """Modelo para gerenciar registros de entrada"""
    
    @staticmethod
    def criar(dados):
        """Cria um novo registro de entrada"""
        query = """
        INSERT INTO Registrar_Entrada 
        (produto, quantidade, fornecedor, numero_nf, data_recebimento, valor_uni, observacoes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            dados.get('produto'),
            dados.get('quantidade'),
            dados.get('fornecedor'),
            dados.get('numero_nf'),
            dados.get('data_recebimento'),
            dados.get('valor_uni'),
            dados.get('observacoes')
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Entrada registrada com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def listar():
        """Lista todos os registros de entrada"""
        query = "SELECT * FROM Registrar_Entrada"
        try:
            cursor = Database.execute_query(query)
            colunas = [desc[0] for desc in cursor.description]
            entradas = []
            for row in cursor.fetchall():
                entradas.append(dict(zip(colunas, row)))
            return entradas
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def obter_por_id(id_entrada):
        """Obtém um registro de entrada específico"""
        query = "SELECT * FROM Registrar_Entrada WHERE id_registrar_entrada = ?"
        try:
            cursor = Database.execute_query(query, (id_entrada,))
            colunas = [desc[0] for desc in cursor.description]
            row = cursor.fetchone()
            if row:
                return dict(zip(colunas, row))
            return None
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def atualizar(id_entrada, dados):
        """Atualiza um registro de entrada"""
        query = """
        UPDATE Registrar_Entrada SET 
        produto=?, quantidade=?, fornecedor=?, numero_nf=?, 
        data_recebimento=?, valor_uni=?, observacoes=?
        WHERE id_registrar_entrada = ?
        """
        params = (
            dados.get('produto'),
            dados.get('quantidade'),
            dados.get('fornecedor'),
            dados.get('numero_nf'),
            dados.get('data_recebimento'),
            dados.get('valor_uni'),
            dados.get('observacoes'),
            id_entrada
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Entrada atualizada com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def deletar(id_entrada):
        """Deleta um registro de entrada"""
        query = "DELETE FROM Registrar_Entrada WHERE id_registrar_entrada = ?"
        try:
            cursor = Database.execute_query(query, (id_entrada,))
            Database.commit()
            return {"sucesso": True, "mensagem": "Entrada deletada com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
