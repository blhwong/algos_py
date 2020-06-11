from unittest import TestCase, main
from grokking.fast_slow_pointers.happy_number.main import find_happy_number


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(find_happy_number(23))

    def test_2(self):
        self.assertFalse(find_happy_number(12))


if __name__ == '__main__':
    main()
