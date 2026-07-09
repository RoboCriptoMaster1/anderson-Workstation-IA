"""
=====================================================
Workstation Tasks

Pacote Oficial de Formulários

Versão: 0.4.5

=====================================================

Centraliza todos os formulários da aplicação.
"""

from .base_form import BaseForm
from .login_form import LoginForm
from .user_form import UserForm
from .project_form import ProjectForm
from .task_form import TaskForm
from .category_form import CategoryForm
from .status_form import StatusForm

__all__ = [
    "BaseForm",
    "LoginForm",
    "UserForm",
    "ProjectForm",
    "TaskForm",
    "CategoryForm",
    "StatusForm",
]