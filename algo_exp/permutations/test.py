from unittest import TestCase, main
from algo_exp.permutations.main import get_permutations


class TestSuite(TestCase):

    def test_1(self):
        self.assertCountEqual(get_permutations([1, 2, 3]), [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ])


if __name__ == '__main__':
    main()
