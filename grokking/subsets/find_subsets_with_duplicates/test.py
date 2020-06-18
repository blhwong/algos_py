from unittest import TestCase, main
from grokking.subsets.find_subsets_with_duplicates.main import find_subsets


class TestSuite(TestCase):
    def test_1(self):
        expected = [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
        self.assertCountEqual(find_subsets([1, 3, 3]), expected)

    def test_2(self):
        expected = [
            [],
            [1],
            [3],
            [1, 3],
            [3, 3],
            [1, 3, 3],
            [5],
            [1, 5],
            [3, 5],
            [1, 3, 5],
            [3, 3, 5],
            [1, 3, 3, 5],
        ]
        self.assertCountEqual(find_subsets([1, 5, 3, 3]), expected)


if __name__ == '__main__':
    main()
