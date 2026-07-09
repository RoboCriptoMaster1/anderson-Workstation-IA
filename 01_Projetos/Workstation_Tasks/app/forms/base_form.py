"""
=====================================================
Workstation Tasks

Base Form

Versão: 0.4.5

=====================================================

Classe base para todos os formulários da aplicação.

Todos os formulários deverão herdar desta classe.
"""

from flask_wtf import FlaskForm


class BaseForm(FlaskForm):
    """
    Classe base dos formulários.

    Centraliza comportamentos comuns dos formulários
    da aplicação.
    """

    class Meta:
        csrf = True

    def clean_string(self, value: str) -> str:
        """
        Remove espaços excedentes.

        Parameters
        ----------
        value : str

        Returns
        -------
        str
        """

        if value is None:
            return ""

        return value.strip()

    def clean_email(self, value: str) -> str:
        """
        Normaliza e-mail.

        Parameters
        ----------
        value : str

        Returns
        -------
        str
        """

        if value is None:
            return ""

        return value.strip().lower()

    def populate_object(self, obj):
        """
        Copia automaticamente os dados do formulário
        para um objeto/model.
        """

        for field in self:

            if hasattr(obj, field.name):

                setattr(
                    obj,
                    field.name,
                    field.data
                )

        return obj

    def to_dict(self):
        """
        Retorna os dados do formulário em formato dict.
        """

        return {
            field.name: field.data
            for field in self
        }