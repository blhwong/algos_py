from unittest import TestCase, main
from leet.permutation_sequence.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.getPermutation(3, 3), '213')

    def test_2(self):
        self.assertEqual(s.getPermutation(4, 9), '2314')

    def test_3(self):
        self.assertEqual(s.getPermutation(9, 278621), '792861534')

if __name__ == '__main__':
    main()
