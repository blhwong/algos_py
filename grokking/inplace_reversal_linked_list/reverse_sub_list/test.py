from grokking.inplace_reversal_linked_list.reverse_sub_list.main import reverse_sub_list
from data_structures.list_node import ListNode as Node


def test_1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    result = reverse_sub_list(head, 2, 4)
    expected = Node(1, Node(4, Node(3, Node(2, Node(5)))))
    assert Node.compare(result, expected)


def test_2():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    result = reverse_sub_list(head, 1, 3)
    expected = Node(3, Node(2, Node(1, Node(4, Node(5)))))
    assert Node.compare(result, expected)


def test_3():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    result = reverse_sub_list(head, 2, 10)
    expected = Node(1, Node(5, Node(4, Node(3, Node(2)))))
    assert Node.compare(result, expected)


def test_4():
    head = Node(5)
    head.next = Node(4)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    result = reverse_sub_list(head, 2, 4)
    expected = Node(5, Node(2, Node(3, Node(4, Node(1)))))
    assert Node.compare(result, expected)
