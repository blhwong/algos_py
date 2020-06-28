from unittest import TestCase, main
from algo_exp.two_sum.main import twoNumberSum


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10), [-1, 11])


if __name__ == '__main__':
    main()
