from numbers_summ import num_func

def test_type():
    assert type(num_func([1,2,3,4,5,5,6])) == list

def test_output_1():
    assert num_func([1,2,3,4,5,5,6]) == [(4,6),(5,5)]

def test_output_2():
    assert (5,5) in num_func([1,2,3,4,5,5,6])
    
def test_output_3():
    assert (6,4) not in num_func([1,2,3,4,5,5,6])
