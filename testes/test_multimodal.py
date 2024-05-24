import pytest

@pytest.mark.parametrize("test_list, resultado", [
    ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
    ([4, 4, 6, 6], [4, 6]),
    ([1, 1, 7, 7],  [1, 7])
])
def test_multimodal(N2, test_list, resultado):
    assert N2.multimodal(test_list) == resultado

def test_nao_multimodal(N2):
    test_list = [1, 1, 2, 5, 3, 7]
    assert N2.multimodal(test_list) == "Não é multimodal"

@pytest.mark.xfail(reason="Valor NÃO pode ser multimodal")
def test_nao_multimodal_xfail(N2):
    test_list = [1, 1, 2, 2, 3, 3]
    assert N2.multimodal(test_list) == "Não é multimodal"