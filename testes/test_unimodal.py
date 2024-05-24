import pytest

@pytest.mark.parametrize("test_list, resultado", [
    ([1, 2, 2, 3, 4], 2),
    ([4, 6, 0, 3, 3, 9, 7, 1], 3),
    ([3, 10, 0, 4, 4, 9, 8, 7],  4)
])
def test_unimodal(N2, test_list, resultado):
    assert N2.unimodal(test_list) == resultado


def test_nao_unimodal(N2):
    test_list = [1, 1, 2, 2, 3, 3]
    assert N2.unimodal(test_list) == "Não é unimodal"


@pytest.mark.xfail(reason="NÃO pode ser unimodal")
def test_nao_unimodal_xfail(N2):
    test_list = [1, 4, 2, 2, 3, 7]
    assert N2.unimodal(test_list) == "Não é unimodal"