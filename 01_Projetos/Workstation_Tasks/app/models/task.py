"""
=====================================================
Workstation Tasks
Modelo de Tarefa
=====================================================
"""

from app.extensions import db


class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(
        db.Integer,
        primary_key=True,
        index=True
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

    def __repr__(self):
        return f"<Task {self.id} - {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "project_id": self.project_id,
            "status_id": self.status_id,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }