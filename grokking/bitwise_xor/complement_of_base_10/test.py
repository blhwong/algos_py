from unittest import TestCase, main
from grokking.bitwise_xor.complement_of_base_10.main import calculate_bitwise_complement


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(calculate_bitwise_complement(8), 7)

    def test_2(self):
        self.assertEqual(calculate_bitwise_complement(10), 5)


if __name__ == '__main__':
    main()
