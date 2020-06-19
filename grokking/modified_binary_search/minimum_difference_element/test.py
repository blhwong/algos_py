from unittest import TestCase, main
from grokking.modified_binary_search.minimum_difference_element.main import search_min_diff_element


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(search_min_diff_element([4, 6, 10], 7), 6)

    def test_2(self):
        self.assertEqual(search_min_diff_element([4, 6, 10], 4), 4)

    def test_3(self):
        self.assertEqual(search_min_diff_element([1, 3, 8, 10, 15], 12), 10)

    def test_4(self):
        self.assertEqual(search_min_diff_element([4, 6, 10], 17), 10)


if __name__ == '__main__':
    main()
