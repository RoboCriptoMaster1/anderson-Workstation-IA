"""
=====================================================
Workstation Tasks

Role Repository

Versão: 0.4.6

=====================================================

Responsável pelo acesso aos dados de Perfis.
"""

from app.models.role import Role
from app.repositories.base_repository import BaseRepository


class RoleRepository(BaseRepository[Role]):
    """
    Repositório de Perfis.
    """

    def __init__(self):
        super().__init__(Role)

    # =====================================================
    # Consultas Específicas
    # =====================================================

    def get_by_name(self, name: str):
        """
        Busca um perfil pelo nome.
        """

        return Role.query.filter_by(
            name=name
        ).first()

    def exists_name(self, name: str) -> bool:
        """
        Verifica se o nome do perfil já existe.
        """

        return (
            Role.query.filter_by(name=name)
            .first()
            is not None
        )

    def get_default_role(self):
        """
        Retorna o perfil padrão do sistema.
        """

        return Role.query.order_by(
            Role.id.asc()
        ).first()