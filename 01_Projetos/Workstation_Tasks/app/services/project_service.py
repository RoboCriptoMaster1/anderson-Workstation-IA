"""
=====================================================

Workstation Tasks

Serviço de Projetos

Versão: 0.4.7

=====================================================

Responsável pelas regras de negócio relacionadas
aos projetos.

"""

from app.models.project import Project
from app.repositories.project_repository import ProjectRepository
from app.services.base_service import BaseService


class ProjectService(BaseService):
    """
    Serviço responsável pelos projetos.
    """

    def __init__(self):
        super().__init__(ProjectRepository())

    # =====================================================
    # Consultas
    # =====================================================

    def get_by_name(self, name: str):
        """
        Busca um projeto pelo nome.
        """

        return self.repository.get_by_name(
            name.strip()
        )

    def get_active_projects(self):
        """
        Retorna todos os projetos ativos.
        """

        return self.repository.get_active_projects()

    def get_by_owner(self, owner_id: int):
        """
        Retorna todos os projetos de um responsável.
        """

        return self.repository.get_by_owner(owner_id)

    # =====================================================
    # Regras de Negócio
    # =====================================================

    def create_project(
        self,
        name: str,
        description: str,
        owner_id: int
    ) -> Project:
        """
        Cria um novo projeto.
        """

        name = name.strip()

        if self.repository.exists_name(name):

            raise ValueError(
                "Já existe um projeto com esse nome."
            )

        project = Project()

        project.name = name
        project.description = description.strip()
        project.owner_id = owner_id

        return self.repository.create(project)

    def update_project(
        self,
        project: Project,
        **kwargs
    ) -> Project:
        """
        Atualiza um projeto.
        """

        project.update(**kwargs)

        self.repository.update()

        return project

    def activate(
        self,
        project: Project
    ) -> Project:
        """
        Ativa um projeto.
        """

        project.active = True

        self.repository.update()

        return project

    def deactivate(
        self,
        project: Project
    ) -> Project:
        """
        Desativa um projeto.
        """

        project.active = False

        self.repository.update()

        return project