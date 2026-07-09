"""
=====================================================

Workstation Tasks

Modelo de Projeto

Versão: 0.4.8

=====================================================

Modelo responsável pelos Projetos do sistema.
"""

from app.extensions import db


class Project(db.Model):
    """
    Modelo de Projeto.
    """

    __tablename__ = "projects"

    # =====================================================
    # Campos
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False,
        unique=True,
        index=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    active = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
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

    owner = db.relationship(
        "User",
        backref="projects",
        lazy=True
    )

    tasks = db.relationship(
        "Task",
        back_populates="project",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # =====================================================
    # Métodos
    # =====================================================

    def update(self, **kwargs) -> None:
        """
        Atualiza os atributos do projeto.
        """

        for key, value in kwargs.items():

            if hasattr(self, key):

                setattr(self, key, value)

    def __repr__(self) -> str:
        """
        Representação textual do objeto.
        """

        return f"<Project {self.name}>"

    def to_dict(self) -> dict:
        """
        Retorna o projeto em formato dicionário.
        """

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "active": self.active,
            "owner_id": self.owner_id,
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