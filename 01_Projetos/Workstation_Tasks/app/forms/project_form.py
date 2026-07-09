"""
=====================================================
Workstation Tasks

Project Form

Versão: 0.4.5

=====================================================

Formulário oficial de Projetos.
"""

from wtforms import DateField
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField

from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Optional

from app.forms.base_form import BaseForm


class ProjectForm(BaseForm):
    """
    Formulário de Projetos.
    """

    name = StringField(
        "Nome do Projeto",
        validators=[
            DataRequired(
                message="Informe o nome do projeto."
            ),
            Length(
                min=3,
                max=120
            )
        ],
        render_kw={
            "placeholder": "Nome do projeto",
            "class": "form-control"
        }
    )

    description = TextAreaField(
        "Descrição",
        validators=[
            Optional(),
            Length(max=500)
        ],
        render_kw={
            "placeholder": "Descrição do projeto",
            "rows": 5,
            "class": "form-control"
        }
    )

    owner_id = SelectField(
        "Responsável",
        coerce=int,
        validators=[
            DataRequired(
                message="Selecione um responsável."
            )
        ],
        choices=[]
    )

    start_date = DateField(
        "Data de Início",
        validators=[Optional()],
        format="%Y-%m-%d"
    )

    end_date = DateField(
        "Data Final",
        validators=[Optional()],
        format="%Y-%m-%d"
    )

    submit = SubmitField(
        "Salvar Projeto"
    )