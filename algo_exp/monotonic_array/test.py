from unittest import TestCase, main
from algo_exp.monotonic_array.main import isMonotonic


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))

    def test_2(self):
        self.assertTrue(isMonotonic([1, 2, 3, 4, 5, 6, 7]))

    def test_3(self):
        self.assertTrue(isMonotonic([1, 1, 1, 1, 1, 1, 1]))

    def test_4(self):
        self.assertFalse(isMonotonic([1, 0, 1]))

    def test_5(self):
        self.assertFalse(isMonotonic([0, 1, 2, 2, 1]))


if __name__ == '__main__':
    main()
