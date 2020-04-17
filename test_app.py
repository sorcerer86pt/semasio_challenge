from challenge import getMultiplicationValues


def test_sample_array():
    numbers = [6, 8, 8, 7, 2, 5]
    mult_values = getMultiplicationValues(numbers)
    assert (int(mult_values[0])) == 6
    assert (int(mult_values[1])) == 8


def test_second_sample_array():
    numbers = [1, 9, 2, 4]
    mult_values = getMultiplicationValues(numbers)
    assert (int(mult_values[0])) == 9
    assert (int(mult_values[1])) == 4
    
def test_third_sample_array():
    numbers = [1, 2, 3, 4, 5, 6]
    mult_values = getMultiplicationValues(numbers)
    assert (int(mult_values[0])) == 6
    assert (int(mult_values[1])) == 5
