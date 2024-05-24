import pytest

@pytest.mark.parametrize("test_list, resultado", [
    ([10, 20, 30], 20),
    ([4, 3, 5], 4),
    ([4, 8, 12], 8)
])
def test_media(N2, test_list, resultado):
    assert N2.media(test_list) == resultado

def test_media_lista_vazia(N2):
    test_list = []
    assert N2.media(test_list) == 0


@pytest.mark.xfail(reason="Tem número, precisa ser vazio")
def test_media_lista_vazia2(N2):
    test_list = [2, 4, 5]
    assert N2.media(test_list) == 0