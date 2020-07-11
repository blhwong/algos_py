from unittest import TestCase, main
from algo_exp.levenshtein_distance.main import levenshteinDistance


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(levenshteinDistance('abc', 'yabd'), 2)


if __name__ == '__main__':
    main()
