import pytest


@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("valor1, valor2", [(2, 2), (3, 5)])
def test_soma(valor1, valor2):
    assert valor1 == 2 or valor1 == 3
    assert valor2 == 2 or valor2 == 5

