from unittest import TestCase, main
from algo_exp.smallest_difference.main import smallestDifference


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])


if __name__ == '__main__':
    main()
