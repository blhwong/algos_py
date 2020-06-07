from unittest import TestCase, main
from grokking.sliding_window.length_of_longest_substring.main import length_of_longest_substring


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(length_of_longest_substring('aabccbb', 2), 5)

    def test_2(self):
        self.assertEqual(length_of_longest_substring('abbcb', 1), 4)

    def test_3(self):
        self.assertEqual(length_of_longest_substring('abccde', 1), 3)

    def test_4(self):
        self.assertEqual(length_of_longest_substring('abbcb', 2), 5)

if __name__ == '__main__':
    main()
