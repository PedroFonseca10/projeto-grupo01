from flask import request, jsonify
from models.usuario_model import UsuarioModel
from services.jwt_service import JwtService

class AutenticacaoController:
    @staticmethod
    def login():
        """Endpoint para login de usuários"""
        dados = request.get_json()
        
        if not dados or not dados.get('email') or not dados.get('senha'):
            return jsonify({"erro": "Email e senha são obrigatórios"}), 400
        
        usuario = UsuarioModel.autenticar(dados.get('email'), dados.get('senha'))
        
        if usuario:
            token = JwtService.gerar_token(usuario['id_cad_usuario'])
            return jsonify({
                "sucesso": True,
                "token": token,
                "usuario": {
                    "id": usuario['id_cad_usuario'],
                    "nome": usuario['nome_completo'],
                    "email": usuario['email']
                }
            }), 200
        
        return jsonify({"erro": "Email ou senha inválidos"}), 401
    
    @staticmethod
    def registrar():
        """Endpoint para registrar novo usuário"""
        dados = request.get_json()
        
        if not dados or not dados.get('email') or not dados.get('senha'):
            return jsonify({"erro": "Email e senha são obrigatórios"}), 400
        
        resultado = UsuarioModel.criar(dados)
        
        if resultado.get('sucesso'):
            return jsonify(resultado), 201
        else:
            return jsonify(resultado), 400