from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from routes.rotas import api_bp
import os

# Inicializar aplicação Flask
app = Flask(__name__)

# Configurações
app.config['JSON_SORT_KEYS'] = False

# Ativar CORS
CORS(app)

# ========================================
# ROTAS DE ARQUIVOS ESTÁTICOS
# ========================================

@app.route('/assets/<path:arquivo>')
def serve_static(arquivo):

    caminho_completo = os.path.join(
        app.root_path,
        'frontend',
        arquivo
    )

    if os.path.isfile(caminho_completo):

        pasta = os.path.dirname(caminho_completo)
        nome = os.path.basename(caminho_completo)

        return send_from_directory(
            pasta,
            nome
        )

    return jsonify({"erro": "Arquivo não encontrado"}), 404

# ========================================
# ROTAS DE PÁGINAS HTML
# ========================================

@app.route('/', methods=['GET'])
def index():
    """Página inicial - tela de cadastro"""
    return send_from_directory('frontend/kore-tela-de-cadastro', 'index.html')

@app.route('/sistema', methods=['GET'])
def sistema():
    """Página do sistema após login"""
    return send_from_directory('frontend/kore-sistema', 'index.html')

@app.route('/apresentacao', methods=['GET'])
def apresentacao():
    """Página de apresentação"""
    return send_from_directory('frontend/kore-apresentacao', 'index.html')

# ========================================
# API BLUEPRINT (APÓS AS ROTAS DE ARQUIVOS)
# ========================================

app.register_blueprint(api_bp)

# ========================================
# ROTAS UTILITÁRIAS
# ========================================

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "OK", "mensagem": "API funcionando"}), 200

# ========================================
# HANDLERS DE ERRO
# ========================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({"erro": "Rota não encontrada"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"erro": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
