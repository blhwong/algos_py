from data_structures.list_node import ListNode

def test_compare_false():
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    assert list1 != list2

def test_compare_true():
    list1 = ListNode(1, ListNode(2, ListNode(3)))
    list2 = ListNode(1, ListNode(2, ListNode(3)))

    assert list1 == list2

def test_repr():
    list1 = ListNode(1, ListNode(2, ListNode(3)))

    expected = '1->2->3'

    assert repr(list1) == expected
