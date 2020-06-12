from unittest import TestCase, main
from grokking.fast_slow_pointers.linked_list_cycle.main import has_cycle
from data_structures.list_node import ListNode as Node


class TestSuite(TestCase):
    def test_1(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
        self.assertFalse(has_cycle(head))


    def test_2(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = head.next.next
        self.assertTrue(has_cycle(head))


if __name__ == '__main__':
    main()
