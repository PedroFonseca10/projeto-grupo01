import jwt
from datetime import datetime, timedelta
from config.configuração import Configuracao

class JwtService:
    @staticmethod
    def gerar_token(client_id):
        payload = {
            'client_id': client_id,
            'exp': datetime.utcnow() + timedelta(hours=1)  # Token válido por 1 hora
        }
        token = jwt.encode(payload, Configuracao.JWT_SECRET, algorithm='HS256')
        return token