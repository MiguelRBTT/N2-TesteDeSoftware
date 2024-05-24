import pytest

@pytest.mark.parametrize("test_list, resultado", [
    ([1, 2, 3], "Não existe moda"),
    ([2, 3, 5], "Não existe moda"),
    ([-1, 1, 0], "Não existe moda")
])
def test_amodal(N2, test_list, resultado):
    assert N2.amodal(test_list) == resultado


def test_nao_amodal(N2):
    test_list = [1, 2, 2, 3]
    assert N2.amodal(test_list) == "Existe moda"

@pytest.mark.xfail(reason="Não existe moda nesse")
def test_nao_amodal2(N2, amodal_generico_erro):
    test_list = [amodal_generico_erro]
    assert N2.amodal(test_list) == "Existe moda"