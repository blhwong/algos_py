from unittest import TestCase, main
from algo_exp.nth_fibonacci.main import getNthFib


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(getNthFib(2), 1)

    def test_2(self):
        self.assertEqual(getNthFib(6), 5)


if __name__ == '__main__':
    main()
