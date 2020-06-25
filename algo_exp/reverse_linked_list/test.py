from unittest import TestCase, main
from algo_exp.reverse_linked_list.main import reverseLinkedList
from data_structures.list_node import ListNode


class TestSuite(TestCase):
    def test_1(self):
        head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
        expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, ListNode(0))))))
        result = reverseLinkedList(head)
        self.assertTrue(ListNode.compare(result, expected))


if __name__ == '__main__':
    main()
