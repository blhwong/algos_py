from unittest import TestCase, main
from grokking.top_k_elements.connect_ropes.main import minimum_cost_to_connect_ropes


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(minimum_cost_to_connect_ropes([1, 3, 11, 5]), 33)

    def test_2(self):
        self.assertEqual(minimum_cost_to_connect_ropes([3, 4, 5, 6]), 36)

    def test_3(self):
        self.assertEqual(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2]), 42)

if __name__ == '__main__':
    main()
