from unittest import TestCase, main
from grokking.inplace_reversal_linked_list.reverse_sub_list.main import reverse_sub_list
from data_structures.list_node import ListNode as Node


class TestSuite(TestCase):
    def test_1(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        result = reverse_sub_list(head, 2, 4)
        expected = Node(1, Node(4, Node(3, Node(2, Node(5)))))
        self.assertTrue(Node.compare(result, expected))


    def test_2(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        result = reverse_sub_list(head, 1, 3)
        expected = Node(3, Node(2, Node(1, Node(4, Node(5)))))
        self.assertTrue(Node.compare(result, expected))


    def test_3(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        result = reverse_sub_list(head, 2, 10)
        expected = Node(1, Node(5, Node(4, Node(3, Node(2)))))
        self.assertTrue(Node.compare(result, expected))

if __name__ == '__main__':
    main()
