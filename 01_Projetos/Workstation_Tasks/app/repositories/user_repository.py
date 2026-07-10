"""
=====================================================

Workstation Tasks

User Repository

Versão: 0.5.0

=====================================================

Responsável pelo acesso aos dados de usuários.

"""

from sqlalchemy import or_

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

    def get_inactive_users(self):
        """
        Retorna apenas usuários inativos.
        """

        return User.query.filter_by(
            active=False
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

    def search(self, term: str):
        """
        Pesquisa usuários por nome ou e-mail.
        """

        return User.query.filter(

            or_(
                User.name.ilike(f"%{term}%"),
                User.email.ilike(f"%{term}%")
            )

        ).order_by(User.name.asc()).all()

    def get_by_role(self, role_id: int):
        """
        Retorna usuários por perfil.
        """

        return User.query.filter_by(
            role_id=role_id
        ).all()

    def count_active(self) -> int:
        """
        Retorna a quantidade de usuários ativos.
        """

        return User.query.filter_by(
            active=True
        ).count()

    def count_inactive(self) -> int:
        """
        Retorna a quantidade de usuários inativos.
        """

        return User.query.filter_by(
            active=False
        ).count()