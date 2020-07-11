from unittest import TestCase, main
from algo_exp.coin_change_possibilities.main import numberOfWaysToMakeChange


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(numberOfWaysToMakeChange(6, [1, 5]), 2)

    def test_2(self):
        self.assertEqual(numberOfWaysToMakeChange(10, [1, 5, 10]), 4)

    def test_3(self):
        self.assertEqual(numberOfWaysToMakeChange(0, [1, 2, 3]), 1)

    def test_4(self):
        self.assertEqual(numberOfWaysToMakeChange(10, []), 0)

    def test_5(self):
        self.assertEqual(numberOfWaysToMakeChange(12, [2, 3, 7]), 4)

    def test_6(self):
        self.assertEqual(numberOfWaysToMakeChange(7, [2, 3, 4, 7]), 3)

if __name__ == '__main__':
    main()
