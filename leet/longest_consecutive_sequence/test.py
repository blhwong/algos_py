from unittest import TestCase, main
from leet.longest_consecutive_sequence.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_2(self):
        self.assertEqual(s.longestConsecutive([1, 3, 2, 99, 4, 101, 100, 103, 102]), 5)

    def test_3(self):
        self.assertEqual(s.longestConsecutive([-4, -3, -2, -1, 100, 101, 102]), 4)

    def test_4(self):
        self.assertEqual(s.longestConsecutive([1, 3, 5, 7, 9]), 1)

    def test_5(self):
        self.assertEqual(s.longestConsecutive([]), 0)

    def test_6(self):
        self.assertEqual(s.longestConsecutive([0]), 1)

    def test_7(self):
        self.assertEqual(s.longestConsecutive([2147483646, -2147483647, 0, 2, 2147483644, -2147483645, 2147483645]), 3)


if __name__ == '__main__':
    main()
