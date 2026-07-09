"""
=====================================================
Workstation Tasks

User Repository

Versão: 0.4.6

=====================================================

Responsável pelo acesso aos dados de usuários.
"""

from app.models.user import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """
    Repositório de Usuários.
    """

    def __init__(self):
        super().__init__(User)

    # =====================================================
    # Consultas Específicas
    # =====================================================

    def get_by_email(self, email: str):
        """
        Retorna um usuário pelo e-mail.
        """

        return User.query.filter_by(
            email=email
        ).first()

    def get_active_users(self):
        """
        Retorna apenas usuários ativos.
        """

        return User.query.filter_by(
            active=True
        ).all()

    def email_exists(self, email: str) -> bool:
        """
        Verifica se o e-mail já existe.
        """

        return (
            User.query.filter_by(email=email)
            .first()
            is not None
        )