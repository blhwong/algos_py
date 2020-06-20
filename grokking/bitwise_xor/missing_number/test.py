from unittest import TestCase, main
from grokking.bitwise_xor.missing_number.main import find_missing_number


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_missing_number([1, 5, 2, 6, 4]), 3)

    def test_2(self):
        self.assertEqual(find_missing_number([1, 3, 4, 5, 6, 7, 2, 9, 10]), 8)


if __name__ == '__main__':
    main()
