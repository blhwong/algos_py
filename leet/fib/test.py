from unittest import TestCase, main
from main import fib

class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(0, fib(0))

    def test_2(self):
        self.assertEqual(1, fib(1))

    def test_3(self):
        self.assertEqual(1, fib(2))

    def test_4(self):
        self.assertEqual(2, fib(3))

    def test_5(self):
        self.assertEqual(3, fib(4))

    def test_6(self):
        self.assertEqual(5, fib(5))

    def test_7(self):
        self.assertEqual(8, fib(6))

    def test_8(self):
        self.assertEqual(13, fib(7))

if __name__ == '__main__':
    main()
