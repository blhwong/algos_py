from unittest import TestCase, main
from grokking.cyclic_sort.find_duplicate.main import find_duplicate


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_duplicate([1, 4, 4, 3, 2]), 4)

    def test_2(self):
        self.assertEqual(find_duplicate([2, 1, 3, 3, 5, 4]), 3)

    def test_3(self):
        self.assertEqual(find_duplicate([2, 4, 1, 4, 4]), 4)


if __name__ == '__main__':

    main()
