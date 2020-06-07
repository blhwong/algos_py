from unittest import TestCase, main
from grokking.sliding_window.length_of_longest_subarray.main import length_of_longest_subarray


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(length_of_longest_subarray(
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2), 6)

    def test_2(self):
        self.assertEqual(length_of_longest_subarray(
            [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3), 9)


if __name__ == '__main__':
    main()
