from unittest import TestCase, main
from leet.coin_change.main import Solution


s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.coinChange([1, 2, 5], 11), 3)

    def test_2(self):
        self.assertEqual(s.coinChange([2], 3), -1)

    def test_3(self):
        self.assertEqual(s.coinChange([1, 2, 3, 4], 0), 0)

    def test_4(self):
        self.assertEqual(s.coinChange([1, 5, 10, 25], 41), 4)

    def test_5(self):
        self.assertEqual(s.coinChange([2, 5, 10, 1], 27), 4)

    def test_6(self):
        self.assertEqual(s.coinChange([186, 419, 83, 408], 6249), 20)

if __name__ == '__main__':
    main()
