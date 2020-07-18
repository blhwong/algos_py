from unittest import TestCase, main
from algo_exp.same_bsts.main import sameBsts


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]))

    def test_2(self):
        self.assertFalse(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 13, 11, 94, 81]))

if __name__ == '__main__':
    main()
