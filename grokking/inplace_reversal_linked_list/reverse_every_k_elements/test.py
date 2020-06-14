from unittest import TestCase, main
from grokking.inplace_reversal_linked_list.reverse_every_k_elements.main import reverse_every_k_elements
from data_structures.list_node import ListNode as Node


class TestSuite(TestCase):
    def test_1(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
        result = reverse_every_k_elements(head, 3)
        expected = Node(3, Node(2, Node(1, Node(6, Node(5, Node(4, Node(8, Node(7))))))))
        self.assertTrue(Node.compare(result, expected))


if __name__ == '__main__':
    main()
