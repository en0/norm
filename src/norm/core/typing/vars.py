from typing import TypeVar

from norm.core.typing.query_mapper import IQueryMapper

MAPPER_T = TypeVar("MAPPER_T", bound=IQueryMapper)
MODEL_T = TypeVar("MODEL_T", bound=object)
IDENT_T = TypeVar("IDENT_T", bound=object)
