from algo_exp.linked_list_construction.main import Node, DoublyLinkedList


def getNodeValuesHeadToTail(linked_list):
    values = []
    node = linked_list.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def getNodeValuesTailToHead(linked_list):
    values = []
    node = linked_list.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne

def test_1():
    linked_list = DoublyLinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    three2 = Node(3)
    three3 = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    bindNodes(one, two)
    bindNodes(two, three)
    bindNodes(three, four)
    bindNodes(four, five)
    linked_list.head = one
    linked_list.tail = five

    linked_list.setHead(four)
    assert getNodeValuesHeadToTail(linked_list) == [4, 1, 2, 3, 5]
    assert getNodeValuesTailToHead(linked_list) == [5, 3, 2, 1, 4]

    linked_list.setTail(six)
    assert getNodeValuesHeadToTail(linked_list) == [4, 1, 2, 3, 5, 6]
    assert getNodeValuesTailToHead(linked_list) == [6, 5, 3, 2, 1, 4]

    linked_list.insertBefore(six, three)
    assert getNodeValuesHeadToTail(linked_list) == [4, 1, 2, 5, 3, 6]
    assert getNodeValuesTailToHead(linked_list) == [6, 3, 5, 2, 1, 4]

    linked_list.insertAfter(six, three2)
    assert getNodeValuesHeadToTail(linked_list) == [4, 1, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linked_list) == [3, 6, 3, 5, 2, 1, 4]

    linked_list.insertAtPosition(1, three3)
    assert getNodeValuesHeadToTail(linked_list) == [3, 4, 1, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linked_list) == [3, 6, 3, 5, 2, 1, 4, 3]

    linked_list.removeNodesWithValue(3)
    assert getNodeValuesHeadToTail(linked_list) == [4, 1, 2, 5, 6]
    assert getNodeValuesTailToHead(linked_list) == [6, 5, 2, 1, 4]

    linked_list.remove(two)
    assert getNodeValuesHeadToTail(linked_list) == [4, 1, 5, 6]
    assert getNodeValuesTailToHead(linked_list) == [6, 5, 1, 4]

    assert linked_list.containsNodeWithValue(5) is True


def test_2():
    one = Node(1)
    linked_list = DoublyLinkedList()
    linked_list.insertAtPosition(1, one)

    assert getNodeValuesHeadToTail(linked_list) == [1]
    assert getNodeValuesTailToHead(linked_list) == [1]
