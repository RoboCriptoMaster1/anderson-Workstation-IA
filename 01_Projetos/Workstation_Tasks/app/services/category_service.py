"""
=====================================================
Workstation Tasks

Serviço de Categorias

Versão: 0.4.7

=====================================================

Responsável pelas regras de negócio das categorias.
"""

from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.services.base_service import BaseService


class CategoryService(BaseService):
    """
    Serviço responsável pelas categorias.
    """

    def __init__(self):
        super().__init__(CategoryRepository())

    def get_by_name(self, name: str):
        """
        Busca categoria pelo nome.
        """

        return self.repository.get_by_name(name)

    def create_category(
        self,
        name: str,
        description: str = ""
    ) -> Category:
        """
        Cria uma nova categoria.
        """

        if self.repository.exists_name(name):

            raise ValueError(
                "Categoria já cadastrada."
            )

        category = Category()

        category.name = name.strip()
        category.description = description.strip()

        return self.repository.create(category)