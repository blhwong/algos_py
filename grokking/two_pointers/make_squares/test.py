from unittest import TestCase, main
from grokking.two_pointers.make_squares.main import make_squares


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(make_squares([-2, -1, 0, 2, 3]), [0, 1, 4, 4, 9])

    def test_2(self):
        self.assertCountEqual(make_squares([-3, -1, 0, 1, 2]), [0, 1, 1, 4, 9])


if __name__ == '__main__':
    main()
