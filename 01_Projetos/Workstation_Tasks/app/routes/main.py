"""
=====================================================
Workstation Tasks
Rotas Principais
Versão: 0.1.0
=====================================================
"""

from flask import Blueprint, render_template

# Blueprint principal
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """
    Página inicial da aplicação.
    """
    return render_template("dashboard/index.html")