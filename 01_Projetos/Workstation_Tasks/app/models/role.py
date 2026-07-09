"""
=====================================================
Workstation Tasks
Modelo de Perfil de Usuário
=====================================================
"""

from app.extensions import db


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(
        db.Integer,
        primary_key=True,
        index=True
    )

    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
        index=True
    )

    description = db.Column(
        db.String(255),
        nullable=True
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

    users = db.relationship(
        "User",
        back_populates="role",
        lazy=True
    )

    def __repr__(self):
        return f"<Role {self.id} - {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }