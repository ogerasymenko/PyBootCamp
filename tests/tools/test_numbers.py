import pytest
from pbc.tools.numbers_summ import num_func

@pytest.mark.parametrize("data_input,expected",
                         [([1,2,3,4,5,5,6], [(4,6), (5,5)]), 
                          ([5,5,5,5,5], [(5,5)]),
                          ((10,0,0,10,1,25), [(10,0)]),
                          pytest.param((10,0,0,10,1,25), [10,0], marks=pytest.mark.xfail),
                          pytest.param(('10,0,0,10,1,25'), [(10,0)], marks=pytest.mark.xfail),
                         ])


# this test is marked with "numbers" label
@pytest.mark.numbers  
def test_num_func(setup,data_input, expected):
    assert num_func(data_input) == expected
