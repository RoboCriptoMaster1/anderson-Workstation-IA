"""
=====================================================
Workstation Tasks

Date Validator

Versão: 0.4.4

=====================================================

Validações para datas e horários.
"""

from __future__ import annotations

from datetime import date
from datetime import datetime

from app.validators.base_validator import BaseValidator


class DateValidator(BaseValidator):
    """
    Classe responsável pelas validações de datas.
    """

    @staticmethod
    def is_valid(date_string: str, format: str = "%Y-%m-%d") -> bool:
        """
        Verifica se a data é válida.
        """

        if BaseValidator.is_empty(date_string):
            return False

        try:

            datetime.strptime(date_string, format)

            return True

        except ValueError:

            return False

    @staticmethod
    def is_future(date_string: str, format: str = "%Y-%m-%d") -> bool:
        """
        Verifica se a data é futura.
        """

        if not DateValidator.is_valid(date_string, format):
            return False

        value = datetime.strptime(date_string, format).date()

        return value > date.today()

    @staticmethod
    def is_past(date_string: str, format: str = "%Y-%m-%d") -> bool:
        """
        Verifica se a data é passada.
        """

        if not DateValidator.is_valid(date_string, format):
            return False

        value = datetime.strptime(date_string, format).date()

        return value < date.today()

    @staticmethod
    def today() -> date:
        """
        Retorna a data atual.
        """

        return date.today()