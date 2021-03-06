from algo_exp.rearrange_linked_list.main import rearrangeLinkedList, LinkedList

def get_list(head):
    array = []
    curr = head
    while curr:
        array.append(curr.value)
        curr = curr.next

    return array


def test_1():
    ll = LinkedList(3)
    ll.next = LinkedList(0)
    ll.next.next = LinkedList(5)
    ll.next.next.next = LinkedList(2)
    ll.next.next.next.next = LinkedList(1)
    ll.next.next.next.next.next = LinkedList(4)

    result = rearrangeLinkedList(ll, 3)

    assert get_list(result) == [0, 2, 1, 3, 5, 4]

def test_2():
    ll = LinkedList(3)
    ll.next = LinkedList(0)
    ll.next.next = LinkedList(2)
    ll.next.next.next = LinkedList(1)
    ll.next.next.next.next = LinkedList(4)
    ll.next.next.next.next.next = LinkedList(5)

    result = rearrangeLinkedList(ll, 4)

    assert get_list(result) == [3, 0, 2, 1, 4, 5]

def test_3():
    ll = LinkedList(3)
    ll.next = LinkedList(0)
    ll.next.next = LinkedList(2)
    ll.next.next.next = LinkedList(1)
    ll.next.next.next.next = LinkedList(4)
    ll.next.next.next.next.next = LinkedList(5)

    result = rearrangeLinkedList(ll, 0)

    assert get_list(result) == [0, 3, 2, 1, 4, 5]

def test_4():
    ll = LinkedList(0)
    ll.next = LinkedList(3)
    ll.next.next = LinkedList(2)
    ll.next.next.next = LinkedList(1)
    ll.next.next.next.next = LinkedList(4)
    ll.next.next.next.next.next = LinkedList(5)
    ll.next.next.next.next.next.next = LinkedList(3)
    ll.next.next.next.next.next.next.next = LinkedList(-1)
    ll.next.next.next.next.next.next.next.next = LinkedList(-2)
    ll.next.next.next.next.next.next.next.next.next = LinkedList(3)
    ll.next.next.next.next.next.next.next.next.next.next = LinkedList(6)
    ll.next.next.next.next.next.next.next.next.next.next.next = LinkedList(7)
    ll.next.next.next.next.next.next.next.next.next.next.next.next = LinkedList(3)
    ll.next.next.next.next.next.next.next.next.next.next.next.next.next = LinkedList(2)
    ll.next.next.next.next.next.next.next.next.next.next.next.next.next.next = LinkedList(-9000)

    result = rearrangeLinkedList(ll, -9000)
    expected = [
        -9000,
        0,
        3,
        2,
        1,
        4,
        5,
        3,
        -1,
        -2,
        3,
        6,
        7,
        3,
        2,
    ]
    assert get_list(result) == expected

def test_5():
    ll = LinkedList(3)
    ll.next = LinkedList(0)
    ll.next.next = LinkedList(5)
    ll.next.next.next = LinkedList(2)
    ll.next.next.next.next = LinkedList(1)
    ll.next.next.next.next.next = LinkedList(4)

    result = rearrangeLinkedList(ll, -1)

    assert get_list(result) == [3, 0, 5, 2, 1, 4]


def test_6():
    ll = LinkedList(6)
    ll.next = LinkedList(0)
    ll.next.next = LinkedList(5)
    ll.next.next.next = LinkedList(2)
    ll.next.next.next.next = LinkedList(1)
    ll.next.next.next.next.next = LinkedList(4)

    result = rearrangeLinkedList(ll, 3)

    assert get_list(result) == [0, 2, 1, 6, 5, 4]
