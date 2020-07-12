from unittest import TestCase, main
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

class TestSuite(TestCase):
    def test_1(self):
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
        self.assertEqual(getNodeValuesHeadToTail(linked_list), [4, 1, 2, 3, 5])
        self.assertEqual(getNodeValuesTailToHead(linked_list), [5, 3, 2, 1, 4])

        linked_list.setTail(six)
        self.assertEqual(getNodeValuesHeadToTail(
            linked_list), [4, 1, 2, 3, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(
            linked_list), [6, 5, 3, 2, 1, 4])

        linked_list.insertBefore(six, three)
        self.assertEqual(getNodeValuesHeadToTail(
            linked_list), [4, 1, 2, 5, 3, 6])
        self.assertEqual(getNodeValuesTailToHead(
            linked_list), [6, 3, 5, 2, 1, 4])

        linked_list.insertAfter(six, three2)
        self.assertEqual(getNodeValuesHeadToTail(
            linked_list), [4, 1, 2, 5, 3, 6, 3])
        self.assertEqual(getNodeValuesTailToHead(
            linked_list), [3, 6, 3, 5, 2, 1, 4])

        linked_list.insertAtPosition(1, three3)
        self.assertEqual(getNodeValuesHeadToTail(
            linked_list), [3, 4, 1, 2, 5, 3, 6, 3])
        self.assertEqual(getNodeValuesTailToHead(
            linked_list), [3, 6, 3, 5, 2, 1, 4, 3])

        linked_list.removeNodesWithValue(3)
        self.assertEqual(getNodeValuesHeadToTail(linked_list), [4, 1, 2, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linked_list), [6, 5, 2, 1, 4])

        linked_list.remove(two)
        self.assertEqual(getNodeValuesHeadToTail(linked_list), [4, 1, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linked_list), [6, 5, 1, 4])

        self.assertEqual(linked_list.containsNodeWithValue(5), True)


if __name__ == '__main__':
    main()
