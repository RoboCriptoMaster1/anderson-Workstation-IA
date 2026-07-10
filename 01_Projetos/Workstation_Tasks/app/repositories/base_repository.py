"""
=====================================================

Workstation Tasks

Base Repository

Versão: 0.5.1

=====================================================

Classe base para todos os repositórios da aplicação.

Responsável pelas operações comuns de acesso ao banco
de dados utilizando SQLAlchemy.

"""

from __future__ import annotations

from typing import Generic, Type, TypeVar

from app.extensions import db

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """
    Repositório base.

    Todos os repositórios herdam desta classe.
    """

    def __init__(self, model: Type[T]):
        self.model = model

    # =====================================================
    # Consultas
    # =====================================================

    def get_all(self):
        """
        Retorna todos os registros.
        """

        return db.session.query(self.model).all()

    def get_by_id(self, record_id: int):
        """
        Busca um registro pelo ID.
        """

        return db.session.get(
            self.model,
            record_id
        )

    def first(self):
        """
        Retorna o primeiro registro.
        """

        return db.session.query(self.model).first()

    def count(self) -> int:
        """
        Retorna a quantidade de registros.
        """

        return db.session.query(self.model).count()

    def exists(self, record_id: int) -> bool:
        """
        Verifica se um registro existe.
        """

        return self.get_by_id(record_id) is not None

    # =====================================================
    # Persistência
    # =====================================================

    def create(self, obj: T) -> T:
        """
        Persiste um novo objeto.
        """

        db.session.add(obj)
        db.session.commit()

        return obj

    def save(self, obj: T) -> T:
        """
        Salva um objeto.
        """

        db.session.add(obj)
        db.session.commit()

        return obj

    def update(self) -> None:
        """
        Persiste alterações.
        """

        db.session.commit()

    def delete(self, obj: T) -> None:
        """
        Remove um objeto.
        """

        db.session.delete(obj)
        db.session.commit()

    # =====================================================
    # Transações
    # =====================================================

    def commit(self) -> None:
        """
        Efetua commit manual.
        """

        db.session.commit()

    def rollback(self) -> None:
        """
        Desfaz alterações.
        """

        db.session.rollback()

    # =====================================================
    # Utilidades
    # =====================================================

    def paginate(
        self,
        page: int = 1,
        per_page: int = 10
    ):
        """
        Paginação simples.
        """

        query = db.session.query(self.model)

        return query.offset(
            (page - 1) * per_page
        ).limit(
            per_page
        ).all()

    def refresh(self, obj: T) -> None:
        """
        Atualiza um objeto com os dados do banco.
        """

        db.session.refresh(obj)

    def flush(self) -> None:
        """
        Executa flush na sessão.
        """

        db.session.flush()