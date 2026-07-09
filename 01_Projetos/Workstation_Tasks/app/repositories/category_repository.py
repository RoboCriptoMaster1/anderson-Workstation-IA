"""
=====================================================
Workstation Tasks

Category Repository

Versão: 0.4.6

=====================================================

Responsável pelo acesso aos dados de Categorias.
"""

from app.models.category import Category
from app.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    """
    Repositório de Categorias.
    """

    def __init__(self):
        super().__init__(Category)

    # =====================================================
    # Consultas Específicas
    # =====================================================

    def get_by_name(self, name: str):
        """
        Busca uma categoria pelo nome.
        """

        return Category.query.filter_by(
            name=name
        ).first()

    def exists_name(self, name: str) -> bool:
        """
        Verifica se a categoria já existe.
        """

        return (
            Category.query.filter_by(name=name)
            .first()
            is not None
        )

    def search(self, text: str):
        """
        Pesquisa categorias pelo nome.
        """

        return Category.query.filter(
            Category.name.ilike(f"%{text}%")
        ).all()

    def ordered(self):
        """
        Retorna categorias ordenadas por nome.
        """

        return Category.query.order_by(
            Category.name.asc()
        ).all()