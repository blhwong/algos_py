from unittest import TestCase, main
from leet.valid_parenthesis.main import Solution

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(s.isValid('()'))

    def test_2(self):
        self.assertTrue(s.isValid('()[]{}'))

    def test_3(self):
        self.assertFalse(s.isValid('(]'))

    def test_4(self):
        self.assertFalse(s.isValid('([)]'))

    def test_5(self):
        self.assertTrue(s.isValid('{[]}'))

    def test_6(self):
        self.assertFalse(s.isValid('['))

    def test_7(self):
        self.assertFalse(s.isValid(']'))

if __name__ == '__main__':
    main()
