from config.database import Database

class FornecedorModel:
    """Modelo para gerenciar fornecedores"""
    
    @staticmethod
    def criar(dados):
        """Cria um novo fornecedor"""
        query = """
        INSERT INTO Cad_Fornecedor 
        (razao_social, nome_fantasia, cnpj, incricao_estadual, categoria, 
         telefone, email, site, endereco, prazo_entrega, cond_pagamento, observacoes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            dados.get('razao_social'),
            dados.get('nome_fantasia'),
            dados.get('cnpj'),
            dados.get('incricao_estadual'),
            dados.get('categoria'),
            dados.get('telefone'),
            dados.get('email'),
            dados.get('site'),
            dados.get('endereco'),
            dados.get('prazo_entrega'),
            dados.get('cond_pagamento'),
            dados.get('observacoes')
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Fornecedor criado com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def listar():
        """Lista todos os fornecedores"""
        query = "SELECT * FROM Cad_Fornecedor"
        try:
            cursor = Database.execute_query(query)
            colunas = [desc[0] for desc in cursor.description]
            fornecedores = []
            for row in cursor.fetchall():
                fornecedores.append(dict(zip(colunas, row)))
            return fornecedores
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def obter_por_id(id_fornecedor):
        """Obtém um fornecedor específico"""
        query = "SELECT * FROM Cad_Fornecedor WHERE id_cad_fornecedor = ?"
        try:
            cursor = Database.execute_query(query, (id_fornecedor,))
            colunas = [desc[0] for desc in cursor.description]
            row = cursor.fetchone()
            if row:
                return dict(zip(colunas, row))
            return None
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def atualizar(id_fornecedor, dados):
        """Atualiza um fornecedor"""
        query = """
        UPDATE Cad_Fornecedor SET 
        razao_social=?, nome_fantasia=?, cnpj=?, incricao_estadual=?, 
        categoria=?, telefone=?, email=?, site=?, endereco=?, 
        prazo_entrega=?, cond_pagamento=?, observacoes=?
        WHERE id_cad_fornecedor = ?
        """
        params = (
            dados.get('razao_social'),
            dados.get('nome_fantasia'),
            dados.get('cnpj'),
            dados.get('incricao_estadual'),
            dados.get('categoria'),
            dados.get('telefone'),
            dados.get('email'),
            dados.get('site'),
            dados.get('endereco'),
            dados.get('prazo_entrega'),
            dados.get('cond_pagamento'),
            dados.get('observacoes'),
            id_fornecedor
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Fornecedor atualizado com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def deletar(id_fornecedor):
        """Deleta um fornecedor"""
        query = "DELETE FROM Cad_Fornecedor WHERE id_cad_fornecedor = ?"
        try:
            cursor = Database.execute_query(query, (id_fornecedor,))
            Database.commit()
            return {"sucesso": True, "mensagem": "Fornecedor deletado com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
