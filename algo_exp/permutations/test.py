from unittest import TestCase, main
from algo_exp.permutations.main import getPermutations


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(getPermutations([1, 2, 3]), [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ])

if __name__ == '__main__':
    main()
