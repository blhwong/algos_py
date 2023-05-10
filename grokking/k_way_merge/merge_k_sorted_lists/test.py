from grokking.k_way_merge.merge_k_sorted_lists.main import merge_lists
from data_structures.list_node import ListNode


def test_1():
    l1 = ListNode(2, ListNode(6, ListNode(8)))
    l2 = ListNode(3, ListNode(6, ListNode(7)))
    l3 = ListNode(1, ListNode(3, ListNode(4)))
    expected = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(6, ListNode(6, ListNode(7, ListNode(8)))))))))
    assert ListNode.compare(merge_lists([l1, l2, l3]), expected)

def test_2():
    l1 = ListNode(5, ListNode(8, ListNode(9)))
    l2 = ListNode(1, ListNode(7))
    expected = ListNode(1, ListNode(5, ListNode(7, ListNode(8, ListNode(9)))))
    assert ListNode.compare(merge_lists([l1, l2]), expected)
