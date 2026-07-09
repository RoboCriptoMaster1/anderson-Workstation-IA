"""
=====================================================
Workstation Tasks

Modelo de Usuário

Versão: 0.4.6

=====================================================

Modelo responsável pelos usuários do sistema.
"""

from flask_login import UserMixin
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from app.extensions import db


class User(UserMixin, db.Model):
    """
    Modelo de Usuário.
    """

    __tablename__ = "users"

    # =====================================================
    # Campos
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(120),
        nullable=False,
        index=True
    )

    email = db.Column(
        db.String(150),
        nullable=False,
        unique=True,
        index=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    active = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False,
        index=True
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now(),
        nullable=False
    )

    # =====================================================
    # Relacionamentos
    # =====================================================

    role = db.relationship(
        "Role",
        back_populates="users"
    )

    tasks = db.relationship(
        "Task",
        back_populates="user",
        lazy=True
    )

    # =====================================================
    # Métodos
    # =====================================================

    def set_password(self, password: str) -> None:
        """
        Gera o hash da senha.
        """

        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Verifica se a senha informada é válida.
        """

        return check_password_hash(
            self.password,
            password
        )

    def update(self, **kwargs) -> None:
        """
        Atualiza os atributos do objeto dinamicamente.
        """

        for key, value in kwargs.items():

            if hasattr(self, key):

                setattr(self, key, value)

    def __repr__(self) -> str:
        """
        Representação textual do objeto.
        """

        return f"<User {self.email}>"

    def to_dict(self) -> dict:
        """
        Retorna o objeto em formato dicionário.
        """

        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "active": self.active,
            "role_id": self.role_id,
            "created_at": (
                self.created_at.isoformat()
                if self.created_at
                else None
            ),
            "updated_at": (
                self.updated_at.isoformat()
                if self.updated_at
                else None
            )
        }