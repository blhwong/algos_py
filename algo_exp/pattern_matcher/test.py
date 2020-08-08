from unittest import TestCase, main
from algo_exp.pattern_matcher.main import patternMatcher


class TestSuite(TestCase):
    def test_1(self):
        result = patternMatcher('xxyxxy', 'gogopowerrangergogopowerranger')
        expected = ['go', 'powerranger']
        self.assertListEqual(result, expected)

    def test_2(self):
        result = patternMatcher('yyxyyx', 'gogopowerrangergogopowerranger')
        expected = ['powerranger', 'go']
        self.assertListEqual(result, expected)

    def test_3(self):
        result = patternMatcher('xxx', 'blahblahblah')
        expected = ['blah', '']
        self.assertListEqual(result, expected)

    def test_4(self):
        result = patternMatcher('yyyy', 'testtesttesttest')
        expected = ['', 'test']
        self.assertListEqual(result, expected)

if __name__ == '__main__':
    main()
