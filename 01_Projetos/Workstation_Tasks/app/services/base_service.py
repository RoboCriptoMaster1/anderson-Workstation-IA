"""
=====================================================
Workstation Tasks

Base Service

Versão: 0.4.7

=====================================================

Classe base responsável pelas regras de negócio
comuns da aplicação.

Todos os Services deverão herdar desta classe.
"""

from __future__ import annotations

from typing import Generic
from typing import TypeVar

T = TypeVar("T")


class BaseService(Generic[T]):
    """
    Classe base dos Services.
    """

    def __init__(self, repository):
        """
        Inicializa o Service.

        Parameters
        ----------
        repository
            Repositório responsável pelo acesso aos dados.
        """

        self.repository = repository

    # =====================================================
    # Consultas
    # =====================================================

    def get_all(self):
        """
        Retorna todos os registros.
        """

        return self.repository.get_all()

    def get_by_id(self, record_id: int):
        """
        Busca um registro pelo ID.
        """

        return self.repository.get_by_id(record_id)

    def first(self):
        """
        Retorna o primeiro registro.
        """

        return self.repository.first()

    def count(self) -> int:
        """
        Retorna a quantidade de registros.
        """

        return self.repository.count()

    def exists(self, record_id: int) -> bool:
        """
        Verifica se um registro existe.
        """

        return self.repository.exists(record_id)

    def paginate(
        self,
        page: int = 1,
        per_page: int = 10
    ):
        """
        Retorna uma paginação.
        """

        return self.repository.paginate(
            page=page,
            per_page=per_page
        )

    # =====================================================
    # Persistência
    # =====================================================

    def create(self, obj: T):
        """
        Cria um novo registro.
        """

        return self.repository.create(obj)

    def update(self):
        """
        Salva alterações.
        """

        return self.repository.update()

    def delete(self, obj: T):
        """
        Remove um registro.
        """

        return self.repository.delete(obj)

    # =====================================================
    # Transações
    # =====================================================

    def commit(self):
        """
        Efetua commit.
        """

        self.repository.commit()

    def rollback(self):
        """
        Efetua rollback.
        """

        self.repository.rollback()