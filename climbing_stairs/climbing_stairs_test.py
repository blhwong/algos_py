from unittest import TestCase, main
from climbing_stairs import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.climbStairs(2), 2)
        self.assertEqual(s.bottom_up(2), 2)
        self.assertEqual(s.fib(2), 2)

    def test_2(self):
        self.assertEqual(s.climbStairs(3), 3)
        self.assertEqual(s.bottom_up(3), 3)
        self.assertEqual(s.fib(3), 3)


    def test_3(self):
        self.assertEqual(s.climbStairs(100), 573147844013817084101)
        self.assertEqual(s.bottom_up(100), 573147844013817084101)
        self.assertEqual(s.fib(100), 573147844013817084101)


    def test_4(self):
        self.assertEqual(s.climbStairs(4), 5)
        self.assertEqual(s.bottom_up(4), 5)
        self.assertEqual(s.fib(4), 5)

    def test_5(self):
        self.assertEqual(s.climbStairs(5), 8)
        self.assertEqual(s.bottom_up(5), 8)
        self.assertEqual(s.fib(5), 8)

    def test_6(self):
        self.assertEqual(s.climbStairs(0), 1)
        self.assertEqual(s.bottom_up(0), 1)
        self.assertEqual(s.fib(0), 1)

    def test_7(self):
        self.assertEqual(s.climbStairs(1), 1)
        self.assertEqual(s.bottom_up(1), 1)
        self.assertEqual(s.fib(1), 1)

if __name__ == '__main__':
    main()
