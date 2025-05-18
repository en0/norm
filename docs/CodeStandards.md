# Coding Standards

Coding standards document for nORM

## General Requirements

- All public classes must implement a specific interface.
- All public interfaces must contain class and method level docstrings
- Typehits must be used in all required cases. No unknown types should exist.
- Functionality must have a corresponding unit test suite.
- Use descriptive and consistent naming conventions for classes, methods, and variables.
- Class names should be in `PascalCase`, and method/variable names should be in `snake_case`.

## Class and Method Documentation

- All public interface must contain a docstring on the class and each method.
- Classes that implement an interface do not require docstrings.
- Class level docstrings must provide the following details:
    - A description of the class including its purpose and responsibilities.
- Method level docstrings must include the following details:
    - A description of the method and its function.
    - `Args` required to call the function.
    - `Kwargs` if applicable, available to the function.
    - `Raises` will identify what conditions raise what exceptions. Note: only specify exceptions
      that the caller should catch. Unexpected exceptions should not be listed.
    - `Returns` will specify what the method returns. If the return type is None, you can exclude
      this attribute.

## Interface

- All classes part of the public interface must be described by an interface.
- Define interfaces and abstract classes using the `ABC` module.
- Use the `@abstractmethod` decorator for methods that must be implemented by subclasses.
- All interfaces should start with a capital i, 'I', followed by the rest of the name.

## Exception Handling

- Custom exceptions should inherit from a base exception class (`NORMError`).
- Each exception class must have a clear docstring explaining its purpose and attributes.
- Use descriptive error messages and include relevant attributes in exceptions.
- Methods should raise specific exceptions for error conditions.
- Docstrings should include what exceptions can be raised by a method.

## Type Hints

- Use type annotations for function arguments, return types, and ambiguous variables.
- Use `Any` for generic types when the specific type is not known.
- Use the `@override` decorator to indicate that a method is intended to override a method in a base class.
- Use the `@final` decorator to indicate that a class should not be subclassed.
- Always catpure return values from methods. If the value is not used, use the `_` variable.

### Examples

1. **Type Annotations for Function Arguments and Return Types**:

```python
class IRepository(Generic[MODEL_T, IDENTITY_T]):

    @abstractmethod
    def save(self, entity: MODEL_T) -> MODEL_T:
        ...
```

2. **Using `@final` Decorator**:

```python
from typing import final

@final
class ConfigSetService:
    ...
```

3. **Using `@override` Decorator**:

```python
from typing import override

class MyRepository(IRepository[str, str]):

    @override
    def save(self, entity: str) -> str:
        ...
```

4. **Docstrings are required on interfaces and interface methods.**

```python

class IClass(ABC):
    """
    A class used as an example to show docstrings.

    This class exists to show you an example of a good docstring. It's primary responsibility is to
    provide a complete example of docstrings in use.

    Attributes:
    - get(k: str) -> str: Retrives and returns the string associated with the given key.
    """

    @abstractmethod
    def get(self, k: str) -> str:
        """
        Retrive and return the string associated with the given key.

        This will locate the value associated with the given key and return the value as a string.
        If the given key is not known, the method will raise an exception.

        Args:
            k (str): The key that identifies the desired value.

        Raises:
            KeyNotKnownError when the given key is not found.

        Returns:
            The value associated with the given key.
        ...
```

5. **Typing and return values.**

```python
_ = a_function_that_returns_a_value_we_dont_need()
ambiguous_variable: str = a_function_with_an_ambiguous_response()
```


## Unit Tests

- Use fixtures to provide mocks, builders, and other test dependencies.
- Use mock classes to simulate dependencies in unit tests.
- Mock classes should end with the word "mock". e.g. foo_repository_mock
- The `unit` fixture should always be included in each test module and represent the unit under test.
- Include tests that verify exception handling.
- Unit tests should follow the "Given, When, Then" structure.
    - The structure should be clearly articulated in the comments.
    - Add detail to each part to clarify what the test is doing.
- Unit tests do not require docstrings.
- Unit tests do not require type hints.
- Fixtures should include a docstring.
- Do not include fixtures that are not used by the test.

1. **The Unit Under Test**

```python
@pytest.fixture
def unit(some_mock) -> SomeUnit:
    """
    Fixture for SomeUnit with it's dependencies mocked.
    """
    return SomeUnit(some_mock)
```

2. **Testing for Exceptions**:

```python
def test_cannot_do_that(unit: SomeUnit):
    # Given a key that doesn't exist
    key = "foo"

    # When get is called with the name
    # Then the KeyNotKnownError is raised
    with pytest.raises(KeyNotKnownError):
        _ = unit.get(name)
```

3. **Mocking Dependencies**:
```python
def test_can_create_config_set(unit: SomeUnit, some_mock: SomeMock):
    # Given a name
    name = "Foo"

    # When the name is set
    unit.set("name", name)

    # Then the given name should saved.
    some_mock.write.assert_called_with(f"name={name}")
```
