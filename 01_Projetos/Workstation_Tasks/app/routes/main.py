"""
=====================================================
Workstation Tasks
Rota Principal
=====================================================
"""

from flask import Blueprint, render_template
from flask_login import login_required

# Blueprint principal
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
@login_required
def index():
    """
    Página inicial da aplicação.
    """

    return render_template("dashboard/index.html")