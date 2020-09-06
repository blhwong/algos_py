from algo_exp.product_sum.main import product_sum


def test_1():
    assert product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12

def test_2():
    assert product_sum([1, 2, 3, 4, 5]) == 15
