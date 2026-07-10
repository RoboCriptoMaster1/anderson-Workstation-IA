"""
=====================================================
Workstation Tasks

Task Repository

Versão: 0.4.6

=====================================================

Responsável pelo acesso aos dados de Tarefas.
"""

from app.models.task import Task
from app.repositories.base_repository import BaseRepository


class TaskRepository(BaseRepository[Task]):
    """
    Repositório de Tarefas.
    """

    def __init__(self):
        super().__init__(Task)

    # =====================================================
    # Consultas Específicas
    # =====================================================

    def get_by_project(self, project_id: int):
        """
        Retorna tarefas de um projeto.
        """

        return Task.query.filter_by(
            project_id=project_id
        ).all()

    def get_by_user(self, user_id: int):
        """
        Retorna tarefas de um usuário.
        """

        return Task.query.filter_by(
            user_id=user_id
        ).all()

    def get_by_status(self, status_id: int):
        """
        Retorna tarefas por status.
        """

        return Task.query.filter_by(
            status_id=status_id
        ).all()

    def get_by_category(self, category_id: int):
        """
        Retorna tarefas por categoria.
        """

        return Task.query.filter_by(
            category_id=category_id
        ).all()

    def get_open_tasks(self):
        """
        Retorna tarefas em aberto.
        """

        return Task.query.filter_by(
            completed=False
        ).all()

    def get_completed_tasks(self):
        """
        Retorna tarefas concluídas.
        """

        return Task.query.filter_by(
            completed=True
        ).all()

    def get_overdue_tasks(self):
        """
        Retorna tarefas vencidas.

        (Implementação inicial)
        """

        return Task.query.all()