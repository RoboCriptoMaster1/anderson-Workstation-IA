"""
=====================================================
Workstation Tasks
Configuração Principal da Aplicação
Versão: 0.1.0
=====================================================
"""

from flask import Flask

# Importação centralizada dos Blueprints
from app.routes import (
    main_bp,
    auth_bp,
    projects_bp,
    tasks_bp,
    users_bp,
    settings_bp,
)


def create_app():
    """
    Cria e configura a aplicação Flask.
    """

    app = Flask(__name__)

    # =====================================================
    # Configurações Básicas
    # =====================================================

    app.config["SECRET_KEY"] = "workstation_tasks_dev"

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