from unittest import TestCase, main
from leet.rotate_right.main import Solution
from data_structures.list_node import ListNode

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        result = s.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
        expected = ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))
        self.assertTrue(ListNode.compare(result, expected))

    def test_2(self):
        result = s.rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4)
        expected = ListNode(2, ListNode(0, ListNode(1)))
        self.assertTrue(ListNode.compare(result, expected))

    def test_3(self):
        result = s.rotateRight(ListNode(1), 1)
        expected = ListNode(1)
        self.assertTrue(ListNode.compare(result, expected))

if __name__ == '__main__':
    main()
