from unittest import TestCase, main
from main import Solution

from leet.data_structures.list_node import ListNode


s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
        self.assertTrue(ListNode.compare(expected, s.removeNthFromEnd(n, 2)))

    def test_2(self):
        expected = None
        self.assertTrue(ListNode.compare(expected, s.removeNthFromEnd(ListNode(1), 1)))

    def test_3(self):
        expected = ListNode(2)
        self.assertTrue(ListNode.compare(expected, s.removeNthFromEnd(ListNode(1, ListNode(2)), 2)))

if __name__ == '__main__':
    main()
