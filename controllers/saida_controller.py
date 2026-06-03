from flask import request, jsonify
from models.saida_model import SaidaModel
from middleware.autenticacao_middleware import AutenticacaoMiddleware

class SaidaController:
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def criar():
        """Criar novo registro de saída"""
        dados = request.get_json()
        resultado = SaidaModel.criar(dados)
        status = 201 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def listar():
        """Listar todos os registros de saída"""
        saidas = SaidaModel.listar()
        return jsonify(saidas), 200
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def obter(id_saida):
        """Obter registro de saída específico"""
        saida = SaidaModel.obter_por_id(id_saida)
        if saida:
            return jsonify(saida), 200
        return jsonify({"erro": "Saída não encontrada"}), 404
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def atualizar(id_saida):
        """Atualizar registro de saída"""
        dados = request.get_json()
        resultado = SaidaModel.atualizar(id_saida, dados)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def deletar(id_saida):
        """Deletar registro de saída"""
        resultado = SaidaModel.deletar(id_saida)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
