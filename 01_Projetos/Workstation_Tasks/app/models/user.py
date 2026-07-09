"""
=====================================================
Workstation Tasks
Modelo de Usuário
Versão: 0.3.0
=====================================================
"""

from flask_login import UserMixin
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.extensions import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        index=True
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

    role = db.relationship(
        "Role",
        back_populates="users"
    )

    tasks = db.relationship(
        "Task",
        back_populates="user",
        lazy=True
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(
            self.password,
            password
        )

    def __repr__(self):
        return f"<User {self.email}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "active": self.active,
            "role_id": self.role_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }