"""
=====================================================

Workstation Tasks

Modelo de Categoria

Versão: 0.4.8

=====================================================

Modelo responsável pelas categorias do sistema.
"""

from app.extensions import db


class Category(db.Model):
    """
    Modelo de Categoria.
    """

    __tablename__ = "categories"

    # =====================================================
    # Campos
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
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

    # =====================================================
    # Relacionamentos
    # =====================================================

    tasks = db.relationship(
        "Task",
        back_populates="category",
        lazy=True
    )

    # =====================================================
    # Métodos
    # =====================================================

    def update(self, **kwargs) -> None:
        """
        Atualiza os atributos da categoria.
        """

        for key, value in kwargs.items():

            if hasattr(self, key):

                setattr(self, key, value)

    def __repr__(self) -> str:
        """
        Representação textual da categoria.
        """

        return f"<Category {self.id} - {self.name}>"

    def to_dict(self) -> dict:
        """
        Retorna a categoria em formato dicionário.
        """

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
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