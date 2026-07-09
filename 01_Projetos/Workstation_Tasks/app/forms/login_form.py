"""
=====================================================
Workstation Tasks

Login Form

Versão: 0.4.5

=====================================================

Formulário oficial de autenticação.
"""

from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField

from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import Length

from app.forms.base_form import BaseForm


class LoginForm(BaseForm):
    """
    Formulário de Login.
    """

    email = StringField(
        "E-mail",
        validators=[
            DataRequired(
                message="Informe seu e-mail."
            ),
            Email(
                message="Informe um e-mail válido."
            ),
            Length(
                max=120,
                message="O e-mail é muito longo."
            )
        ],
        render_kw={
            "placeholder": "Digite seu e-mail",
            "autocomplete": "email",
            "class": "form-control"
        }
    )

    password = PasswordField(
        "Senha",
        validators=[
            DataRequired(
                message="Informe sua senha."
            ),
            Length(
                min=8,
                max=255,
                message="Senha inválida."
            )
        ],
        render_kw={
            "placeholder": "Digite sua senha",
            "autocomplete": "current-password",
            "class": "form-control"
        }
    )

    submit = SubmitField(
        "Entrar"
    )