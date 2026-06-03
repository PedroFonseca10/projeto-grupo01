from flask import Blueprint
from controllers.autenticacao_controller import AutenticacaoController
from controllers.fornecedor_controller import FornecedorController
from controllers.produto_controller import ProdutoController
from controllers.usuario_controller import UsuarioController
from controllers.entrada_controller import EntradaController
from controllers.saida_controller import SaidaController

# Criar blueprints
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Rotas de Autenticação (Sem proteção JWT)
api_bp.route('/auth/login', methods=['POST'], endpoint='auth_login')(AutenticacaoController.login)
api_bp.route('/auth/registrar', methods=['POST'], endpoint='auth_registrar')(AutenticacaoController.registrar)

# Rotas de Fornecedores (Com proteção JWT)
api_bp.route('/fornecedores', methods=['POST'], endpoint='fornecedores_criar')(FornecedorController.criar)
api_bp.route('/fornecedores', methods=['GET'], endpoint='fornecedores_listar')(FornecedorController.listar)
api_bp.route('/fornecedores/<int:id_fornecedor>', methods=['GET'], endpoint='fornecedores_obter')(FornecedorController.obter)
api_bp.route('/fornecedores/<int:id_fornecedor>', methods=['PUT'], endpoint='fornecedores_atualizar')(FornecedorController.atualizar)
api_bp.route('/fornecedores/<int:id_fornecedor>', methods=['DELETE'], endpoint='fornecedores_deletar')(FornecedorController.deletar)

# Rotas de Produtos (Com proteção JWT)
api_bp.route('/produtos', methods=['POST'], endpoint='produtos_criar')(ProdutoController.criar)
api_bp.route('/produtos', methods=['GET'], endpoint='produtos_listar')(ProdutoController.listar)
api_bp.route('/produtos/<int:id_produto>', methods=['GET'], endpoint='produtos_obter')(ProdutoController.obter)
api_bp.route('/produtos/<int:id_produto>', methods=['PUT'], endpoint='produtos_atualizar')(ProdutoController.atualizar)
api_bp.route('/produtos/<int:id_produto>', methods=['DELETE'], endpoint='produtos_deletar')(ProdutoController.deletar)
api_bp.route('/produtos/estoque/minimo', methods=['GET'], endpoint='produtos_estoque_minimo')(ProdutoController.estoque_minimo)

# Rotas de Usuários (Com proteção JWT)
api_bp.route('/usuarios', methods=['POST'], endpoint='usuarios_criar')(UsuarioController.criar)
api_bp.route('/usuarios', methods=['GET'], endpoint='usuarios_listar')(UsuarioController.listar)
api_bp.route('/usuarios/<int:id_usuario>', methods=['GET'], endpoint='usuarios_obter')(UsuarioController.obter)
api_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'], endpoint='usuarios_atualizar')(UsuarioController.atualizar)
api_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'], endpoint='usuarios_deletar')(UsuarioController.deletar)

# Rotas de Entradas (Com proteção JWT)
api_bp.route('/entradas', methods=['POST'], endpoint='entradas_criar')(EntradaController.criar)
api_bp.route('/entradas', methods=['GET'], endpoint='entradas_listar')(EntradaController.listar)
api_bp.route('/entradas/<int:id_entrada>', methods=['GET'], endpoint='entradas_obter')(EntradaController.obter)
api_bp.route('/entradas/<int:id_entrada>', methods=['PUT'], endpoint='entradas_atualizar')(EntradaController.atualizar)
api_bp.route('/entradas/<int:id_entrada>', methods=['DELETE'], endpoint='entradas_deletar')(EntradaController.deletar)

# Rotas de Saídas (Com proteção JWT)
api_bp.route('/saidas', methods=['POST'], endpoint='saidas_criar')(SaidaController.criar)
api_bp.route('/saidas', methods=['GET'], endpoint='saidas_listar')(SaidaController.listar)
api_bp.route('/saidas/<int:id_saida>', methods=['GET'], endpoint='saidas_obter')(SaidaController.obter)
api_bp.route('/saidas/<int:id_saida>', methods=['PUT'], endpoint='saidas_atualizar')(SaidaController.atualizar)
api_bp.route('/saidas/<int:id_saida>', methods=['DELETE'], endpoint='saidas_deletar')(SaidaController.deletar)
