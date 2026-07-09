"""
=====================================================
Workstation Tasks

Unique Validator

Versão: 0.4.4

=====================================================

Validações de unicidade no banco de dados.
"""

from __future__ import annotations

from app.extensions import db


class UniqueValidator:
    """
    Responsável por validar unicidade de registros.
    """

    @staticmethod
    def exists(model, field_name: str, value) -> bool:
        """
        Verifica se o valor já existe na tabela.
        """

        field = getattr(model, field_name)

        return db.session.query(
            model.query.filter(field == value).exists()
        ).scalar()

    @staticmethod
    def available(model, field_name: str, value) -> bool:
        """
        Retorna True caso o valor esteja disponível.
        """

        return not UniqueValidator.exists(
            model,
            field_name,
            value
        )