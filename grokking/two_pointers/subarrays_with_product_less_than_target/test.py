from unittest import TestCase, main
from grokking.two_pointers.subarrays_with_product_less_than_target.main import find_subarrays


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(find_subarrays([2, 5, 3, 10], 30), [[2], [5], [2, 5], [3], [5, 3], [10]])

    def test_2(self):
        self.assertCountEqual(find_subarrays([8, 2, 6, 5], 50), [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]])


if __name__ == '__main__':
    main()
