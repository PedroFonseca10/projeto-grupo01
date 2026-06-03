import jwt
from functools import wraps
from flask import request, jsonify
from config.configuração import Configuracao

class AutenticacaoMiddleware:
    @staticmethod
    def verificar_token(f):
        """Middleware para verificar token JWT"""
        @wraps(f)
        def decorada(*args, **kwargs):
            token = None
            
            # Verifica no header Authorization
            if 'Authorization' in request.headers:
                try:
                    token = request.headers['Authorization'].split(" ")[1]
                except IndexError:
                    return jsonify({"erro": "Formato de token inválido"}), 401
            
            if not token:
                return jsonify({"erro": "Token não fornecido"}), 401
            
            try:
                payload = jwt.decode(token, Configuracao.JWT_SECRET, algorithms=['HS256'])
                request.user = payload
            except jwt.ExpiredSignatureError:
                return jsonify({"erro": "Token expirado"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"erro": "Token inválido"}), 401
            
            return f(*args, **kwargs)
        return decorada