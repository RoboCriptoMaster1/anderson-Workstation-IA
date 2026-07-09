"""
=====================================================
Workstation Tasks

Status Repository

Versão: 0.4.6

=====================================================

Responsável pelo acesso aos dados de Status.
"""

from app.models.status import Status
from app.repositories.base_repository import BaseRepository


class StatusRepository(BaseRepository[Status]):
    """
    Repositório de Status.
    """

    def __init__(self):
        super().__init__(Status)

    # =====================================================
    # Consultas Específicas
    # =====================================================

    def get_by_name(self, name: str):
        """
        Busca um status pelo nome.
        """

        return Status.query.filter_by(
            name=name
        ).first()

    def exists_name(self, name: str) -> bool:
        """
        Verifica se o status já existe.
        """

        return (
            Status.query.filter_by(name=name)
            .first()
            is not None
        )

    def search(self, text: str):
        """
        Pesquisa status pelo nome.
        """

        return Status.query.filter(
            Status.name.ilike(f"%{text}%")
        ).all()

    def ordered(self):
        """
        Retorna os status ordenados por nome.
        """

        return Status.query.order_by(
            Status.name.asc()
        ).all()