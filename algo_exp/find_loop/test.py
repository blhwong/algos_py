from unittest import TestCase, main
from algo_exp.find_loop.main import findLoop
from data_structures.list_node import ListNode as Node


class TestSuite(TestCase):
    def test_1(self):
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(4)
        head.next.next.next.next.next = Node(5)
        head.next.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next.next = Node(7)
        head.next.next.next.next.next.next.next.next = Node(8)
        head.next.next.next.next.next.next.next.next.next = Node(9)
        head.next.next.next.next.next.next.next.next.next.next = head.next.next.next.next
        self.assertTrue(findLoop(head) == head.next.next.next.next)

if __name__ == '__main__':
    main()
