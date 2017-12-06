import pytest
from ..some_app.numbers_summ import num_func


@pytest.mark.parametrize("test_input,expected", [
    pytest.param("4 + 6", "4 + 6", marks=pytest.mark.xfail)
])


# this test is marked with "debug" label
@pytest.mark.debug  
def test_eval(test_input, expected):
    assert eval(test_input) == expected
