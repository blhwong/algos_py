from unittest import TestCase, main
from grokking.cyclic_sort.find_all_duplicates.main import find_all_duplicates


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(find_all_duplicates([3, 4, 4, 5, 5]), [4, 5])

    def test_2(self):
        self.assertCountEqual(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]), [3, 5])


if __name__ == '__main__':

    main()
