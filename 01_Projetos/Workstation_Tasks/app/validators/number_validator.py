"""
=====================================================
Workstation Tasks

Number Validator

Versão: 0.4.4

=====================================================

Validações numéricas.
"""

from __future__ import annotations

from app.validators.base_validator import BaseValidator


class NumberValidator(BaseValidator):
    """
    Validação de números.
    """

    @staticmethod
    def is_integer(value) -> bool:
        """
        Verifica se o valor é um inteiro.
        """

        try:

            int(value)

            return True

        except (TypeError, ValueError):

            return False

    @staticmethod
    def is_float(value) -> bool:
        """
        Verifica se o valor é decimal.
        """

        try:

            float(value)

            return True

        except (TypeError, ValueError):

            return False

    @staticmethod
    def between(value, minimum, maximum) -> bool:
        """
        Verifica intervalo numérico.
        """

        try:

            value = float(value)

            return minimum <= value <= maximum

        except (TypeError, ValueError):

            return False

    @staticmethod
    def positive(value) -> bool:
        """
        Verifica se o número é positivo.
        """

        try:

            return float(value) > 0

        except (TypeError, ValueError):

            return False

    @staticmethod
    def negative(value) -> bool:
        """
        Verifica se o número é negativo.
        """

        try:

            return float(value) < 0

        except (TypeError, ValueError):

            return False