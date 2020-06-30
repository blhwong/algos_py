from unittest import TestCase, main
from algo_exp.longest_peak.main import longestPeak


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]), 6)

    def test_2(self):
        self.assertEqual(longestPeak([1, 3, 2]), 3)

    def test_3(self):
        self.assertEqual(longestPeak([1, 2, 3]), 0)


if __name__ == '__main__':
    main()
