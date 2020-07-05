from unittest import TestCase, main
from leet.multiply_strings.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.multiply('2', '3'), '6')

    def test_2(self):
        self.assertEqual(s.multiply('123', '456'), '56088')

    def test_3(self):
        self.assertEqual(s.multiply('9', '9'), '81')

    def test_4(self):
        self.assertEqual(s.multiply('99', '99'), '9801')

    def test_5(self):
        self.assertEqual(s.multiply('9133', '0'), '0')

    def test_6(self):
        self.assertEqual(s.multiply('123', '987'), '121401')

    def test_7(self):
        self.assertEqual(s.multiply('6', '501'), '3006')

if __name__ == '__main__':
    main()
