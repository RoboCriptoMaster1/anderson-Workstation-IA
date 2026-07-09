"""
=====================================================
Workstation Tasks
Serviço de Autenticação
Versão: 0.3.0
=====================================================
"""

from app.models.user import User


class AuthService:
    """
    Serviço responsável pela autenticação dos usuários.
    """

    @staticmethod
    def authenticate(email, password):
        """
        Autentica um usuário pelo e-mail e senha.
        """

        user = User.query.filter_by(email=email).first()

        if user is None:
            return None

        if not user.check_password(password):
            return None

        return user