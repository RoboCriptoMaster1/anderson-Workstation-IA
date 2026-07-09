"""
=====================================================
Workstation Tasks
Módulo de Usuários
Versão: 0.1.0
=====================================================
"""

from flask import Blueprint, render_template
from flask_login import login_required

# Blueprint de Usuários
users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users"
)


@users_bp.route("/")
@login_required
def index():
    
    """
    Lista todos os usuários.
    """
    return render_template("users/index.html")


@users_bp.route("/new")
def new():
    """
    Formulário para novo usuário.
    """
    return "<h2>Novo Usuário (Em desenvolvimento)</h2>"


@users_bp.route("/profile/<int:id>")
def profile(id):
    """
    Perfil do usuário.
    """
    return f"<h2>Perfil do Usuário #{id} (Em desenvolvimento)</h2>"


@users_bp.route("/edit/<int:id>")
def edit(id):
    """
    Editar usuário.
    """
    return f"<h2>Editando Usuário #{id} (Em desenvolvimento)</h2>"


@users_bp.route("/delete/<int:id>")
def delete(id):
    """
    Excluir usuário.
    """
    return f"<h2>Excluindo Usuário #{id} (Em desenvolvimento)</h2>"