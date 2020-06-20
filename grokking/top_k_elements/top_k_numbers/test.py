from unittest import TestCase, main
from grokking.top_k_elements.top_k_numbers.main import find_k_largest_numbers


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3), [5, 12, 11])

    def test_2(self):
        self.assertCountEqual(find_k_largest_numbers([5, 12, 11, -1, 12], 3), [12, 11, 12])


if __name__ == '__main__':
    main()
