from algo_exp.three_largest_numbers.main import find_three_largest_numbers


def test_1():
    assert find_three_largest_numbers([10, 5, 9, 10, 12]) == [10, 10, 12]

def test_2():
    assert find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]) == [18, 141, 541]
