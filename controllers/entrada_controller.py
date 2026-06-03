from flask import request, jsonify
from models.entrada_model import EntradaModel
from middleware.autenticacao_middleware import AutenticacaoMiddleware

class EntradaController:
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def criar():
        """Criar novo registro de entrada"""
        dados = request.get_json()
        resultado = EntradaModel.criar(dados)
        status = 201 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def listar():
        """Listar todos os registros de entrada"""
        entradas = EntradaModel.listar()
        return jsonify(entradas), 200
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def obter(id_entrada):
        """Obter registro de entrada específico"""
        entrada = EntradaModel.obter_por_id(id_entrada)
        if entrada:
            return jsonify(entrada), 200
        return jsonify({"erro": "Entrada não encontrada"}), 404
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def atualizar(id_entrada):
        """Atualizar registro de entrada"""
        dados = request.get_json()
        resultado = EntradaModel.atualizar(id_entrada, dados)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def deletar(id_entrada):
        """Deletar registro de entrada"""
        resultado = EntradaModel.deletar(id_entrada)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
