"""
=====================================================
Workstation Tasks
Rotas de Autenticação
=====================================================
"""

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from app.extensions import login_manager
from app.models.user import User
from app.services import AuthService

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:

        return redirect(
            url_for("main.index")
        )

    if request.method == "POST":

        email = request.form.get("email")

        password = request.form.get("password")

        user = AuthService.authenticate(
            email,
            password
        )

        if user:

            login_user(user)

            flash(
                "Login realizado com sucesso.",
                "success"
            )

            return redirect(
                url_for("main.index")
            )

        flash(
            "Usuário ou senha inválidos.",
            "danger"
        )

    return render_template(
        "login/login.html"
    )


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Sessão encerrada.",
        "info"
    )

    return redirect(
        url_for("auth.login")
    )