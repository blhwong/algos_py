from unittest import TestCase, main
from grokking.two_pointers.dutch_flag_sort.main import dutch_flag_sort


class TestSuite(TestCase):
    def test_1(self):
        arr = [1, 0, 2, 1, 0]
        expected = [0, 0, 1, 1, 2]
        dutch_flag_sort(arr)
        self.assertListEqual(arr, expected)

    def test_2(self):
        arr = [2, 2, 0, 1, 2, 0]
        expected = [0, 0, 1, 2, 2, 2]
        dutch_flag_sort(arr)
        self.assertListEqual(arr, expected)


if __name__ == '__main__':
    main()
