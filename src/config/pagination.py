from typing import Any, List

from ninja import Schema
from ninja.pagination import PaginationBase


class CustomPagination(PaginationBase):
    class Input(Schema):
        page: int = 1
        per_page: int = 100

    class Output(Schema):
        count: int
        data: List[Any]
        next: str = None
        previous: str = None

    items_attribute: str = "data"

    def paginate_queryset(self, queryset, pagination: Input, **params):
        per_page = pagination.per_page
        page = pagination.page
        offset = (page - 1) * per_page
        return {
            "count": queryset.count(),
            "data": queryset[offset : offset + per_page],  # noqa
            "next": None,
            "previous": None,
        }
