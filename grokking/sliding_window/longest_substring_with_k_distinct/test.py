from unittest import TestCase, main
from main import longest_substring_with_k_distinct


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(longest_substring_with_k_distinct('araaci', 2), 4)


    def test_2(self):
        self.assertEqual(longest_substring_with_k_distinct('araaci', 1), 2)


    def test_3(self):
        self.assertEqual(
            longest_substring_with_k_distinct('araaci', 3), 5)


if __name__ == '__main__':
    main()
