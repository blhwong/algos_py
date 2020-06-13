from unittest import TestCase, main
from grokking.inplace_reversal_linked_list.reverse_linked_list.main import reverse
from data_structures.list_node import ListNode as Node

class TestSuite(TestCase):
    def test_1(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(8)
        head.next.next.next.next = Node(10)
        result = reverse(head)
        expected = Node(10, Node(8, Node(6, Node(4, Node(2)))))
        self.assertTrue(Node.compare(result, expected))


if __name__ == '__main__':
    main()
