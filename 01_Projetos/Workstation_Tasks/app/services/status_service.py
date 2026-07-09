"""
=====================================================
Workstation Tasks

Serviço de Status

Versão: 0.4.7

=====================================================

Responsável pelas regras de negócio dos status.
"""

from app.models.status import Status
from app.repositories.status_repository import StatusRepository
from app.services.base_service import BaseService


class StatusService(BaseService):
    """
    Serviço responsável pelos status.
    """

    def __init__(self):
        super().__init__(StatusRepository())

    def get_by_name(self, name: str):
        """
        Busca um status pelo nome.
        """

        return self.repository.get_by_name(name)

    def create_status(
        self,
        name: str,
        color: str = "#0d6efd"
    ) -> Status:
        """
        Cria um novo status.
        """

        if self.repository.exists_name(name):

            raise ValueError(
                "Status já cadastrado."
            )

        status = Status()

        status.name = name.strip()
        status.color = color

        return self.repository.create(status)