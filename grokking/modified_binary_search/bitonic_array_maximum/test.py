from unittest import TestCase, main
from grokking.modified_binary_search.bitonic_array_maximum.main import find_max_in_bitonic_array


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]), 12)

    def test_2(self):
        self.assertEqual(find_max_in_bitonic_array([3, 8, 3, 1]), 8)

    def test_3(self):
        self.assertEqual(find_max_in_bitonic_array([1, 3, 8, 12]), 12)

    def test_4(self):
        self.assertEqual(find_max_in_bitonic_array([10, 9, 8]), 10)


if __name__ == '__main__':
    main()
