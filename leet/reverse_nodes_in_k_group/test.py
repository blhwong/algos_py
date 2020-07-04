from unittest import TestCase, main
from leet.reverse_nodes_in_k_group.main import Solution
from data_structures.list_node import ListNode as Node

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        result = s.reverseKGroup(head, 3)
        expected = Node(3, Node(2, Node(1, Node(4, Node(5)))))
        self.assertTrue(Node.compare(result, expected))

    def test_2(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        result = s.reverseKGroup(head, 2)
        expected = Node(2, Node(1, Node(4, Node(3, Node(5)))))
        self.assertTrue(Node.compare(result, expected))

if __name__ == '__main__':
    main()
