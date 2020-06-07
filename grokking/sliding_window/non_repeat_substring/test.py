from unittest import TestCase, main
from grokking.sliding_window.non_repeat_substring.main import non_repeat_substring


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(non_repeat_substring('aabccbb'), 3)

    def test_2(self):
        self.assertEqual(non_repeat_substring('abbbb'), 2)

    def test_3(self):
        self.assertEqual(non_repeat_substring('abccde'), 3)


if __name__ == '__main__':
    main()
