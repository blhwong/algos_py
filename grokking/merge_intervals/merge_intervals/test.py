from unittest import TestCase, main
from grokking.fast_slow_pointers.middle_of_linked_list.main import find_middle_of_linked_list
from data_structures.list_node import ListNode as Node


class TestSuite(TestCase):
    def test_1(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        self.assertTrue(find_middle_of_linked_list(head) == head.next.next)

    def test_2(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        self.assertTrue(find_middle_of_linked_list(head)
                        == head.next.next.next)

    def test_3(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = Node(7)
        self.assertTrue(find_middle_of_linked_list(head)
                        == head.next.next.next)


if __name__ == '__main__':
    main()
