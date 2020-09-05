from unittest import TestCase, main
from algo_exp.two_sum.main import two_number_sum


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10), [-1, 11])


if __name__ == '__main__':
    main()
