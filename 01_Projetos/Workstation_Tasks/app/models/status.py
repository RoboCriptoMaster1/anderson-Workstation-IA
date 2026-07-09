"""
=====================================================
Workstation Tasks
Modelo de Status
=====================================================
"""

from app.extensions import db


class Status(db.Model):

    __tablename__ = "statuses"

    id = db.Column(
        db.Integer,
        primary_key=True,
        index=True
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

    tasks = db.relationship(
        "Task",
        back_populates="status",
        lazy=True
    )

    def __repr__(self):
        return f"<Status {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }