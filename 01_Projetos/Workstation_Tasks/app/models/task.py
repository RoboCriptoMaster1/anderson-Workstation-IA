"""
=====================================================

Workstation Tasks

Modelo de Tarefa

Versão: 0.4.8

=====================================================

Modelo responsável pelas tarefas do sistema.
"""

from app.extensions import db


class Task(db.Model):
    """
    Modelo de Tarefa.
    """

    __tablename__ = "tasks"

    # =====================================================
    # Campos
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150),
        nullable=False,
        index=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    deadline = db.Column(
        db.Date,
        nullable=True,
        index=True
    )

    completed = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id"),
        nullable=False,
        index=True
    )

    status_id = db.Column(
        db.Integer,
        db.ForeignKey("statuses.id"),
        nullable=False,
        index=True
    )

    user_id = db.Column(
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

    project = db.relationship(
        "Project",
        back_populates="tasks"
    )

    status = db.relationship(
        "Status",
        back_populates="tasks"
    )

    user = db.relationship(
        "User",
        back_populates="tasks"
    )

    # =====================================================
    # Métodos
    # =====================================================

    def update(self, **kwargs) -> None:
        """
        Atualiza os atributos da tarefa.
        """

        for key, value in kwargs.items():

            if hasattr(self, key):

                setattr(self, key, value)

    def __repr__(self) -> str:
        """
        Representação textual da tarefa.
        """

        return f"<Task {self.id} - {self.title}>"

    def to_dict(self) -> dict:
        """
        Retorna a tarefa em formato dicionário.
        """

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": (
                self.deadline.isoformat()
                if self.deadline
                else None
            ),
            "completed": self.completed,
            "project_id": self.project_id,
            "status_id": self.status_id,
            "user_id": self.user_id,
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