from unittest import TestCase, main
from grokking.subsets.balance_parentheses.main import generate_valid_parentheses, generate_valid_parentheses_recursive

class TestSuite(TestCase):
    def test_1(self):
        expected = ['(())', '()()']
        self.assertListEqual(generate_valid_parentheses(2), expected)

    def test_2(self):
        expected = ['((()))', '(()())', '(())()', '()(())', '()()()']
        self.assertListEqual(generate_valid_parentheses(3), expected)

    def test_3(self):
        expected = ['(())', '()()']
        self.assertListEqual(generate_valid_parentheses_recursive(2), expected)

    def test_4(self):
        expected = ['((()))', '(()())', '(())()', '()(())', '()()()']
        self.assertListEqual(generate_valid_parentheses_recursive(3), expected)

if __name__ == '__main__':
    main()
