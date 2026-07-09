"""
=====================================================
Workstation Tasks

Serviço de Autenticação

Versão: 0.4.7

=====================================================

Responsável pelas regras de negócio relacionadas à
autenticação dos usuários.
"""

from app.repositories.user_repository import UserRepository


class AuthService:
    """
    Serviço responsável pela autenticação dos usuários.
    """

    _repository = UserRepository()

    @staticmethod
    def authenticate(email: str, password: str):
        """
        Autentica um usuário.

        Parameters
        ----------
        email : str
            E-mail do usuário.

        password : str
            Senha informada.

        Returns
        -------
        User | None
            Retorna o usuário autenticado ou None.
        """

        email = email.strip().lower()

        user = AuthService._repository.get_by_email(email)

        if user is None:
            return None

        if not user.active:
            return None

        if not user.check_password(password):
            return None

        return user

    @staticmethod
    def user_exists(email: str) -> bool:
        """
        Verifica se um usuário existe pelo e-mail.

        Parameters
        ----------
        email : str

        Returns
        -------
        bool
        """

        return AuthService._repository.email_exists(
            email.strip().lower()
        )