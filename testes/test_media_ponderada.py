import pytest

@pytest.mark.parametrize("test_list, test_pesos, resultado", [
    ([10, 10], [10, 10], 10),
    ([4, 6], [5, 5], 5),
    ([18, 2], [10, 10], 10)
])
def test_media_ponderada(N2, test_list, test_pesos, resultado):
    assert N2.media_ponderada(test_list, test_pesos) == resultado


@pytest.mark.xfail(reason="Resultados incorretos")
@pytest.mark.parametrize("test_list, test_pesos, resultado", [
    ([10, 10], [10, 10], 15),
    ([4, 6], [5, 5], 44),
    ([18, 2], [10, 10], 11)
])
def test_media_ponderada_xfail(N2, test_list, test_pesos, resultado):
    assert N2.media_ponderada(test_list, test_pesos) == resultado