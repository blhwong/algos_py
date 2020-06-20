from unittest import TestCase, main
from grokking.top_k_elements.maximum_distinct_elements.main import find_maximum_distinct_elements


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2), 3)

    def test_2(self):
        self.assertEqual(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3), 2)

    def test_3(self):
        self.assertEqual(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2), 3)


if __name__ == '__main__':
    main()
