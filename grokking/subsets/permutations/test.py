from unittest import TestCase, main
from grokking.subsets.permutations.main import find_permutations, find_permutations_recursive


class TestSuite(TestCase):
    def test_1(self):
        expected = [[1, 3, 5], [1, 5, 3], [3, 1, 5],
                    [3, 5, 1], [5, 1, 3], [5, 3, 1]]
        self.assertCountEqual(find_permutations([1, 3, 5]), expected)

    def test_2(self):
        expected = [[1, 3, 5], [1, 5, 3], [3, 1, 5],
                    [3, 5, 1], [5, 1, 3], [5, 3, 1]]
        self.assertCountEqual(find_permutations_recursive([1, 3, 5]), expected)


if __name__ == '__main__':
    main()
