from unittest import TestCase, main
from leet.stack_using_queues.main import MyStack


class TestSuite(TestCase):
    def test_1(self):
        stack = MyStack()
        empty = stack.empty()
        stack.push(1)
        not_empty = stack.empty()
        top_1 = stack.top()
        stack.push(2)
        stack.push(3)
        top_3 = stack.top()
        three = stack.pop()
        two = stack.pop()
        one = stack.pop()

        self.assertTrue(empty)
        self.assertFalse(not_empty)
        self.assertEqual(top_1, 1)
        self.assertEqual(top_3, 3)
        self.assertEqual(three, 3)
        self.assertEqual(two, 2)
        self.assertEqual(one, 1)




if __name__ == '__main__':
    main()
