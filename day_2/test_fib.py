from fibonacci import fibonacci

def test_type():
    assert type(fibonacci(7)) == str
    
def test_output_1():
    assert fibonacci(7) == '0, 1, 1, 2, 3, 5, 8'

def test_output_2():
    assert fibonacci(3) == '0, 1, 1'
