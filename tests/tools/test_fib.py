import pytest
from pbc.tools.fibonacci import fibonacci

# this test is marked with "fibs" label
@pytest.mark.fibs
def test_type(setup):
    assert type(fibonacci(7)) == str


@pytest.mark.parametrize("data_input,expected",
                         [(7, '0, 1, 1, 2, 3, 5, 8'), 
                          (3, '0, 1, 1'),
                          pytest.param('1', '0, 1, 1', marks=pytest.mark.xfail),
                         ])


# this test is marked with "fibs" label
@pytest.mark.fibs 
def test_num_func(setup,data_input, expected):
    assert fibonacci(data_input) == expected
