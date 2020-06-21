from unittest import TestCase, main
from grokking.k_way_merge.smallest_number_range.main import find_smallest_range


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]]), [4, 7])

    def test_2(self):
        self.assertListEqual(find_smallest_range([[1, 9], [4, 12], [7, 10, 16]]), [9, 12])

if __name__ == '__main__':
    main()
