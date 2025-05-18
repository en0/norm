from abc import ABC, abstractmethod

from .query_builder import IQueryBuilder


class IQueryMapper(ABC):
    """
    The IQueryMapper interface defines a contract for mapping domain requests to queries.

    Implementations of this interface will provide a way to translate domain-level filter conditions
    into a query that can be executed against a specific database technology.

    This interface is intended to be implemented by concrete classes that provide the actual logic
    for mapping domain requests to queries.

    Example:

        class TodoQueryMapper(IQueryMapper):

            def closed_tasks(self):
                self._closed_only = True

            @override
            def apply(self, query_builder: IQueryBuilder) -> None:
                if self._closed_only:
                    query_builder.equals("status", "CLOSED")

            def __init__(self):
                self._closed_only = False

        # Usage
        repo = TodoRepository()
        closed_tasks = repo.find(lambda q: q.closed_tasks())
    """

    @abstractmethod
    def apply(self, query_builder: IQueryBuilder) -> None: ...
