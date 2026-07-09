"""
=====================================================
Workstation Tasks
Módulo de Tarefas
Versão: 0.1.0
=====================================================
"""

from flask import Blueprint, render_template

# Blueprint de Tarefas
tasks_bp = Blueprint(
    "tasks",
    __name__,
    url_prefix="/tasks"
)


@tasks_bp.route("/")
def index():
    """
    Lista todas as tarefas.
    """
    return render_template("tarefas/index.html")


@tasks_bp.route("/new")
def new():
    """
    Formulário para nova tarefa.
    """
    return "<h2>Nova Tarefa (Em desenvolvimento)</h2>"


@tasks_bp.route("/edit/<int:id>")
def edit(id):
    """
    Editar tarefa.
    """
    return f"<h2>Editando Tarefa #{id} (Em desenvolvimento)</h2>"


@tasks_bp.route("/delete/<int:id>")
def delete(id):
    """
    Excluir tarefa.
    """
    return f"<h2>Excluindo Tarefa #{id} (Em desenvolvimento)</h2>"


@tasks_bp.route("/completed")
def completed():
    """
    Lista de tarefas concluídas.
    """
    return "<h2>Tarefas Concluídas (Em desenvolvimento)</h2>"


@tasks_bp.route("/pending")
def pending():
    """
    Lista de tarefas pendentes.
    """
    return "<h2>Tarefas Pendentes (Em desenvolvimento)</h2>"