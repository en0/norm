"""
Environment Setup Test Suite

This module ensures the python test environment is correctly installed and all modules are in the
path and accessable.
"""

from abc import ABC, abstractmethod
from typing import NamedTuple, override

import pytest


class IDependency(ABC):
    """An example dependency"""

    @abstractmethod
    def set(self, k: str, v: str): ...

    @abstractmethod
    def get(self, k: str) -> str: ...


class MyDependency(IDependency):

    @override
    def set(self, k: str, v: str):
        self.storage[k] = v

    @override
    def get(self, k: str) -> str:
        return self.storage[k]

    def __init__(self):
        self.storage: dict[str, str] = {}


class Model(NamedTuple):
    """An example model."""

    foo: str
    bar: str


@pytest.fixture
def dependency_mock(mocker):
    """Provides a mocked dependency"""

    storage = {}

    def _set(k, v):
        storage[k] = v

    def _get(k):
        return storage[k]

    mock = mocker.Mock(spec=IDependency)
    mock.get.side_effect = _get
    mock.set.side_effect = _set

    return mock


@pytest.fixture
def dependency():
    """Provides a dependency"""
    return MyDependency()


@pytest.fixture
def create_model():
    """Provides a model creator"""

    def _create_model(**kwargs):
        kwargs.setdefault("foo", "FOO")
        kwargs.setdefault("bar", "BAR")
        return Model(**kwargs)

    return _create_model


def test_is_core_accessable():
    # Given nothing

    # When nothing

    # Then i can import the core module
    import core


def test_create_model_is_accessable(create_model):
    # Given a create_model function

    # When creating multiple models
    model1 = create_model()
    model2 = create_model(foo="1", bar="2")

    # Then each model is different and the fields are set correctly
    assert model1 is not model2

    assert model1.foo == "FOO"
    assert model1.bar == "BAR"

    assert model2.foo == "1"
    assert model2.bar == "2"


def test_dependency_mock(dependency_mock):
    # Given a mocked depenency

    # When i use the mocked dependency
    dependency_mock.set("foo", "FOO")

    # Then it works as expected
    assert dependency_mock.get("foo") == "FOO"
    dependency_mock.set.assert_called()


def test_dependency(dependency, mocker):
    # Given an unmocked depenency with a spy on the set method
    spy = mocker.spy(dependency, "set")

    # When set is called
    dependency.set("foo", "FOO")

    # I can use the spy to see verify calling details
    spy.assert_called_with("foo", "FOO")
