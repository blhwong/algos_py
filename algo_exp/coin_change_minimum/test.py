from unittest import TestCase, main
from algo_exp.coin_change_minimum.main import minNumberOfCoinsForChange


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(minNumberOfCoinsForChange(6, [1, 5]), 2)

    def test_2(self):
        self.assertEqual(minNumberOfCoinsForChange(10, [1, 5, 10]), 1)

    def test_3(self):
        self.assertEqual(minNumberOfCoinsForChange(0, [1, 2, 3]), 0)

    def test_4(self):
        self.assertEqual(minNumberOfCoinsForChange(10, []), -1)

    def test_5(self):
        self.assertEqual(minNumberOfCoinsForChange(12, [2, 3, 7]), 3)

    def test_6(self):
        self.assertEqual(minNumberOfCoinsForChange(7, [2, 3, 4, 7]), 1)

    def test_7(self):
        self.assertEqual(minNumberOfCoinsForChange(41, [1, 5, 10, 25]), 4)

    def test_8(self):
        self.assertEqual(minNumberOfCoinsForChange(7, [1, 5, 10]), 3)

    def test_9(self):
        self.assertEqual(minNumberOfCoinsForChange(10, [11]), -1)

    def test_10(self):
        self.assertEqual(minNumberOfCoinsForChange(7, [2, 4]), -1)

if __name__ == '__main__':
    main()
