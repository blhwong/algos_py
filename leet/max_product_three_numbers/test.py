from leet.max_product_three_numbers.main import Solution


s = Solution()


def test_1():
    assert s.maximumProduct([1, 2, 3]) == 6


def test_2():
    assert s.maximumProduct([1, 2, 3, 4]) == 24
