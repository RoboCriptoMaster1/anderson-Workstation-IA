"""
=====================================================
Workstation Tasks

String Validator

Versão: 0.4.4

=====================================================

Validações para textos.
"""

from __future__ import annotations

from app.validators.base_validator import BaseValidator


class StringValidator(BaseValidator):
    """
    Validações para strings.
    """

    @staticmethod
    def min_length(value: str, minimum: int) -> bool:
        """
        Verifica tamanho mínimo.
        """

        if BaseValidator.is_empty(value):
            return False

        return len(value.strip()) >= minimum

    @staticmethod
    def max_length(value: str, maximum: int) -> bool:
        """
        Verifica tamanho máximo.
        """

        if BaseValidator.is_empty(value):
            return False

        return len(value.strip()) <= maximum

    @staticmethod
    def between(value: str, minimum: int, maximum: int) -> bool:
        """
        Verifica intervalo de caracteres.
        """

        if BaseValidator.is_empty(value):
            return False

        size = len(value.strip())

        return minimum <= size <= maximum

    @staticmethod
    def only_letters(value: str) -> bool:
        """
        Permite apenas letras e espaços.
        """

        if BaseValidator.is_empty(value):
            return False

        return all(
            character.isalpha() or character.isspace()
            for character in value
        )

    @staticmethod
    def only_numbers(value: str) -> bool:
        """
        Permite apenas números.
        """

        if BaseValidator.is_empty(value):
            return False

        return value.isdigit()

    @staticmethod
    def only_alphanumeric(value: str) -> bool:
        """
        Permite letras e números.
        """

        if BaseValidator.is_empty(value):
            return False

        return value.replace(" ", "").isalnum()