"""
=====================================================
Workstation Tasks
Pacote Oficial de Rotas
Versão: 0.1.0
=====================================================

Centraliza todos os Blueprints da aplicação.
"""

# Blueprint Principal
from .main import main_bp

# Blueprint de Autenticação
from .auth import auth_bp

# Blueprint de Projetos
from .projects import projects_bp

# Blueprint de Tarefas
from .tasks import tasks_bp

# Blueprint de Usuários
from .users import users_bp

# Blueprint de Configurações
from .settings import settings_bp

# Blueprints disponíveis para importação
__all__ = [
    "main_bp",
    "auth_bp",
    "projects_bp",
    "tasks_bp",
    "users_bp",
    "settings_bp",
]