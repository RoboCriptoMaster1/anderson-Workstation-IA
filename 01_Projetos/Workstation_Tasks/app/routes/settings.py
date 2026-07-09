"""
=====================================================
Workstation Tasks
Módulo de Configurações
Versão: 0.1.0
=====================================================
"""

from flask import Blueprint, render_template

# Blueprint de Configurações
settings_bp = Blueprint(
    "settings",
    __name__,
    url_prefix="/settings"
)


@settings_bp.route("/")
def index():
    """
    Página principal de configurações.
    """
    return render_template("config/index.html")


@settings_bp.route("/profile")
def profile():
    """
    Configurações do perfil do usuário.
    """
    return "<h2>Perfil do Usuário (Em desenvolvimento)</h2>"


@settings_bp.route("/security")
def security():
    """
    Configurações de segurança.
    """
    return "<h2>Segurança (Em desenvolvimento)</h2>"


@settings_bp.route("/appearance")
def appearance():
    """
    Configurações de aparência.
    """
    return "<h2>Aparência (Em desenvolvimento)</h2>"


@settings_bp.route("/system")
def system():
    """
    Configurações gerais do sistema.
    """
    return "<h2>Configurações do Sistema (Em desenvolvimento)</h2>"