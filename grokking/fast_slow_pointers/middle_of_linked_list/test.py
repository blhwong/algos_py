from grokking.fast_slow_pointers.middle_of_linked_list.main import find_middle_of_linked_list
from data_structures.list_node import ListNode as Node


def test_1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    assert find_middle_of_linked_list(head) == head.next.next

def test_2():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    assert find_middle_of_linked_list(head) == head.next.next.next

def test_3():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    assert find_middle_of_linked_list(head) == head.next.next.next
