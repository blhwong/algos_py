from unittest import TestCase, main
from grokking.bitwise_xor.single_number.main import find_single_number


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_single_number([1, 4, 2, 1, 3, 2, 3]), 4)

    def test_2(self):
        self.assertEqual(find_single_number([7, 9, 7]), 9)


if __name__ == '__main__':
    main()
