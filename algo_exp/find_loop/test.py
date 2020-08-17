from algo_exp.find_loop.main import findLoop
from data_structures.list_node import ListNode as Node


def test_1():
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(5)
    head.next.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next.next.next.next.next = head.next.next.next.next
    assert findLoop(head) == head.next.next.next.next
