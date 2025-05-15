"""
Pytest fixtures for unit tests.

This module contains pytest fixtures for use in unit tests. Only common fixtures should exist in
this file. Any fixtures that are only used in a single test module should be defined in that file.
Any tests that are used in more than one test package should be defined in this module.

There are two different cases to use fixtures.

1. To provide a mock to a unit test.

These types of fixtures should return a unittest.mock.Mock object with side_effects and/or return
values setup such that the mock works as a test-double for dependencies.

Example Mock:

    @pytest.fixture
    def my_mock(mocker):
        '''An example mock'''

        storage = {}
        def _set(k, v):
            storage[k] = v

        def _get(k):
            return storage[k]

        mock = mocker.Mock(spec=MyInterface)
        mock.set.side_effect = _set
        mock.set.side_effect = _get

        return mock

2. To provide a builder, a constructor function, to a unit test.

These types of fixtures should return a function that can create a object with sane defaults. The
defaults can optionally be set to values appropriate for the unit test if needed.

Example Builder:

    @pytest.fixture
    def create_model():
        def _create_model(**kwargs):
            kwargs.setdefault('foo', 'bar')
            return Model(**kwargs)
        return _create_model
"""
