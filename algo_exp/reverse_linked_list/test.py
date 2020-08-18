from algo_exp.reverse_linked_list.main import reverseLinkedList
from data_structures.list_node import ListNode


def test_1():
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, ListNode(0))))))
    result = reverseLinkedList(head)
    assert ListNode.compare(result, expected) is True
