"""
=====================================================
Workstation Tasks
Módulo de Autenticação
Versão: 0.1.0
=====================================================
"""

from flask import Blueprint, render_template

# Blueprint de autenticação
auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/login")
def login():
    """
    Exibe a tela de login.
    """
    return render_template("login/login.html")


@auth_bp.route("/logout")
def logout():
    """
    Logout do usuário.
    """
    return "<h2>Logout (Em desenvolvimento)</h2>"


@auth_bp.route("/forgot-password")
def forgot_password():
    """
    Recuperação de senha.
    """
    return "<h2>Recuperação de Senha (Em desenvolvimento)</h2>"