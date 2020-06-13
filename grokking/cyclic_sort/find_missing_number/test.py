from unittest import TestCase, main
from grokking.cyclic_sort.find_missing_number.main import find_missing_number


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_missing_number([4, 0, 3, 1]), 2)


    def test_2(self):
        self.assertEqual(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]), 7)


if __name__ == '__main__':
    main()
