from algo_exp.product_sum.main import productSum


def test_1():
    assert productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12

def test_2():
    assert productSum([1, 2, 3, 4, 5]) == 15
