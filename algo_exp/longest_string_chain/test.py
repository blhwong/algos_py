from unittest import TestCase, main
from algo_exp.longest_string_chain.main import longestStringChain

class TestSuite(TestCase):
    def test_1(self):
        result = longestStringChain([
            'abde',
            'abc',
            'abd',
            'abcde',
            'ade',
            'ae',
            'labde',
            'abcdef',
        ])
        expected = [
            'abcdef',
            'abcde',
            'abde',
            'ade',
            'ae',
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
