"""
=====================================================
Workstation Tasks

Serviço de Tarefas

Versão: 0.4.7

=====================================================

Responsável pelas regras de negócio das tarefas.
"""

from app.models.task import Task
from app.repositories.task_repository import TaskRepository
from app.services.base_service import BaseService


class TaskService(BaseService):
    """
    Serviço responsável pelas tarefas.
    """

    def __init__(self):
        super().__init__(TaskRepository())

    # =====================================================
    # Consultas
    # =====================================================

    def get_by_project(self, project_id: int):
        """
        Retorna todas as tarefas de um projeto.
        """

        return self.repository.get_by_project(project_id)

    def get_by_user(self, user_id: int):
        """
        Retorna todas as tarefas de um usuário.
        """

        return self.repository.get_by_user(user_id)

    def get_by_status(self, status_id: int):
        """
        Retorna tarefas por status.
        """

        return self.repository.get_by_status(status_id)

    def get_by_category(self, category_id: int):
        """
        Retorna tarefas por categoria.
        """

        return self.repository.get_by_category(category_id)

    # =====================================================
    # Regras de Negócio
    # =====================================================

    def create_task(self, task: Task) -> Task:
        """
        Cria uma nova tarefa.
        """

        return self.repository.create(task)

    def conclude_task(self, task: Task):
        """
        Marca uma tarefa como concluída.
        """

        task.completed = True

        self.repository.update()

        return task

    def reopen_task(self, task: Task):
        """
        Reabre uma tarefa.
        """

        task.completed = False

        self.repository.update()

        return task