import pytest


def func(x):
    return x + 1


def test_func():
    assert func(4) == 5


def f():
    raise SystemExit(1)


def test_f():
    with pytest.raises(SystemExit):
        f()


class TestClass:

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert "h" in x, "test failed"

