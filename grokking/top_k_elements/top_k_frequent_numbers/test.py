from unittest import TestCase, main
from grokking.top_k_elements.top_k_frequent_numbers.main import find_k_frequent_numbers


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2), [12, 11])

    def test_2(self):
        self.assertCountEqual(find_k_frequent_numbers([5, 12, 11, 3, 11], 2), [11, 3])

if __name__ == '__main__':
    main()
