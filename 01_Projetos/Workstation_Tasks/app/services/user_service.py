"""
=====================================================
Workstation Tasks

Serviço de Usuários

Versão: 0.4.7

=====================================================

Responsável pelas regras de negócio relacionadas aos
usuários.
"""

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.base_service import BaseService


class UserService(BaseService):
    """
    Serviço responsável pelos usuários.
    """

    def __init__(self):
        super().__init__(UserRepository())

    # =====================================================
    # Consultas
    # =====================================================

    def get_by_email(self, email: str):
        """
        Busca usuário pelo e-mail.
        """

        return self.repository.get_by_email(
            email.strip().lower()
        )

    def get_active_users(self):
        """
        Retorna somente usuários ativos.
        """

        return self.repository.get_active_users()

    # =====================================================
    # Regras de Negócio
    # =====================================================

    def create_user(
        self,
        name: str,
        email: str,
        password: str,
        role_id: int
    ) -> User:
        """
        Cria um novo usuário.
        """

        email = email.strip().lower()

        if self.repository.email_exists(email):

            raise ValueError(
                "Já existe um usuário com este e-mail."
            )

        user = User()

        user.name = name.strip()
        user.email = email
        user.role_id = role_id
        user.active = True

        user.set_password(password)

        return self.repository.create(user)

    def activate(self, user: User) -> User:
        """
        Ativa um usuário.
        """

        user.active = True

        self.repository.update()

        return user

    def deactivate(self, user: User) -> User:
        """
        Desativa um usuário.
        """

        user.active = False

        self.repository.update()

        return user

    def change_password(
        self,
        user: User,
        password: str
    ) -> User:
        """
        Atualiza a senha.
        """

        user.set_password(password)

        self.repository.update()

        return user

    def update_user(
        self,
        user: User,
        **kwargs
    ) -> User:
        """
        Atualiza os dados do usuário.
        """

        user.update(**kwargs)

        self.repository.update()

        return user