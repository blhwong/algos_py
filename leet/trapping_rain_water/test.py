from unittest import TestCase, main
from leet.trapping_rain_water.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)


if __name__ == '__main__':
    main()
