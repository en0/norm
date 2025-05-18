from abc import abstractmethod
from collections.abc import Iterable
from typing import Callable, Generic

from .vars import IDENT_T, MAPPER_T, MODEL_T

FilterPredicate = Callable[[MAPPER_T], MAPPER_T]


class IRepository(Generic[IDENT_T, MODEL_T, MAPPER_T]):

    @abstractmethod
    def save(self, entity: MODEL_T) -> MODEL_T: ...

    @abstractmethod
    def update(self, entity: MODEL_T) -> MODEL_T: ...

    @abstractmethod
    def delete(self, ident: IDENT_T) -> None: ...

    @abstractmethod
    def find_by_id(self, ident: IDENT_T) -> MODEL_T: ...

    @abstractmethod
    def find_all(self) -> Iterable[MODEL_T]: ...

    @abstractmethod
    def find(self, predicate: FilterPredicate[MAPPER_T]) -> Iterable[MODEL_T]: ...
