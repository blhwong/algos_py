from unittest import TestCase, main
from algo_exp.min_max_stack.main import MinMaxStack


class TestSuite(TestCase):
    def test_1(self):
        stack = MinMaxStack()

        stack.push(5)
        self.assertEqual(stack.getMin(), 5)
        self.assertEqual(stack.getMax(), 5)
        self.assertEqual(stack.peek(), 5)

        stack.push(7)
        self.assertEqual(stack.getMin(), 5)
        self.assertEqual(stack.getMax(), 7)
        self.assertEqual(stack.peek(), 7)

        stack.push(2)
        self.assertEqual(stack.getMin(), 2)
        self.assertEqual(stack.getMax(), 7)
        self.assertEqual(stack.peek(), 2)

        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)

        self.assertEqual(stack.getMin(), 5)
        self.assertEqual(stack.getMax(), 5)
        self.assertEqual(stack.peek(), 5)

if __name__ == '__main__':
    main()
