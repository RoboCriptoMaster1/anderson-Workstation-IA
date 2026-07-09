"""
=====================================================

Workstation Tasks

Modelo de Status

Versão: 0.4.8

=====================================================

Modelo responsável pelos Status das tarefas.
"""

from app.extensions import db


class Status(db.Model):
    """
    Modelo de Status.
    """

    __tablename__ = "statuses"

    # =====================================================
    # Campos
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(60),
        nullable=False,
        unique=True,
        index=True
    )

    color = db.Column(
        db.String(20),
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

    # =====================================================
    # Relacionamentos
    # =====================================================

    tasks = db.relationship(
        "Task",
        back_populates="status",
        lazy=True
    )

    # =====================================================
    # Métodos
    # =====================================================

    def update(self, **kwargs) -> None:
        """
        Atualiza os atributos do status.
        """

        for key, value in kwargs.items():

            if hasattr(self, key):

                setattr(self, key, value)

    def __repr__(self) -> str:
        """
        Representação textual do objeto.
        """

        return f"<Status {self.name}>"

    def to_dict(self) -> dict:
        """
        Retorna o status em formato dicionário.
        """

        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
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