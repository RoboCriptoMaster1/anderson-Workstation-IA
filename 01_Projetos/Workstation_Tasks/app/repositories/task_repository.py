"""
=====================================================
Workstation Tasks

Project Repository

Versão: 0.4.6

=====================================================

Responsável pelo acesso aos dados de Projetos.
"""

from app.models.project import Project
from app.repositories.base_repository import BaseRepository


class ProjectRepository(BaseRepository[Project]):
    """
    Repositório de Projetos.
    """

    def __init__(self):
        super().__init__(Project)

    # =====================================================
    # Consultas Específicas
    # =====================================================

    def get_by_name(self, name: str):
        """
        Busca um projeto pelo nome.
        """

        return Project.query.filter_by(
            name=name
        ).first()

    def exists_name(self, name: str) -> bool:
        """
        Verifica se o projeto já existe.
        """

        return (
            Project.query.filter_by(name=name)
            .first()
            is not None
        )

    def get_active_projects(self):
        """
        Retorna projetos ativos.
        """

        return Project.query.filter_by(
            active=True
        ).all()

    def get_by_owner(self, owner_id: int):
        """
        Retorna projetos de um responsável.
        """

        return Project.query.filter_by(
            owner_id=owner_id
        ).all()