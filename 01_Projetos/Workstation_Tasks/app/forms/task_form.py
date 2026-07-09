"""
=====================================================
Workstation Tasks

Task Form

Versão: 0.4.5

=====================================================

Formulário oficial de Tarefas.
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


class TaskForm(BaseForm):
    """
    Formulário de Tarefas.
    """

    title = StringField(
        "Título",
        validators=[
            DataRequired(
                message="Informe o título da tarefa."
            ),
            Length(
                min=3,
                max=150
            )
        ],
        render_kw={
            "placeholder": "Título da tarefa",
            "class": "form-control"
        }
    )

    description = TextAreaField(
        "Descrição",
        validators=[
            Optional(),
            Length(max=1000)
        ],
        render_kw={
            "placeholder": "Descreva a tarefa",
            "rows": 6,
            "class": "form-control"
        }
    )

    project_id = SelectField(
        "Projeto",
        coerce=int,
        validators=[
            DataRequired(
                message="Selecione um projeto."
            )
        ],
        choices=[]
    )

    user_id = SelectField(
        "Responsável",
        coerce=int,
        validators=[
            DataRequired(
                message="Selecione um responsável."
            )
        ],
        choices=[]
    )

    status_id = SelectField(
        "Status",
        coerce=int,
        validators=[
            DataRequired(
                message="Selecione um status."
            )
        ],
        choices=[]
    )

    category_id = SelectField(
        "Categoria",
        coerce=int,
        validators=[Optional()],
        choices=[]
    )

    deadline = DateField(
        "Prazo",
        validators=[Optional()],
        format="%Y-%m-%d"
    )

    submit = SubmitField(
        "Salvar Tarefa"
    )