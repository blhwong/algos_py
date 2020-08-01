from unittest import TestCase, main
from algo_exp.search_for_range.main import searchForRange


class TestSuite(TestCase):
    def test_1(self):
        array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
        self.assertListEqual(searchForRange(array, 45), [4, 9])

if __name__ == '__main__':
    main()
