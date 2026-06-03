from flask import request, jsonify
from models.produto_model import ProdutoModel
from middleware.autenticacao_middleware import AutenticacaoMiddleware

class ProdutoController:
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def criar():
        """Criar novo produto"""
        dados = request.get_json()
        resultado = ProdutoModel.criar(dados)
        status = 201 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def listar():
        """Listar todos os produtos"""
        produtos = ProdutoModel.listar()
        return jsonify(produtos), 200
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def obter(id_produto):
        """Obter produto específico"""
        produto = ProdutoModel.obter_por_id(id_produto)
        if produto:
            return jsonify(produto), 200
        return jsonify({"erro": "Produto não encontrado"}), 404
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def atualizar(id_produto):
        """Atualizar produto"""
        dados = request.get_json()
        resultado = ProdutoModel.atualizar(id_produto, dados)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def deletar(id_produto):
        """Deletar produto"""
        resultado = ProdutoModel.deletar(id_produto)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def estoque_minimo():
        """Verificar produtos com estoque mínimo"""
        produtos = ProdutoModel.verificar_estoque_minimo()
        return jsonify(produtos), 200
