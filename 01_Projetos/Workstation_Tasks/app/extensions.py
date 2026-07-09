"""
=====================================================
Workstation Tasks
Extensões da Aplicação
Versão: 0.3.1
=====================================================
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# =====================================================
# Banco de Dados
# =====================================================

db = SQLAlchemy()

# =====================================================
# Migrations
# =====================================================

migrate = Migrate()

# =====================================================
# Login
# =====================================================

login_manager = LoginManager()


def init_extensions(app: Flask) -> None:
    """
    Inicializa todas as extensões da aplicação.
    """

    # Banco de Dados
    db.init_app(app)

    # Migrations
    migrate.init_app(app, db)

    # Login
    login_manager.init_app(app)

    # Configurações do Flask-Login
    login_manager.login_view = "auth.login"  # type: ignore[attr-defined]
    login_manager.login_message = "Faça login para acessar o sistema."  # type: ignore[attr-defined]
    login_manager.login_message_category = "warning"  # type: ignore[attr-defined]