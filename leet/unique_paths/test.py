from unittest import TestCase, main
from leet.unique_paths.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.uniquePaths(3, 2), 3)

    def test_2(self):
        self.assertEqual(s.uniquePaths(7, 3), 28)

    def test_3(self):
        self.assertEqual(s.uniquePaths(2, 3), 3)

    def test_4(self):
        self.assertEqual(s.uniquePaths(4, 2), 4)

    def test_5(self):
        self.assertEqual(s.uniquePaths(2, 4), 4)

    def test_6(self):
        self.assertEqual(s.uniquePaths(3, 3), 6)

    def test_7(self):
        self.assertEqual(s.uniquePaths(
            100, 100), 22750883079422934966181954039568885395604168260154104734000)

if __name__ == '__main__':
    main()
