"""
=====================================================
Workstation Tasks

Category Form

Versão: 0.4.5

=====================================================

Formulário oficial de Categorias.
"""

from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField

from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Optional

from app.forms.base_form import BaseForm


class CategoryForm(BaseForm):
    """
    Formulário de Categorias.
    """

    name = StringField(
        "Nome da Categoria",
        validators=[
            DataRequired(
                message="Informe o nome da categoria."
            ),
            Length(
                min=3,
                max=100
            )
        ],
        render_kw={
            "placeholder": "Ex.: Desenvolvimento",
            "class": "form-control"
        }
    )

    description = TextAreaField(
        "Descrição",
        validators=[
            Optional(),
            Length(max=300)
        ],
        render_kw={
            "placeholder": "Descrição da categoria",
            "rows": 4,
            "class": "form-control"
        }
    )

    submit = SubmitField(
        "Salvar Categoria"
    )