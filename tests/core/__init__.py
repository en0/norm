"""
Core Package Unit Tests

This module contains unit tests for the core module.

Each unit under test should be contain the same namespace structure as the unit being tested. For
example, if a module is located in src/core/lib/foo::Foo, then the test module would be located at
tests/core/lib/test_foo.py or tests/core/lib/foo/test_foo_method.py. If you use a directory to store
multiple test cases for a single unit, it is appropriate to create a fixtures.py for those test
cases. In this example, tests/core/lib/foo/fixtures.py.


# Example unittest file.

    import pytest

    from fixtures import *


    @pytest.fixture
    def unit():
        return Foo()


    def test_foo_can_bar(unit):
        # Given some initial criteria
        ...

        # When an action is taken
        ...

        # Then expect some result.
        ...
"""
