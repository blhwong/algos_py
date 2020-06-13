from unittest import TestCase, main
from grokking.cyclic_sort.find_missing_numbers.main import find_missing_numbers


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]), [4, 6, 7])

    def test_2(self):
        self.assertListEqual(find_missing_numbers([2, 4, 1, 2]), [3])

    def test_3(self):
        self.assertListEqual(find_missing_numbers([2, 3, 2, 1]), [4])

if __name__ == '__main__':

    main()
