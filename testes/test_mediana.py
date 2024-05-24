import pytest

@pytest.mark.parametrize("test_list, resultado", [
    ([10, 20, 35, 40, 51], 35),
    ([4, 6, 8], 6),
    ([1, 6, 7, 12],  6.5)
])
def test_mediana(N2, test_list, resultado):
    assert N2.mediana(test_list) == resultado

def test_mediana_vazio(N2):
    test_list = []
    assert N2.mediana(test_list) == 0

@pytest.mark.xfail(reason="Precisa ser vazio")
def test_mediana_vazio_xfail(N2):
    test_list = [2]
    assert N2.mediana(test_list) == 0