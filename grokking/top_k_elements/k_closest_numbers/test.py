from unittest import TestCase, main
from grokking.top_k_elements.k_closest_numbers.main import find_closest_elements


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(find_closest_elements([5, 6, 7, 8, 9], 3, 7), [6, 7, 8])

    def test_2(self):
        self.assertCountEqual(find_closest_elements([2, 4, 5, 6, 9], 3, 6), [4, 5, 6])

    def test_3(self):
        self.assertCountEqual(find_closest_elements([2, 4, 5, 6, 9], 3, 10), [5, 6, 9])


if __name__ == '__main__':
    main()
