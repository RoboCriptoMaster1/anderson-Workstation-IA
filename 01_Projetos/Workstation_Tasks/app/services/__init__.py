"""
=====================================================
Workstation Tasks

Pacote Oficial de Services

Versão: 0.4.7

=====================================================

Centraliza todos os Services da aplicação.
"""

from .base_service import BaseService
from .auth_service import AuthService
from .user_service import UserService
from .role_service import RoleService
from .project_service import ProjectService
from .task_service import TaskService
from .category_service import CategoryService
from .status_service import StatusService

__all__ = [
    "BaseService",
    "AuthService",
    "UserService",
    "RoleService",
    "ProjectService",
    "TaskService",
    "CategoryService",
    "StatusService",
]