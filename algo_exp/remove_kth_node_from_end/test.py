from algo_exp.remove_kth_node_from_end.main import removeKthNodeFromEnd
from data_structures.list_node import ListNode


def test_1():
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9))))))))))
    removeKthNodeFromEnd(head, 4)
    expected = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(7, ListNode(8, ListNode(9)))))))))
    assert ListNode.compare(head, expected) is True

def test_2():
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9))))))))))
    removeKthNodeFromEnd(head, 1)
    expected = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))))
    assert ListNode.compare(head, expected) is True
