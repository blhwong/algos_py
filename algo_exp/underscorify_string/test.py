from unittest import TestCase, main
from algo_exp.underscorify_string.main import underscorifySubstring


class TestSuite(TestCase):
    def test_1(self):
        result = underscorifySubstring('testthis is a testtest to see if testestest it works', 'test')
        expected = '_test_this is a _testtest_ to see if _testestest_ it works'
        self.assertEqual(result, expected)

    def test_2(self):
        result = underscorifySubstring('this is a test to see if it works and test', 'test')
        expected = 'this is a _test_ to see if it works and _test_'
        self.assertEqual(result, expected)

    def test_3(self):
        result = underscorifySubstring('this is a test to see if it works and test', 'bfjawkfja')
        expected = 'this is a test to see if it works and test'
        self.assertEqual(result, expected)

    def test_4(self):
        result = underscorifySubstring('tzttztttz', 'ttt')
        expected = 'tzttz_ttt_z'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    main()
