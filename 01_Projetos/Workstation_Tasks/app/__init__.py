"""
=====================================================
Workstation Tasks
Application Factory
Versão: 0.3.1
=====================================================
"""

from flask import Flask

from app.config import Config

from app.extensions import (
    init_extensions,
)

# Importa todos os Models
from app.models import *

# Importa os Blueprints
from app.routes import (
    main_bp,
    auth_bp,
    projects_bp,
    tasks_bp,
    users_bp,
    settings_bp,
)


def create_app() -> Flask:
    """
    Cria e configura a aplicação Flask.
    """

    app = Flask(__name__)

    # =====================================================
    # Configurações
    # =====================================================

    app.config.from_object(Config)

    # =====================================================
    # Inicializa as Extensões
    # =====================================================

    init_extensions(app)

    # =====================================================
    # Registro dos Blueprints
    # =====================================================

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(settings_bp)

    return app