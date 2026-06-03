import json
from urllib.request import Request, urlopen

BASE = 'http://127.0.0.1:5000'

def post(path, payload):
    url = BASE + path
    data = json.dumps(payload).encode('utf-8')
    req = Request(url, data=data, headers={'Content-Type': 'application/json'})
    with urlopen(req) as resp:
        return resp.read().decode('utf-8'), resp.getcode()

def main():
    print('Testando /health')
    with urlopen(BASE + '/health') as r:
        print(r.read().decode())

    # Testar registro
    user = {"nome_completo": "Teste API", "email": "teste_api@example.com", "senha": "senha123"}
    print('\nRegistrando usuário...')
    try:
        body, code = post('/api/auth/registrar', user)
        print('Status:', code)
        print('Resposta:', body)
    except Exception as e:
        print('Erro no registro:', e)

    # Testar login
    print('\nTentando login...')
    try:
        body, code = post('/api/auth/login', {"email": user['email'], "senha": user['senha']})
        print('Status:', code)
        print('Resposta:', body)
    except Exception as e:
        print('Erro no login:', e)

if __name__ == '__main__':
    main()
