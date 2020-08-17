from algo_exp.merge_linked_list.main import mergeLinkedLists
from data_structures.list_node import ListNode


def test_1():
    head1 = ListNode(2, ListNode(6, ListNode(7, ListNode(8))))
    head2 = ListNode(1, ListNode(3, ListNode(4, ListNode(5, ListNode(9, ListNode(10))))))
    expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    result = mergeLinkedLists(head1, head2)
    assert ListNode.compare(result, expected) is True
