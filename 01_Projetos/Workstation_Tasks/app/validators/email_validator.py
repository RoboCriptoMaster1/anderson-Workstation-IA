"""
=====================================================
Workstation Tasks

Email Validator

Versão: 0.4.4

=====================================================

Validação de e-mails.
"""

from __future__ import annotations

from email_validator import EmailNotValidError
from email_validator import validate_email

from app.validators.base_validator import BaseValidator


class EmailValidator(BaseValidator):
    """
    Validação de e-mails.
    """

    @staticmethod
    def is_valid(email: str) -> bool:
        """
        Verifica se um e-mail é válido.
        """

        if BaseValidator.is_empty(email):
            return False

        try:

            validate_email(
                email.strip(),
                check_deliverability=False
            )

            return True

        except EmailNotValidError:

            return False

    @staticmethod
    def normalize(email: str) -> str:
        """
        Normaliza um e-mail.
        """

        return email.strip().lower()