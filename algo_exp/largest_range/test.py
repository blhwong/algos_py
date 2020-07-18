from unittest import TestCase, main
from algo_exp.largest_range.main import largestRange


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])


if __name__ == '__main__':
    main()
