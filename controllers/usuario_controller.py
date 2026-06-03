from flask import request, jsonify
from models.usuario_model import UsuarioModel
from middleware.autenticacao_middleware import AutenticacaoMiddleware

class UsuarioController:
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def criar():
        """Criar novo usuário"""
        dados = request.get_json()
        resultado = UsuarioModel.criar(dados)
        status = 201 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def listar():
        """Listar todos os usuários"""
        usuarios = UsuarioModel.listar()
        return jsonify(usuarios), 200
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def obter(id_usuario):
        """Obter usuário específico"""
        usuario = UsuarioModel.obter_por_id(id_usuario)
        if usuario:
            return jsonify(usuario), 200
        return jsonify({"erro": "Usuário não encontrado"}), 404
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def atualizar(id_usuario):
        """Atualizar usuário"""
        dados = request.get_json()
        resultado = UsuarioModel.atualizar(id_usuario, dados)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
    
    @staticmethod
    @AutenticacaoMiddleware.verificar_token
    def deletar(id_usuario):
        """Deletar usuário"""
        resultado = UsuarioModel.deletar(id_usuario)
        status = 200 if resultado.get('sucesso') else 400
        return jsonify(resultado), status
