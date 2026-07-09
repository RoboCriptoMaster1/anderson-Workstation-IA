"""
=====================================================
Workstation Tasks
Base Validator

Versão: 0.4.4
=====================================================

Classe base para todos os validadores do sistema.
"""

from __future__ import annotations


class BaseValidator:
    """
    Classe base de validação.

    Todos os validadores do sistema herdarão desta classe.
    """

    @staticmethod
    def is_empty(value) -> bool:
        """
        Verifica se um valor está vazio.
        """

        if value is None:
            return True

        if isinstance(value, str):
            return value.strip() == ""

        return False

    @staticmethod
    def normalize(value: str) -> str:
        """
        Remove espaços extras.
        """

        return value.strip()

    @staticmethod
    def normalize_lower(value: str) -> str:
        """
        Remove espaços e converte para minúsculo.
        """

        return value.strip().lower()