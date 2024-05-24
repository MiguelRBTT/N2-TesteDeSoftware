import pytest

@pytest.mark.parametrize("test_list, resultado", [
    ([3, 1, 50], 769),
    ([5, 10, 15], 25),
    ([7, 9, 17],  28)
])
def test_variancia(N2, test_list, resultado):
    assert N2.variancia(test_list) == resultado


@pytest.mark.xfail(reason="Dados incorretos com a variancia")
@pytest.mark.parametrize("test_list, resultado", [
    ([5, 1, 70], 769),
    ([7, 10, 44], 25),
    ([7, 10, 17],  28)
])
def test_variancia_xfail(N2, test_list, resultado):
    assert N2.variancia(test_list) == resultado