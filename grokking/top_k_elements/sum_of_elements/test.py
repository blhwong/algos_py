from unittest import TestCase, main
from grokking.top_k_elements.sum_of_elements.main import find_sum_of_elements


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6), 23)

    def test_2(self):
        self.assertEqual(find_sum_of_elements([3, 5, 8, 7], 1, 4), 12)

if __name__ == '__main__':
    main()
