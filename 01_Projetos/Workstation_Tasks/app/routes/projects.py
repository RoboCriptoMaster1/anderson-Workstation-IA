"""
=====================================================
Workstation Tasks
Módulo de Projetos
Versão: 0.1.0
=====================================================
"""

from flask import Blueprint, render_template
from flask_login import login_required

# Blueprint de Projetos
projects_bp = Blueprint(
    "projects",
    __name__,
    url_prefix="/projects"
)


@projects_bp.route("/")
@login_required
def index():
    
    """
    Lista todos os projetos.
    """
    return render_template("projetos/index.html")


@projects_bp.route("/new")
def new():
    """
    Formulário para novo projeto.
    """
    return "<h2>Novo Projeto (Em desenvolvimento)</h2>"


@projects_bp.route("/edit/<int:id>")
def edit(id):
    """
    Editar projeto.
    """
    return f"<h2>Editando Projeto #{id} (Em desenvolvimento)</h2>"


@projects_bp.route("/delete/<int:id>")
def delete(id):
    """
    Excluir projeto.
    """
    return f"<h2>Excluindo Projeto #{id} (Em desenvolvimento)</h2>"