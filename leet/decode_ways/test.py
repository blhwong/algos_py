from unittest import TestCase, main
from leet.decode_ways.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.numDecodings('12'), 2)

    def test_2(self):
        self.assertEqual(s.numDecodings('226'), 3)

    def test_3(self):
        self.assertEqual(s.numDecodings('0'), 0)

    def test_4(self):
        self.assertEqual(s.numDecodings('10'), 1)

    def test_5(self):
        self.assertEqual(s.numDecodings('1'), 1)

    def test_6(self):
        self.assertEqual(s.numDecodings(''), 1)

    def test_7(self):
        self.assertEqual(s.numDecodings('01'), 0)

    def test_8(self):
        self.assertEqual(s.numDecodings('100'), 0)

if __name__ == '__main__':
    main()
