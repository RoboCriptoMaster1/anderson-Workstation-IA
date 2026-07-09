"""
=====================================================
Workstation Tasks

User Form

Versão: 0.4.5

=====================================================

Formulário de Usuários.
"""

from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField

from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import Optional

from app.forms.base_form import BaseForm


class UserForm(BaseForm):
    """
    Formulário de Usuários.
    """

    name = StringField(
        "Nome",
        validators=[
            DataRequired(
                message="Informe o nome."
            ),
            Length(
                min=3,
                max=100
            )
        ],
        render_kw={
            "placeholder": "Nome completo",
            "class": "form-control"
        }
    )

    email = StringField(
        "E-mail",
        validators=[
            DataRequired(
                message="Informe o e-mail."
            ),
            Email(
                message="E-mail inválido."
            ),
            Length(
                max=120
            )
        ],
        render_kw={
            "placeholder": "usuario@email.com",
            "class": "form-control"
        }
    )

    password = PasswordField(
        "Senha",
        validators=[
            Optional(),
            Length(
                min=8,
                max=255
            )
        ],
        render_kw={
            "placeholder": "Senha",
            "class": "form-control"
        }
    )

    role_id = SelectField(
        "Perfil",
        coerce=int,
        validators=[
            DataRequired(
                message="Selecione um perfil."
            )
        ],
        choices=[]
    )

    active = BooleanField(
        "Usuário Ativo",
        default=True
    )

    submit = SubmitField(
        "Salvar Usuário"
    )