from unittest import TestCase, main
from grokking.modified_binary_search.number_range.main import find_range


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(find_range([4, 6, 6, 6, 9], 6), [1, 3])


    def test_2(self):
        self.assertListEqual(find_range([1, 3, 8, 10, 15], 10), [3, 3])

    def test_3(self):
        self.assertListEqual(find_range([1, 3, 8, 10, 15], 12), [-1, -1])

    def test_4(self):
        self.assertListEqual(find_range([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1), [0, 9])


if __name__ == '__main__':
    main()
