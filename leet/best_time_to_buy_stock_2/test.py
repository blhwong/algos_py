from leet.best_time_to_buy_stock_2.main import Solution


s = Solution()


def test_1():
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7


def test_2():
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4


def test_3():
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
