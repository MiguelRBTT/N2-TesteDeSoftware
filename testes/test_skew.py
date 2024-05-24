import pytest


def test_skew_normal(N2):
    test_list = [1, 2, 3, 4, 5]
    assert N2.skew(test_list) == "Distribuição normal"

@pytest.mark.parametrize("test_list, resultado", [
    ([2, 8, 0, 4, 1, 9, 9, 0], "Distribuição positiva"),
    ([4, 6, 0, 3, 2, 9, 7, 0], "Distribuição positiva"),
    ([3, 10, 0, 4, 2, 9, 8, 0],  "Distribuição positiva")
])
def test_skew_positivo(N2, test_list, resultado):
    assert N2.skew(test_list) == resultado


def test_skew_negativo(N2):
    test_list = [2, 8, 0, 4, 1, 9, 9, 0, -10]
    assert N2.skew(test_list) == "Distribuição negativa"


@pytest.mark.xfail(reason="Precisa ser NEGATIVO")
def test_skew_negativo_xfail(N2):
    test_list = [2, 8, 0, 4, 1, 9, 9, 0, 10]
    assert N2.skew(test_list) == "Distribuição negativa"