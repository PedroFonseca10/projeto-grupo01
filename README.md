# Projeto Backend + Frontend KoreArmazen

## O que foi feito

- Copiado o front-end da tela de cadastro (`frontend/kore-tela-de-cadastro`) para o workspace.
- Atualizei o backend Flask (`app.py`) para servir o front-end na raiz `/`.
- Conectei o formulário de cadastro/login com a API:
  - `POST /api/auth/registrar`
  - `POST /api/auth/login`
- Adicionei um `requirements.txt` com as dependências necessárias.

## Estrutura de front-end

- `frontend/kore-tela-de-cadastro/index.html`
- `frontend/kore-tela-de-cadastro/style.css`
- `frontend/kore-tela-de-cadastro/script.js`

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure o banco de dados no arquivo `.env`:

```env
DB_SERVER=localhost
DB_NAME=ControleEstoque
DB_USER=sa
DB_PASSWORD=sua_senha
JWT_SECRET=sua_chave_secreta
CLIENT_ID=meu_cliente
CLIENT_SECRET=segredo_super
```

3. Execute o backend:

```bash
python app.py
```

4. Abra o navegador em:

```text
http://localhost:5000
```

## Observações

- O front-end agora roda pelo mesmo servidor Flask para evitar problemas de CORS.
- O backend usa CORS e a API está disponível em `/api`.
- Para testar login, você deve primeiro criar um usuário via formulário ou via `POST /api/auth/registrar`.
