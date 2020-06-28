from unittest import TestCase, main
from algo_exp.binary_search.main import binarySearch


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

if __name__ == '__main__':
    main()
