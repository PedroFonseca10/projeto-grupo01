from config.database import Database

class ProdutoModel:
    """Modelo para gerenciar produtos"""
    
    @staticmethod
    def criar(dados):
        """Cria um novo produto"""
        query = """
        INSERT INTO Cad_Produto 
        (nome_produto, sku_codigo, categoria, quant_atual, quant_min, quant_max, 
         valor_uni, unidade, localizacao, fornecedor, descricao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            dados.get('nome_produto'),
            dados.get('sku_codigo'),
            dados.get('categoria'),
            dados.get('quant_atual'),
            dados.get('quant_min'),
            dados.get('quant_max'),
            dados.get('valor_uni'),
            dados.get('unidade'),
            dados.get('localizacao'),
            dados.get('fornecedor'),
            dados.get('descricao')
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Produto criado com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def listar():
        """Lista todos os produtos"""
        query = "SELECT * FROM Cad_Produto"
        try:
            cursor = Database.execute_query(query)
            colunas = [desc[0] for desc in cursor.description]
            produtos = []
            for row in cursor.fetchall():
                produtos.append(dict(zip(colunas, row)))
            return produtos
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def obter_por_id(id_produto):
        """Obtém um produto específico"""
        query = "SELECT * FROM Cad_Produto WHERE id_produto = ?"
        try:
            cursor = Database.execute_query(query, (id_produto,))
            colunas = [desc[0] for desc in cursor.description]
            row = cursor.fetchone()
            if row:
                return dict(zip(colunas, row))
            return None
        except Exception as e:
            return {"erro": str(e)}
    
    @staticmethod
    def atualizar(id_produto, dados):
        """Atualiza um produto"""
        query = """
        UPDATE Cad_Produto SET 
        nome_produto=?, sku_codigo=?, categoria=?, quant_atual=?, quant_min=?, 
        quant_max=?, valor_uni=?, unidade=?, localizacao=?, fornecedor=?, descricao=?
        WHERE id_produto = ?
        """
        params = (
            dados.get('nome_produto'),
            dados.get('sku_codigo'),
            dados.get('categoria'),
            dados.get('quant_atual'),
            dados.get('quant_min'),
            dados.get('quant_max'),
            dados.get('valor_uni'),
            dados.get('unidade'),
            dados.get('localizacao'),
            dados.get('fornecedor'),
            dados.get('descricao'),
            id_produto
        )
        try:
            cursor = Database.execute_query(query, params)
            Database.commit()
            return {"sucesso": True, "mensagem": "Produto atualizado com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def deletar(id_produto):
        """Deleta um produto"""
        query = "DELETE FROM Cad_Produto WHERE id_produto = ?"
        try:
            cursor = Database.execute_query(query, (id_produto,))
            Database.commit()
            return {"sucesso": True, "mensagem": "Produto deletado com sucesso"}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def verificar_estoque_minimo():
        """Verifica produtos que estão abaixo do estoque mínimo"""
        query = "SELECT * FROM Cad_Produto WHERE quant_atual < quant_min"
        try:
            cursor = Database.execute_query(query)
            colunas = [desc[0] for desc in cursor.description]
            produtos = []
            for row in cursor.fetchall():
                produtos.append(dict(zip(colunas, row)))
            return produtos
        except Exception as e:
            return {"erro": str(e)}
