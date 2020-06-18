from unittest import TestCase, main
from grokking.two_heaps.maximize_capital.main import find_maximum_capital


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1), 6)

    def test_2(self):
        self.assertEqual(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0), 8)


if __name__ == '__main__':
    main()
