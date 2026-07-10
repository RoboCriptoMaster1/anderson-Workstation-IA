"""
=====================================================

Workstation Tasks

Módulo de Usuários

Versão: 0.5.0

=====================================================

Responsável pelas rotas do módulo de usuários.

"""

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from flask_login import login_required

from app.forms.user_form import UserForm
from app.services.user_service import UserService


# =====================================================
# Blueprint
# =====================================================

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users"
)


# =====================================================
# Service
# =====================================================

user_service = UserService()


# =====================================================
# Listagem
# =====================================================

@users_bp.route("/")
@login_required
def index():
    """
    Lista todos os usuários.
    """

    users = user_service.get_all()

    return render_template(
        "users/index.html",
        users=users
    )


# =====================================================
# Novo Usuário
# =====================================================

@users_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    """
    Cadastro de usuário.
    """

    form = UserForm()

    if form.validate_on_submit():

        flash(
            "Cadastro de usuários será implementado na Sprint 0.5.0.",
            "info"
        )

        return redirect(url_for("users.index"))

    return render_template(
        "users/new.html",
        form=form
    )


# =====================================================
# Perfil
# =====================================================

@users_bp.route("/profile/<int:user_id>")
@login_required
def profile(user_id):
    """
    Exibe o perfil do usuário.
    """

    user = user_service.get_by_id(user_id)

    if user is None:

        flash(
            "Usuário não encontrado.",
            "danger"
        )

        return redirect(url_for("users.index"))

    return render_template(
        "users/profile.html",
        user=user
    )


# =====================================================
# Editar
# =====================================================

@users_bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit(user_id):
    """
    Edita um usuário.
    """

    user = user_service.get_by_id(user_id)

    if user is None:

        flash(
            "Usuário não encontrado.",
            "danger"
        )

        return redirect(url_for("users.index"))

    form = UserForm(obj=user)

    if form.validate_on_submit():

        flash(
            "Edição será implementada na Sprint 0.5.0.",
            "info"
        )

        return redirect(url_for("users.profile", user_id=user.id))

    return render_template(
        "users/edit.html",
        form=form,
        user=user
    )


# =====================================================
# Excluir
# =====================================================

@users_bp.route("/delete/<int:user_id>", methods=["POST"])
@login_required
def delete(user_id):
    """
    Exclui um usuário.
    """

    flash(
        "Exclusão será implementada na Sprint 0.5.0.",
        "warning"
    )

    return redirect(url_for("users.index"))