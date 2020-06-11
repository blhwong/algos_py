from unittest import TestCase, main
from grokking.fast_slow_pointers.find_cycle_start.main import find_cycle_start
from leet.data_structures.list_node import ListNode as Node


class TestSuite(TestCase):
    def test_1(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = head.next.next
        self.assertTrue(find_cycle_start(head) == head.next.next)


    def test_2(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = head.next.next.next
        self.assertTrue(find_cycle_start(head) == head.next.next.next)


    def test_3(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = head
        self.assertTrue(find_cycle_start(head) == head)


if __name__ == '__main__':
    main()
