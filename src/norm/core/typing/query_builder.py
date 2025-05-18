from abc import ABC


class IQueryBuilder(ABC):
    """
    The IQueryBuilder interface defines a contract for building technology-specific queries.

    Implementations of this interface will provide a way to construct queries that can be executed
    against a specific database technology.

    This interface is intended to be implemented by concrete classes that provide the actual logic
    for building technology specific queries such as MySQL.
    """

    ...
