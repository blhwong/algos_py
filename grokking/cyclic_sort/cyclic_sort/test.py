from unittest import TestCase, main
from grokking.cyclic_sort.cyclic_sort.main import cyclic_sort


class TestSuite(TestCase):
    def test_1(self):
        arr = [3, 1, 5, 4, 2]
        cyclic_sort(arr)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])

    def test_2(self):
        arr = [2, 6, 4, 3, 1, 5]
        cyclic_sort(arr)
        self.assertListEqual(arr, [1, 2, 3, 4, 5, 6])

    def test_3(self):
        arr = [1, 5, 6, 4, 3, 2]
        cyclic_sort(arr)
        self.assertListEqual(arr, [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    main()
