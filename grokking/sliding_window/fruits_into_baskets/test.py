from unittest import TestCase, main
from grokking.sliding_window.fruits_into_baskets.main import fruits_into_baskets


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']), 3)

    def test_2(self):
        self.assertEqual(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']), 5)

    def test_3(self):
        self.assertEqual(fruits_into_baskets(
            ['A', 'B', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']), 7)

if __name__ == '__main__':
    main()
