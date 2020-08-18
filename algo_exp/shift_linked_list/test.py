from algo_exp.shift_linked_list.main import shiftLinkedList
from data_structures.list_node import ListNode


def test_1():
    result = shiftLinkedList(ListNode(0, ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))), 2)
    expected = ListNode(4, ListNode(
        5, ListNode(0, ListNode(1, ListNode(2, ListNode(3))))))
    assert ListNode.compare(result, expected) is True

def test_2():
    result = shiftLinkedList(ListNode(0, ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))), -2)
    expected = ListNode(2, ListNode(
        3, ListNode(4, ListNode(5, ListNode(0, ListNode(1))))))
    assert ListNode.compare(result, expected) is True

def test_3():
    result = shiftLinkedList(ListNode(1), 1)
    expected = ListNode(1)
    assert ListNode.compare(result, expected) is True

def test_4():
    result = shiftLinkedList(ListNode(0, ListNode(1, ListNode(2))), 4)
    expected = ListNode(2, ListNode(0, ListNode(1)))
    assert ListNode.compare(result, expected) is True

def test_5():
    result = shiftLinkedList(ListNode(0, ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))), 18)
    expected = shiftLinkedList(ListNode(0, ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))), 18)
    assert ListNode.compare(result, expected) is True
