from config.configuração import Configuracao

class ClienteModel:
    @staticmethod
    def validar_cliente(client_id, client_secret):
        return client_id == Configuracao.CLIENT_ID and client_secret == Configuracao.CLIENT_SECRET