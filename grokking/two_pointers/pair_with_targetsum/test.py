from unittest import TestCase, main
from grokking.two_pointers.pair_with_targetsum.main import pair_with_targetsum


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(pair_with_targetsum([1, 2, 3, 4, 6], 6), [1, 3])

    def test_2(self):
        self.assertCountEqual(pair_with_targetsum([2, 5, 9, 11], 11), [0, 2])


if __name__ == '__main__':
    main()
