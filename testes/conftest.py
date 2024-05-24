from stat_funcs import StatsN2
import pytest


@pytest.fixture
def N2():
    return StatsN2()


@pytest.fixture
def amodal_generico_erro():
    return [1, 2, 3]