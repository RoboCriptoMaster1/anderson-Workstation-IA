"""
=====================================================
Workstation Tasks

Serviço de Perfis

Versão: 0.4.7

=====================================================

Responsável pelas regras de negócio dos perfis
(Role).
"""

from app.models.role import Role
from app.repositories.role_repository import RoleRepository
from app.services.base_service import BaseService


class RoleService(BaseService):
    """
    Serviço de Perfis.
    """

    def __init__(self):
        super().__init__(RoleRepository())

    def get_by_name(self, name: str):
        """
        Busca perfil pelo nome.
        """

        return self.repository.get_by_name(name)

    def create_role(
        self,
        name: str,
        description: str = ""
    ) -> Role:
        """
        Cria um novo perfil.
        """

        if self.repository.exists_name(name):

            raise ValueError(
                "Este perfil já existe."
            )

        role = Role()

        role.name = name.strip()
        role.description = description.strip()

        return self.repository.create(role)