from unittest import TestCase, main
from leet.house_robber.main import Solution


s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.rob([1, 2, 3, 1]), 4)

    def test_2(self):
        self.assertEqual(s.rob([2, 7, 9, 3, 1]), 12)

    def test_3(self):
        self.assertEqual(s.rob([10, 1, 1, 10]), 20)

    def test_4(self):
        self.assertEqual(s.rob([]), 0)


if __name__ == '__main__':
    main()
