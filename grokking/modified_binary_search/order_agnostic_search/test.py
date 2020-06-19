from unittest import TestCase, main
from grokking.modified_binary_search.order_agnostic_search.main import binary_search


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(binary_search([4, 6, 10], 10), 2)

    def test_2(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 5), 4)

    def test_3(self):
        self.assertEqual(binary_search([10, 6, 4], 10), 0)

    def test_4(self):
        self.assertEqual(binary_search([10, 6, 4], 4), 2)


if __name__ == '__main__':
    main()
