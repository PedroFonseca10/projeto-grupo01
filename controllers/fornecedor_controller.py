from flask import request, jsonify
from models.fornecedor_model import FornecedorModel
from middleware.autenticacao_middleware import AutenticacaoMiddleware

class FornecedorController:
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def criar():
        """Criar novo fornecedor"""
        dados = request.get_json()
        resultado = FornecedorModel.criar(dados)
        status = 201 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def listar():
        """Listar todos os fornecedores"""
        fornecedores = FornecedorModel.listar()
        return jsonify(fornecedores), 200
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def obter(id_fornecedor):
        """Obter fornecedor específico"""
        fornecedor = FornecedorModel.obter_por_id(id_fornecedor)
        if fornecedor:
            return jsonify(fornecedor), 200
        return jsonify({"erro": "Fornecedor não encontrado"}), 404
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def atualizar(id_fornecedor):
        """Atualizar fornecedor"""
        dados = request.get_json()
        resultado = FornecedorModel.atualizar(id_fornecedor, dados)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def deletar(id_fornecedor):
        """Deletar fornecedor"""
        resultado = FornecedorModel.deletar(id_fornecedor)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
