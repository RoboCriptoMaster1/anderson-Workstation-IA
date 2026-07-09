"""
=====================================================
Workstation Tasks

Pacote Oficial de Repositórios

Versão: 0.4.6

=====================================================

Centraliza todos os repositórios da aplicação.
"""

from .base_repository import BaseRepository
from .user_repository import UserRepository
from .role_repository import RoleRepository
from .project_repository import ProjectRepository
from .task_repository import TaskRepository
from .category_repository import CategoryRepository
from .status_repository import StatusRepository

__all__ = [
    "BaseRepository",
    "UserRepository",
    "RoleRepository",
    "ProjectRepository",
    "TaskRepository",
    "CategoryRepository",
    "StatusRepository",
]