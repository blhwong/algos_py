from unittest import TestCase, main
from algo_exp.smallest_substring_containing.main import smallestSubstringContaining


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(smallestSubstringContaining('abcd$ef$axb$c$', '$$abf'), 'f$axb$')

    def test_2(self):
        self.assertEqual(smallestSubstringContaining('abcdefghijklmnopqrstuvwxyz', 'aajjttwwxxzz'), '')

    def test_3(self):
        result = smallestSubstringContaining('a$fuu+afff+affaffa+a$Affab+a+a+$a$bccgtt+aaaacA+++aaa$', 'a+$aaAaaaa$++')
        expected = 'affa+a$Affab+a+a+$a'
        self.assertEqual(result, expected)

    def test_4(self):
        result = smallestSubstringContaining('145624356128828193236336541277356789901', '123')
        expected = '1932'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
