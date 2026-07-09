"""
=====================================================
Workstation Tasks

Status Form

Versão: 0.4.5

=====================================================

Formulário oficial de Status.
"""

from wtforms import StringField
from wtforms import SubmitField

from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Optional

from app.forms.base_form import BaseForm


class StatusForm(BaseForm):
    """
    Formulário de Status.
    """

    name = StringField(
        "Nome do Status",
        validators=[
            DataRequired(
                message="Informe o nome do status."
            ),
            Length(
                min=3,
                max=60
            )
        ],
        render_kw={
            "placeholder": "Ex.: Em andamento",
            "class": "form-control"
        }
    )

    color = StringField(
        "Cor",
        validators=[
            Optional(),
            Length(max=20)
        ],
        render_kw={
            "placeholder": "#0d6efd",
            "type": "color",
            "class": "form-control form-control-color"
        }
    )

    submit = SubmitField(
        "Salvar Status"
    )