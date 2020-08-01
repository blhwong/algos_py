from unittest import TestCase, main
from algo_exp.shifted_binary_search.main import shiftedBinarySearch


class TestSuite(TestCase):
    def test_1(self):
        array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
        self.assertEqual(shiftedBinarySearch(array, 33), 8)

    def test_2(self):
        array = [5, 23, 111, 1]
        self.assertEqual(shiftedBinarySearch(array, 111), 2)

    def test_3(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(shiftedBinarySearch(array, 7), 6)

if __name__ == '__main__':
    main()
