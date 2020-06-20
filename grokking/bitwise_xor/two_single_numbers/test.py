from unittest import TestCase, main
from grokking.bitwise_xor.two_single_numbers.main import find_single_numbers


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(find_single_numbers(
            [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]), [4, 6])

    def test_2(self):
        self.assertListEqual(find_single_numbers([2, 1, 3, 2]), [1, 3])


if __name__ == '__main__':
    main()
