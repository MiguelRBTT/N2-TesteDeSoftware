import pytest

@pytest.mark.parametrize("test_var, resultado", [
    (4, 2),
    (25, 5),
    (36, 6)
])
def test_dpadrao(N2, test_var, resultado):
    assert N2.dpadrao(test_var) == resultado

def test_dpadrao_zero(N2):
    test_var = 0
    assert N2.dpadrao(test_var) == 0

@pytest.mark.xfail(reason="Tem número, precisa ser vazio")
def test_dpadrao_zero2(N2, ):
    test_var = 5
    assert N2.dpadrao(test_var) == 0