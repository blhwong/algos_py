from unittest import TestCase, main
from leet.min_integer_after_k_swaps.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.minInteger('4321', 4), '1342')

    def test_2(self):
        self.assertEqual(s.minInteger('100', 1), '010')

    def test_3(self):
        self.assertEqual(s.minInteger('36789', 1000), '36789')

    def test_4(self):
        self.assertEqual(s.minInteger('22', 22), '22')

if __name__ == '__main__':
    main()
