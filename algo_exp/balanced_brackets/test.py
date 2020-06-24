from unittest import TestCase, main
from algo_exp.balanced_brackets.main import balancedBrackets


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(balancedBrackets('([])(){}(())()()'))

    def test_2(self):
        self.assertFalse(balancedBrackets('[(])'))

    def test_3(self):
        self.assertTrue(balancedBrackets('(a)'))

if __name__ == '__main__':
    main()
