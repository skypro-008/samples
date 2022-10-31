import pytest

class FooClass:

    def __init__(self):
        pass

    def foo(self):
        return 1

    def bar(self):
        return 2


class TestFooClass:

    @pytest.fixture
    def foo_class(self):
        instance = FooClass()
        return instance

    def test_foo(self, foo_class):
        assert foo_class.foo() == 1

    def test_bar(self, foo_class):
        assert foo_class.bar() == 2


